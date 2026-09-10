# Everyday AI for Health IT — presenter guide

Open `Everyday_AI_for_Health_IT_Workshop_Upgraded.pptx`. Speaker notes are embedded in every slide. In PowerPoint Normal view, open the Notes pane below the slide. Use Presenter View when projecting; confirm that the audience sees slides and you see notes.

## Timing

34 core slides, 70 minutes including eight minutes of questions. Three appendix slides are hidden from the normal slide show. The separate 15-minute app exercise is not included.

**60 minutes:** shorten slide 2 by one minute; shorten each of slides 13–15 and 29–31 by one minute; use five minutes for slide 34.

**75 minutes:** follow the core plan and allow thirteen minutes for slide 34.

## Critical review and changes made

- **Pacing:** the original 46 slides included seven divider slides and repeated explanations. The revised core has 34 slides, with a 70-minute schedule and explicit 60- and 75-minute options.
- **Navigation:** the original footer numbers repeated and did not match physical slide positions. The new deck uses consecutive slide numbers.
- **Readability:** replaced dense pages and small embedded diagrams with editable PowerPoint shapes, short text blocks, consistent spacing, and a high-contrast navy/teal palette.
- **Tokens:** removed the original diagram’s misleading suggestion that more tokens automatically mean better context and richer output. The new slide labels its token split as illustrative and emphasizes relevant information.
- **Activities:** added exact live prompts, audience questions, expected findings, transitions, and an offline fallback. The flawed records reply is explicitly a prepared example, not a claimed live model failure.
- **Retrieval:** the records-cost question now explicitly demonstrates missing support. A records-routing policy does not answer a fee question. The optional app notes match the fixed application.
- **Scope:** replaced brand-specific feature claims with durable application categories. Kept the healthcare and health-IT examples accessible to students and nurses.
- **Equity:** retained one sourced healthcare algorithm example and labeled it as not an LLM study. Removed the pulse-oximetry detour to avoid confusing device measurement with generative AI.
- **Governance:** separated U.S./California and European signposts; placed qualifications and primary-source links in notes and hidden reference slides.
- **Delivery:** all 37 slides have simple-language notes. The separate app exercise is a hidden optional appendix, outside the core timing.

The source PPT in Downloads was left unchanged. Structural and text-fit checks passed, and generated layout previews were visually reviewed. Native PowerPoint PDF export failed in this environment, so a successful native slide-show render has not been verified. Please open the deck and check Presenter View on your projector before the workshop.

## Before presenting

- Open the PPT and test Presenter View with the projector. Use extended displays if you want private notes.
- Have ChatGPT or your approved tool signed in before the session. Use fresh chats for the prompt comparison.
- Copy live prompts from the slide notes below. Use only the supplied fictional material.
- If the network fails, use the prepared prompts and answer key already on slides 13–15 and 29–31.
- Keep questions about real patients out of the demonstration.

## Slide-by-slide speaking script

### 1. Everyday AI for Health IT

SLIDE 1: Everyday AI for Health IT
TIMING: 00:00–01:00 | 1 minutes

SAY
Welcome. Today is about using AI thoughtfully, not becoming an AI engineer. These ideas apply to students, nurses, support teams, and health-IT staff. We will learn a few words, try clearer instructions, and practice checking an answer. You do not need to code during this presentation.

DO
Introduce yourself. Ask for a quick show of hands: who has tried a chatbot? The core plan is 70 minutes including questions. The optional app exercise is separate.

TRANSITION
Let me show you the route.

### 2. Our route: understand, practice, review

SLIDE 2: Our route: understand, practice, review
TIMING: 01:00–03:00 | 2 minutes

SAY
We will spend about thirty minutes on the basic ideas and clearer prompts. Then we will look at sources, tools, cost, and governance. We will finish with a live review exercise. The aim is to leave with one task you can do better and one check you will always perform.

DO
Use the full 70-minute plan. For 60 minutes, shorten this introduction by one minute, reduce slides 13–15 and 29–31 by one minute each, and reduce final questions from eight to five minutes. For 75 minutes, add five minutes of final discussion.

TRANSITION
First, one ground rule.

### 3. Use fictional information today

SLIDE 3: Use fictional information today
TIMING: 03:00–04:00 | 1 minutes

