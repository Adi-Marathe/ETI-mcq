import json
import os

filepath = 'src/data/questions.json'

with open(filepath, 'r') as f:
    questions = json.load(f)

for q in questions:
    if not q.get('explanation'):
        ans_text = q['answer'].split(')', 1)[-1].strip()
        if ans_text.lower() in ["true", "false"]:
            q['explanation'] = f"The statement is {ans_text.lower()}."
        else:
            q['explanation'] = f"The correct concept here is '{ans_text}'. This is a foundational principle of the topic being tested."

with open(filepath, 'w') as f:
    json.dump(questions, f, indent=4)
print("Added generic explanations to all questions.")
