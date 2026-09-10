# Clinic Information Assistant — 15-minute hands-on

A complete local web application for a nontechnical healthcare workshop.

**No LLM, API key, account, pip install, cloud service, or internet connection is needed to run it.** Python 3 must already be installed. This is an explicitly labeled **model-free simulation of a GenAI workflow**, not a generative AI model or a clinical system. All clinic policies are fictional.

## Before the workshop — instructor preparation

1. Distribute `clinic-information-assistant.zip` to participants before the session.
2. Ask them to **extract/unzip it** into a folder they can edit, such as Documents. On Windows, use **Extract All**; do not run inside the ZIP preview.
3. Confirm Python 3 is installed. In a terminal, run `python3 --version` on Mac or `py -3 --version` on Windows. Python 3.9 or newer can run this code; use a currently supported Python release for a new installation.
4. If Python is missing, install it ahead of time from [python.org/downloads](https://www.python.org/downloads/). Reopen the terminal after installation. Follow your institution's installation rules on managed laptops.
5. Test the launch steps below on the actual participant laptops. Pair participants if installation is blocked. Budget the 15 minutes for the activity, not for installing Python or VS Code.

VS Code is optional. There is no need to install any VS Code extension, create a virtual environment, or select a notebook kernel.

## Start the app — choose one method

### Method A: VS Code, Mac or Windows

1. Open VS Code.
2. Choose **File → Open Folder** and open the extracted `clinic-information-assistant` folder. You should see `app.py`, `index.html`, and `faqs.json` together.
3. Choose **Terminal → New Terminal** from the menu. The terminal should open in this folder.
4. Enter the command for your computer:

**Mac:**

```sh
python3 app.py
```

**Windows:**

```powershell
py -3 app.py
```

If Windows has Python available as `python` instead, use:

```powershell
python app.py
```

5. Wait for this message:

```text
Clinic Information Assistant is ready!
Open http://127.0.0.1:8000 in your browser.
Keep this terminal open. Press Ctrl+C here to stop.
```

6. Open Chrome, Edge, Safari, or Firefox. Paste **http://127.0.0.1:8000** into the address bar and press Enter. Use `http`, not `https`.
7. Keep the terminal open throughout the activity. You do not need to run the notebook.

### Method B: Mac without VS Code

1. In Finder, locate the extracted folder and its `app.py` file.
2. Press **Command + Space**, type **Terminal**, and press Enter.
3. Type `python3` followed by a space. **Do not press Enter yet.**
4. Drag `app.py` from Finder into the Terminal window. This inserts the full file path.
5. Press Enter. Open **http://127.0.0.1:8000** in your browser.

The app locates its companion files automatically, regardless of the terminal's current directory.

### Method C: Windows without VS Code

1. Extract the ZIP using **Extract All**.
2. Open the extracted folder containing `app.py`.
3. Double-click **START_WINDOWS.bat**. Keep the command window open.
4. Open **http://127.0.0.1:8000** in your browser.

If institution policy prevents running `.bat` files, use Method A or ask your instructor; do not bypass institutional restrictions.

## The 15-minute activity

### Minutes 0–3: Launch

Start the app and open the browser page.

Say: “You are running a full-stack application on your own laptop. The page is the frontend, Python is the backend, and a local file supplies the information.”

### Minutes 3–5: Find an answer and inspect the source

Click the suggested question:

```text
Where do I request my medical records?
```

Expected result:

```text
Records requests go to the Health Information Management team.
Source: RECORDS-01 · Fictional clinic FAQ
```

Expand **Explore the fictional source library**. Find RECORDS-01 and compare the displayed answer with its source.

Ask: “Where did this answer come from?”

### Minutes 5–7: Ask something the app cannot answer

Click:

```text
How much does parking cost?
```

Expected result: **Information not found.** There is no parking information in the supplied FAQs.

Say: “The app has no parking source. It does not make up a fee.”

### Minutes 7–9: A related source is not necessarily an answer

Click:

```text
How much do medical records cost?
```

Expected result: **Information not found.** The records-routing FAQ does not explain fees, so it is not displayed as an answer.

Ask: “Does knowing which team handles requests tell us how much a request costs?”

Say: “Finding a document about the right topic does not mean that document answers the question. Read what it actually supports.”

This connects directly to Section 12 of the workshop notebook.

### Minutes 9–12: Make a small change yourself

1. In VS Code, click **faqs.json**.
2. Find the sentence containing `9 AM to 5 PM`.
3. Change **only** `5 PM` to `6 PM`.
4. Save with **Command + S** on Mac or **Ctrl + S** on Windows.
5. Return to the browser and click **What are the clinic hours?**
6. The answer should now say **9 AM to 6 PM**. No server restart is needed.

This changes a **fictional classroom policy**, not a real clinic's hours.

Without VS Code, use a plain-text editor and preserve the `.json` extension, straight quotation marks, and punctuation. An instructor can demonstrate this step if participants do not have an editor ready.

Say: “You changed the data your application uses, and the visible result changed.”

### Minutes 12–14: Save feedback

1. Click **Helpful** or **Needs review** beneath a result.
2. Find the newly created **feedback.jsonl** file in the app folder.
3. Open it in your editor. Each line records the time, a source ID, and your rating.

The app does not save the question text. Do not enter real patient information even though the demo runs locally.

Say: “Your button click went from the browser to Python and was saved in a local file.”

### Minutes 14–15: Recap and stop

Ask participants to name the three parts:

- **Frontend:** `index.html` — the page they interacted with.
- **Backend:** `app.py` — receives requests, searches, and saves feedback.
- **Storage:** `faqs.json` and the generated `feedback.jsonl`.

Return to the terminal and press **Ctrl + C** to stop the application. On Mac this is Control, not Command.

## What is actually happening?

```text
Browser: participant enters a question
                ↓
Python: compares it with prepared questions and alternative phrasings
                ↓
Local FAQ file: supplies the exact source wording
                ↓
Browser: displays a matching answer or reports missing information
```

A known question or alias (a saved alternative phrasing), ignoring case and punctuation, receives its saved answer. Other questions receive **Information not found**, with no unrelated FAQ displayed. Sharing a word such as “records” is not enough to establish that a policy answers a question about cost. This intentionally conservative matching can miss valid paraphrases; it does not understand language. To support another wording, add it to the appropriate FAQ’s `aliases` list only if that FAQ actually answers it.

There is no text generation, semantic embedding, or real RAG model here. An LLM-based version could draft from retrieved passages, but would still need source checks and appropriate safeguards. This workshop teaches the application structure and review workflow without model setup.

## Files you receive

| File | Purpose |
|---|---|
| `app.py` | Python backend and local server; uses only built-in libraries. |
| `index.html` | Browser interface, styling, and button behavior; all included locally. |
| `faqs.json` | Four fictional FAQ entries participants can edit. |
| `START_WINDOWS.bat` | Optional Windows launcher. |
| `README.md` | These instructions and the teaching script. |
| `.gitignore` | Excludes generated feedback and Python cache from Git. |
| `test_app.py` | Optional regression tests for matching; not needed to run the app. |

`feedback.jsonl` is created after the first feedback click. It is not included in the distributed ZIP.

## Troubleshooting

| What you see | What to do |
|---|---|
| `python3`, `py`, or `python` not found | Python is missing or unavailable in the terminal. Complete installation before the workshop, reopen the terminal, or pair with a prepared participant. |
| `can't open file app.py` | The terminal is in the wrong folder. Reopen the extracted app folder in VS Code and create a new terminal, or use the Mac drag-and-drop method. |
| The browser cannot connect | Keep the Python terminal running; copy the exact `http://127.0.0.1:8000` address. |
| Address already in use / port is busy | Use `python3 app.py --port 8001` on Mac or `py -3 app.py --port 8001` on Windows; open `http://127.0.0.1:8001`. |
| JSON error after editing | Undo the edit and save. Change only the time inside the existing quoted answer; leave commas, brackets, and quotes intact. |
| The hours did not change | Save the correct `faqs.json` file, then ask again. Keep the file beside the running `app.py`. |
| Feedback cannot be saved | Extract to a writable folder, such as Documents, instead of running inside the ZIP or a read-only folder. |
| Double-clicking `index.html` shows a page but buttons fail | Start Python first and open the `http://127.0.0.1:8000` address. Do not open the HTML file directly. |

This application binds only to the laptop's loopback address. It is a classroom demonstration, not a production deployment or a system for real patient records.