SAY
Please do not paste real patient information into this workshop. That includes screenshots, recordings, and notes. Removing a name alone may not remove identifying information. At work, check the exact product, account, and process your organization has approved.

DO
Use only the prepared fictional prompts in the presenter guide. Explain PHI as identifiable health information protected under HIPAA; the applicable rules depend on the setting.

SOURCES (checked 9 September 2026)
HHS: https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html

### 4. You can drive without building the engine

SLIDE 4: You can drive without building the engine
TIMING: 04:00–06:00 | 2 minutes

SAY
An LLM is software that works with language. Think of it as the engine. The application is the dashboard. Your prompt gives directions. You are the driver who checks the result. The car analogy explains the roles; it does not promise that AI is reliable. An LLM can produce fluent text that is wrong.

DO
Point to each box in order. Avoid discussing model mathematics.

ASK / EXPECT
Which part do you control? Your task, the information you supply, and your review.

TRANSITION
Who builds these engines, and who uses them?

### 5. Two roles in the GenAI landscape

SLIDE 5: Two roles in the GenAI landscape
TIMING: 06:00–08:00 | 2 minutes

SAY
Some organizations create models. Examples include OpenAI, Anthropic, Meta, Google, and xAI. Others use models to study, write, summarize, or build applications. The same organization can do both. Today we learn just enough about the engine to use the tools with better judgment.

TRANSITION
The chatbot is only one doorway into that engine.

### 6. LLMs are useful beyond a chat window

SLIDE 6: LLMs are useful beyond a chat window
TIMING: 08:00–09:30 | 1.5 minutes

SAY
A model can sit inside many applications. A chat app lets you ask and revise. A copilot helps inside a document or email tool. A healthcare system may offer a draft feature. A workflow may call a model when a task arrives. These are categories, not endorsements or claims that every product supports every feature.

ASK / EXPECT
Where have you already seen an AI button at school or work?

TRANSITION
Start with a useful task you can check.

### 7. Start with something you can review well

SLIDE 7: Start with something you can review well
TIMING: 09:30–11:00 | 1.5 minutes

SAY
Good first tasks are small and easy for you to check. A student can create practice questions from a reading. A nurse can draft a generic reminder from approved instructions. A support analyst can turn a permitted knowledge article into a checklist. These are drafts. The person checks the source and the final wording.

ASK / EXPECT
Which of these would save you a little time this week? Take two short answers.

### 8. Tokens are the small pieces of text

SLIDE 8: Tokens are the small pieces of text
TIMING: 11:00–13:00 | 2 minutes

SAY
Text is split into small pieces called tokens. A piece may be a word, part of a word, or punctuation. Think of LEGO pieces making a message. The blocks shown here are just an illustration, not the exact output of a tokenizer. Tokens matter because there are space limits and some services charge by usage. More tokens do not automatically mean a better answer.

DO
Point to the blocks. Explain the context window as available desk space: instructions and supplied material take room, and the response needs an allowance too.

TRANSITION
Next: how can different words point toward similar meanings?

### 9. Embeddings are a map of meaning

SLIDE 9: Embeddings are a map of meaning
TIMING: 13:00–15:00 | 2 minutes

SAY
An embedding represents text with numbers so software can compare meanings. Imagine a library map. Book a visit and schedule an appointment belong near each other. A billing question belongs elsewhere. This can help a search system find relevant text even when the wording differs. Similarity does not prove correctness, and this drawing is only an analogy.

DO
Ask participants to suggest a second way to say book an appointment. Do not introduce vectors or distance formulas.

TRANSITION
The next term describes settings inside the model.

### 10. Parameters are learned internal settings

SLIDE 10: Parameters are learned internal settings
TIMING: 15:00–16:00 | 1 minutes

SAY
Think of the internal settings in a radio. You can use it without adjusting every component. Parameters are learned numbers inside the model. They influence how it processes information. Your prompt usually does not change those numbers. A larger parameter count alone does not tell you whether a model is suitable.

DO
Keep this brief. No mathematics or model-size comparisons are needed.

### 11. Attention helps use the surrounding words

SLIDE 11: Attention helps use the surrounding words
TIMING: 16:00–18:00 | 2 minutes

