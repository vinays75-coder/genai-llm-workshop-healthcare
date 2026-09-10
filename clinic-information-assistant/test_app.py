"""Regression checks: run python3 -m unittest discover -s clinic-information-assistant."""
import copy
import unittest
from app import find_answer, load_faqs


class AnswerMatchingTests(unittest.TestCase):
    def setUp(self):
        self.faqs = load_faqs()

    def test_missing_details_do_not_return_topic_only_matches(self):
        for question in [
            'How much do medical records cost?',
            'What is the fee for records?',
            'How long do records requests take?',
            'Do I need photo ID for medical records?',
            'How much does parking cost?',
            'What are the clinic hours on holidays?',
            'How do I reschedule my appointment and what does it cost?',
        ]:
            with self.subTest(question=question):
                result = find_answer(question, self.faqs)
                self.assertEqual(result['status'], 'unknown')
                self.assertEqual(result['sources'], [])

    def test_saved_questions_and_aliases_still_work(self):
        for faq in self.faqs:
            for question in [faq['question']] + faq['aliases']:
                with self.subTest(question=question):
                    result = find_answer('  ' + question.upper() + '!!!  ', self.faqs)
                    self.assertEqual(result['status'], 'found')
                    self.assertEqual(result['sources'], [faq])

    def test_explicit_cost_faq_can_answer_cost_question(self):
        faqs = copy.deepcopy(self.faqs)
        fee_faq = {'id': 'TEST-FEE', 'question': 'How much do medical records cost?',
                   'aliases': [], 'answer': 'Fictional test policy: no fee.'}
        faqs.append(fee_faq)
        result = find_answer(fee_faq['question'], faqs)
        self.assertEqual(result['sources'], [fee_faq])


if __name__ == '__main__':
    unittest.main()
