"""Clinic Information Assistant: a local, model-free classroom application.
Run: python3 app.py (Mac) or py app.py (Windows). No pip installs.
"""
import argparse
import json
import re
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

FOLDER = Path(__file__).resolve().parent


def normalize(text):
    """Ignore capitalization and punctuation, but do not pretend to understand meaning."""
    return ' '.join(re.findall(r'\w+', text.lower()))


def load_faqs():
    """Read on each question so workshop edits take effect without restarting."""
    items = json.loads((FOLDER / 'faqs.json').read_text(encoding='utf-8'))
    if not isinstance(items, list) or not items:
        raise ValueError('The FAQ file must contain a nonempty list.')
    seen = set()
    for item in items:
        for key in ('id', 'question', 'answer'):
            if not isinstance(item.get(key), str) or not item[key].strip():
                raise ValueError('Each FAQ needs an id, question, and answer.')
        for key in ('aliases', 'keywords'):
            if not isinstance(item.get(key), list) or not all(isinstance(x, str) for x in item[key]):
                raise ValueError('Each FAQ needs aliases and keywords lists.')
        if item['id'] in seen:
            raise ValueError('FAQ IDs must be unique.')
        seen.add(item['id'])
    return items


def find_answer(question, faqs):
    """Exact known question -> answer; keyword overlap -> related sources only."""
    query = normalize(question)
    for faq in faqs:
        if query in [normalize(x) for x in [faq['question']] + faq['aliases']]:
            return {'status': 'found', 'message': 'A matching FAQ was found.', 'sources': [faq]}
    words = set(query.split())
    related = [faq for faq in faqs if any(
        set(normalize(keyword).split()).issubset(words) and normalize(keyword)
        for keyword in faq['keywords'])]
    if related:
        return {'status': 'related', 'message': 'No exact question match. These related FAQs may not answer your question. Check the source; do not assume missing details.', 'sources': related[:3]}
    return {'status': 'unknown', 'message': 'I could not find that information in the supplied clinic FAQs. Please check an approved source or ask the appropriate clinic team.', 'sources': []}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass  # Do not log participants' questions.

    def send(self, status, body, content_type='application/json; charset=utf-8'):
        data = json.dumps(body).encode('utf-8') if isinstance(body, dict) else body
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == '/':
            self.send(200, (FOLDER / 'index.html').read_bytes(), 'text/html; charset=utf-8')
        elif self.path == '/api/faqs':
            try:
                self.send(200, {'faqs': load_faqs()})
            except (OSError, ValueError, TypeError, AttributeError):
                self.send(500, {'error': 'Check faqs.json: it must contain valid JSON and the required FAQ fields.'})
        else:
            self.send(404, {'error': 'Page not found.'})

    def do_POST(self):
        # JSON requests from our page only; do not enable cross-origin access.
        if self.headers.get('Content-Type', '').split(';')[0] != 'application/json':
            self.send(415, {'error': 'Send JSON from the workshop page.'})
            return
        origin = self.headers.get('Origin')
        allowed = {f'http://127.0.0.1:{self.server.server_port}', f'http://localhost:{self.server.server_port}'}
        if origin and origin not in allowed:
            self.send(403, {'error': 'Use the local workshop page.'})
            return
        try:
            size = int(self.headers.get('Content-Length', '0'))
            if not 0 < size <= 4096:
                raise ValueError('Invalid size')
            data = json.loads(self.rfile.read(size))
            if not isinstance(data, dict):
                raise ValueError('Expected an object')
        except (ValueError, UnicodeError):
            self.send(400, {'error': 'Please send a short, valid request.'})
            return
        try:
            faqs = load_faqs()
            if self.path == '/api/ask':
                question = data.get('question')
                if not isinstance(question, str) or not question.strip() or len(question) > 300:
                    self.send(400, {'error': 'Enter a question of 1–300 characters.'})
                    return
                self.send(200, find_answer(question, faqs))
            elif self.path == '/api/feedback':
                rating, source_id = data.get('rating'), data.get('source_id')
                if rating not in ('helpful', 'needs_review') or source_id not in [f['id'] for f in faqs] + ['NO_MATCH']:
                    self.send(400, {'error': 'Choose a valid feedback option.'})
                    return
                record = {'time': datetime.now(timezone.utc).isoformat(), 'source_id': source_id, 'rating': rating}
                with (FOLDER / 'feedback.jsonl').open('a', encoding='utf-8') as file:
                    file.write(json.dumps(record) + '\n')
                self.send(200, {'message': 'Thank you! Feedback saved on this laptop.'})
            else:
                self.send(404, {'error': 'Page not found.'})
        except (OSError, ValueError, TypeError, AttributeError):
            self.send(500, {'error': 'Could not read the FAQs or save feedback. Check faqs.json and that this folder is writable.'})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error('Choose a port from 1 to 65535.')
    try:
        load_faqs()
        if not (FOLDER / 'index.html').is_file():
            raise ValueError('Keep index.html beside app.py.')
        server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    except (OSError, ValueError, TypeError, AttributeError) as error:
        print(f'Could not start: {error}')
        print('Keep all files together. If the port is busy, try --port 8001.')
        return 1
    print(f'\nClinic Information Assistant is ready!\nOpen http://127.0.0.1:{args.port} in your browser.\nKeep this terminal open. Press Ctrl+C here to stop.\n', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nWorkshop app stopped.')
    finally:
        server.server_close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