SAY
Imagine a clinician reading a file for one question. Some details matter more than others. Attention is a model mechanism that gives different influence to parts of the context. That is an analogy, not a claim that the model thinks like a clinician. Look at discharge: the surrounding words change what the word means.

DO
Read both sentences slowly. Ask what discharge means in each.

ASK / EXPECT
First: leaving the hospital. Second: fluid from a wound. Context changes the meaning.

### 12. A clear prompt has five ingredients

SLIDE 12: A clear prompt has five ingredients
TIMING: 18:00–20:00 | 2 minutes

SAY
A prompt is a short brief. Say what you want done, what information may be used, who will read the result, how it should look, and what must not be added. You do not need a magic phrase. You need a clear request that fits the task.

DO
Read the five labels, then connect them to the next patient-reminder activity.

TRANSITION
We will keep the facts the same and change the clarity of our instructions.

### 13. Try a loose prompt first

SLIDE 13: Try a loose prompt first
TIMING: 20:00–23:00 | 3 minutes

SAY
This is a fictional exercise. We will ask for a reminder, then review the answer. The first prompt gives facts but leaves several choices open. It might produce a good answer. We are not trying to force an error or prove that vague prompts always fail.

DO
Open a fresh ChatGPT conversation in the approved tool. Paste the prompt below from the presenter guide. Read the response and save it for comparison. Allow about a minute for reactions. If internet access fails, discuss what the prompt specifies and what it leaves open.

COPY THIS PROMPT
Write a patient reminder based on these clinic instructions: arrive 15 minutes before your appointment, bring your medication list, and call the clinic if you need to reschedule.

ASK / EXPECT
What is missing? A clear reading level, a short format, and an explicit limit on adding facts.

### 14. Now make the boundaries explicit

SLIDE 14: Now make the boundaries explicit
TIMING: 23:00–26:00 | 3 minutes

SAY
We are using the same facts. This time we clearly name the audience, the format, and the limits. The extra wording tells the model what to preserve and what not to add. We still need to check the result.

DO
Use a fresh conversation in the same tool and model. Paste the prompt below. Compare the response with the first answer. Do not spend time changing model settings.

COPY THIS PROMPT
Rewrite these fictional clinic instructions in plain language for a patient.

Facts: Arrive 15 minutes before your appointment. Bring your medication list. Call the clinic if you need to reschedule.

Format: Three short bullet points.
Limits: Preserve all three facts. Do not add medical advice, preparation steps, dates, phone numbers, or other requirements.

ASK / EXPECT
Which instructions are clearer now? If both answers are good, point to the explicit controls rather than claiming an error occurred.

### 15. Check the answer, not just the prompt

SLIDE 15: Check the answer, not just the prompt
TIMING: 26:00–29:00 | 3 minutes

SAY
Let us compare the two answers against the three supplied facts. Did either add a requirement or leave something out? Was the language clear for the patient? If both answers were good, that is fine. One successful answer does not tell us how reliably the tool behaves across different tasks.

DO
Take two observations from the room. Use the four checks on the slide. For a 60-minute session, take one observation and move on.

ASK / EXPECT
Could a patient act on an invented instruction? Yes. That is why source checking matters before the message is used.

TRANSITION
Now let us give an assistant a source to consult.

### 16. RAG: let the assistant open the manual

SLIDE 16: RAG: let the assistant open the manual
TIMING: 29:00–31:00 | 2 minutes

SAY
RAG stands for retrieval-augmented generation. In plain language: find useful source material, give it to the model, and ask for a draft based on that source. Think of a new colleague opening the handbook before replying. The retrieved passage might be wrong, old, or incomplete, so the answer still needs review.

DO
Follow the three steps from left to right. Explain that retrieval and generation are different steps.

TRANSITION
Let us try the same source with two different questions.

### 17. The right topic is not always the answer

SLIDE 17: The right topic is not always the answer
TIMING: 31:00–33:00 | 2 minutes

SAY
The fictional source tells us which team handles records requests. It does not tell us what a request costs. These questions share the word records, but they ask for different information. A source about the topic is not automatically support for every claim about that topic.

DO
Read the source once, then ask which question it answers. This is also the behavior we fixed in the local workshop application.

ASK / EXPECT
Can we infer a fee from this policy? No. We need another approved source.

### 18. An agent can take permitted steps

SLIDE 18: An agent can take permitted steps
TIMING: 33:00–35:00 | 2 minutes

SAY
An agent can use a model to choose steps and call tools. For example, it can search the policy library and prepare a reply. In our workflow it stops for a person to review before anything is sent. This review is a design requirement in our example, not something every agent automatically does.

DO
Explain that permission to search is different from permission to send or change a record.

ASK / EXPECT
What could go wrong if a draft was sent automatically?

TRANSITION
How might the application connect to those tools?

### 19. MCP is a standard tool connection

SLIDE 19: MCP is a standard tool connection
TIMING: 35:00–36:30 | 1.5 minutes

SAY
MCP means Model Context Protocol. It is a standard way for an AI application to connect to tools and information. Think of a common connector. It can help different parts work together. It does not itself make the tool trustworthy or decide that a person should have access. Tools can also connect without MCP.

DO
Keep this at the connector analogy. No protocol details or installation steps are needed.

SOURCES (checked 9 September 2026)
MCP: https://modelcontextprotocol.io/docs/getting-started/intro

### 20. The same pattern works at a service desk

SLIDE 20: The same pattern works at a service desk
TIMING: 36:30–38:00 | 1.5 minutes

SAY
IT service management means organizing support requests. Imagine a ticket about access to a training system. An assistant can suggest a category, find an approved support article, and prepare a response. The support analyst checks the article and the proposed action. Logs can record what happened; they do not reveal all of a model’s internal reasoning.

DO
Use a fictional administrative ticket. Do not demonstrate password resets or access changes.

TRANSITION
Useful systems also need sensible cost and governance decisions.

### 21. Reduce waste without removing needed context

SLIDE 21: Reduce waste without removing needed context
TIMING: 38:00–40:00 | 2 minutes

SAY
Many developer services charge for input and output, often at different rates. A subscription app may have a fixed price, so a shorter prompt does not always reduce your bill. In this example, ten thousand input tokens become one thousand at the same input rate. That is ninety percent less for the input portion only. Output and other charges may differ.

DO
Point out that the figures are fictional usage amounts, not a vendor price list. Give three habits: relevant excerpt, clear reusable prompt, and appropriately short response.

### 22. Governance means someone owns the decisions

SLIDE 22: Governance means someone owns the decisions
TIMING: 40:00–42:00 | 2 minutes

SAY
Governance is how an organization decides what is allowed, who is responsible, and what happens when something goes wrong. Think of introducing new equipment: buying it is only the start. Someone must define its use, test it in the real setting, support the staff, and monitor problems. NIST offers a voluntary risk-management framework; it is not a law or a certification.

DO
Ask participants who they would contact if they were unsure whether an AI tool was approved.

SOURCES (checked 9 September 2026)
NIST: https://www.nist.gov/itl/ai-risk-management-framework

### 23. U.S. and California: three legal signposts

SLIDE 23: U.S. and California: three legal signposts
TIMING: 42:00–44:00 | 2 minutes

SAY
These are signposts, not a complete legal checklist. HIPAA can require a business associate agreement for a cloud provider handling electronic protected health information on behalf of a covered entity or business associate, along with other safeguards. FDA oversight depends on the software’s intended function. California AB 3030 addresses certain AI-generated communications about patient clinical information in specified healthcare settings. It includes disclosure and human-contact requirements and an exception when a licensed or certified healthcare provider reads and revises the communication. Administrative scheduling and billing are excluded from that law’s definition of patient clinical information. Ask the local compliance team how the rules apply.

SOURCES (checked 9 September 2026)
HHS: https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html
FDA: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software
California AB 3030: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB3030

### 24. Europe: privacy and intended use matter

SLIDE 24: Europe: privacy and intended use matter
TIMING: 44:00–45:00 | 1 minutes

SAY
GDPR requires a legal basis for processing personal data, and health data needs an applicable special-category condition. Consent is not the only possible basis. The EU AI Act uses a risk-based approach. Obligations depend on the system, intended use, and organizational role. Not every healthcare chatbot is high-risk. We are not memorizing dates today; check current guidance for actual deployment.

SOURCES (checked 9 September 2026)
GDPR: https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data_en
EU AI Act: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

### 25. Check whether the tool works fairly

SLIDE 25: Check whether the tool works fairly
TIMING: 45:00–47:00 | 2 minutes

SAY
A tool can perform differently for different groups. One published study of a healthcare risk algorithm found that using healthcare cost as a proxy for health need created racial bias. This was not an LLM study. It is a lesson about choosing what a system measures and checking whom it serves. For everyday AI drafts, watch for assumptions about language, ability, internet access, or family support.

DO
Use one research example rather than two. The original pulse-oximetry example concerns device measurement, not generative AI, so it is not used here.

ASK / EXPECT
If a draft says use the portal, what does it assume? That the person has access and can use it.

SOURCES (checked 9 September 2026)
Bias study: https://pubmed.ncbi.nlm.nih.gov/31649194/

### 26. Before, during, and after every AI task

SLIDE 26: Before, during, and after every AI task
TIMING: 47:00–49:00 | 2 minutes

SAY
Before a task, check the tool and the information you are allowed to use. During the task, keep the request clear and ask what is missing. Afterward, verify facts and omissions against the source. If there is a problem, follow the local reporting process. Urgent clinical situations use established clinical escalation, not a chatbot conversation.

DO
Keep the distinction clear: asking AI to check itself may help, but comparing with an authoritative source is a separate step.

### 27. A document can contain unsafe instructions

SLIDE 27: A document can contain unsafe instructions
TIMING: 49:00–50:00 | 1 minutes

SAY
A retrieved page or message may contain text telling the assistant to ignore its rules or send information elsewhere. That is untrusted content and can be a prompt-injection attempt. Users should stop and report unexpected behavior. Organizations need access limits and technical protections; a good prompt alone is not enough.

DO
Read the example as a warning, not an instruction. Do not perform it in a live tool.

### 28. Five checks before you use the answer

SLIDE 28: Five checks before you use the answer
TIMING: 50:00–51:00 | 1 minutes

SAY
Here is a short final check. Was the use allowed? Are important statements supported? Is the answer complete enough? Is it appropriate for this audience? Has the right person reviewed it? If one check fails, pause and verify or escalate.

TRANSITION
Now we will practice those checks together on one prepared draft.

### 29. Live review: would you send this reply?

SLIDE 29: Live review: would you send this reply?
TIMING: 51:00–54:00 | 3 minutes

SAY
A patient asks about requesting records. We have one sentence from the fictional clinic policy and a draft reply. Your job is to review the draft before it is sent. The draft is deliberately flawed. We are not claiming that ChatGPT just produced it or will always make these mistakes.

DO
Open a fresh ChatGPT conversation and paste the setup prompt below. Pause before asking for an evaluation. If the internet fails, everything needed is visible on this slide. Give the room one minute to find unsupported details.

COPY THIS SETUP
We are doing a fictional healthcare classroom exercise.

Our entire available clinic policy says:
"Records requests go to the Health Information Management team."

A colleague prepared this patient reply:
"Send your request to the Health Information Management team. Bring photo ID and a $20 processing fee. Your records will be ready tomorrow."

Show the policy and the proposed reply separately. Do not evaluate the reply yet. Wait for my next instruction.

ASK / EXPECT
Which claims can you confirm using the policy alone? Let participants answer before advancing.

### 30. Only one statement is supported

SLIDE 30: Only one statement is supported
TIMING: 54:00–57:00 | 3 minutes

SAY
The source supports the destination team. It does not establish an identification requirement, a fee, or a turnaround time. Those details could be true somewhere, but we cannot claim them for this clinic from this source. Unsupported is the key word. Now we can ask ChatGPT to help audit the draft, and check its table ourselves.

DO
Paste the audit prompt below in the same conversation. Compare the result with this prepared answer key. If ChatGPT classifies a claim incorrectly, use the source to correct it.

COPY THIS PROMPT
Now review the proposed reply using ONLY the supplied policy. Make a table with: statement, supported or not supported, and the exact supporting policy wording or "Not provided". Do not use general knowledge or assume another clinic’s rules apply.

ASK / EXPECT
Why is “ready tomorrow” a problem? Someone may make plans based on an unconfirmed promise.

### 31. Rewrite without guessing

SLIDE 31: Rewrite without guessing
TIMING: 57:00–60:00 | 3 minutes

SAY
An appropriate rewrite keeps the supported destination and identifies what the source does not tell us. It does not invent an answer to make the message feel complete. This is the difference between a useful draft and a misleading promise. Good prompting and checking are complementary skills.

DO
Paste the rewrite prompt below. Compare the answer with the example on the slide. Then ask what would need confirmation before using it at work.

COPY THIS PROMPT
Rewrite the patient reply in plain language. Use only facts supported by the supplied policy. Briefly identify details that need confirmation. Do not invent requirements, fees, contact details, or timing. Keep the reply under 60 words.

ASK / EXPECT
What is still missing? Identification requirements, fees, and timing. Find an approved source rather than guessing.

TRANSITION
These skills are useful across healthcare roles.

### 32. Bring one useful skill back to your role

SLIDE 32: Bring one useful skill back to your role
TIMING: 60:00–61:00 | 1 minutes

SAY
You do not need a new job title to use these ideas. Students can check study aids. Nurses and healthcare staff can review drafts against approved instructions. Support teams can improve knowledge articles. Analysts can evaluate search and summarization. Privacy and project teams can ask about approved use, testing, and accountability.

DO
Invite participants to choose one low-risk task they can review well. These are examples of relevant skills, not guarantees about jobs or credentials.

### 33. Remember the workflow, not every acronym

SLIDE 33: Remember the workflow, not every acronym
TIMING: 61:00–62:00 | 1 minutes

SAY
You do not need to remember every technical term tonight. Remember the workflow. Choose an approved tool. Give clear instructions and permitted context. Use an appropriate source. Check the result. Keep the responsible person in control. Tokens, embeddings, parameters, and attention help explain parts of the engine; they do not remove the need for judgment.

TRANSITION
What would help you apply this in your own setting?

### 34. Questions and one action to take away

SLIDE 34: Questions and one action to take away
TIMING: 62:00–70:00 | 8 minutes

SAY
What is one task where this could help you? What source would you check? What information must stay out? We can discuss examples without sharing real patient information. If a question is about a specific tool’s approval or a clinical decision, the answer belongs with the appropriate local team.

DO
Use eight minutes in the 70-minute plan, five minutes in the 60-minute plan, or thirteen minutes in the 75-minute plan. Optional hidden reference slides follow. The separate app build takes another 15 minutes and is not included in this timing.

ASK / EXPECT
Ask participants to finish: “I will try ___, and I will check it by ___.”

### 35. Reference shelf: privacy and law

SLIDE 35: Reference shelf: privacy and law
TIMING: OPTIONAL / NOT IN CORE TIMING

SAY
This is a reference slide, not a slide to read aloud. Links are clickable. Requirements depend on the real organization and intended use. Dates and rules should be checked again before deployment.

SOURCES (checked 9 September 2026)
HHS: https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html
FDA: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software
California AB 3030: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB3030
GDPR: https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data_en
EU AI Act: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

### 36. Reference shelf: systems, risk, and fairness

SLIDE 36: Reference shelf: systems, risk, and fairness
TIMING: OPTIONAL / NOT IN CORE TIMING

SAY
These links support the discussion of MCP, voluntary AI risk management, and the published bias example. The bias study concerns a healthcare prediction algorithm, not an LLM.

SOURCES (checked 9 September 2026)
MCP: https://modelcontextprotocol.io/docs/getting-started/intro
NIST: https://www.nist.gov/itl/ai-risk-management-framework
Bias study: https://pubmed.ncbi.nlm.nih.gov/31649194/

### 37. Optional: build the Clinic Information Assistant

SLIDE 37: Optional: build the Clinic Information Assistant
TIMING: OPTIONAL / NOT IN CORE TIMING

SAY
This optional activity is separate from the 60–75 minute presentation. The application uses a browser page, a Python backend, and a local FAQ file. It does not use an LLM and does not generate new text. It is a simulation of the application workflow. Participants must have Python installed before the session.

DO
Use clinic-information-assistant/README.md in the workshop repository. Start with python3 app.py on Mac or py -3 app.py on Windows, then open http://127.0.0.1:8000. Test the records destination, then the records cost question. The current version returns Information not found for the cost question; do not demonstrate the old keyword fallback. Change the fictional closing time in faqs.json, save, and ask again. Stop with Ctrl+C.
