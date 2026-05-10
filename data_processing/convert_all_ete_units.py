import json
import re
import os

def clean_text(text):
    # Remove footers/headers like "Mob No : ...", "Youtube : ...", "V2V EdTech LLP", etc.
    text = re.sub(r'Mob No\s*:.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Youtube\s*:.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Insta\s*:.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'App Link\s*\|.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'V2V EdTech LLP.*?\n', '', text, flags=re.IGNORECASE)
    return text

def parse_unit_file(filepath, unit_id):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = clean_text(content)
    
    # Split by number followed by period at start of line
    parts = re.split(r'\n(\d+)\.', '\n' + content)
    
    questions = []
    current_q_id = 1
    
    for i in range(1, len(parts), 2):
        raw_id = parts[i]
        q_body = parts[i+1]
        
        # Extract question text (until the first option)
        q_text_match = re.search(r'^(.*?)(?=\n[a-dA-D]\))', q_body, re.DOTALL)
        if not q_text_match:
            continue
        question_text = q_text_match.group(1).strip().replace('\n', ' ')
        
        # Extract options
        options = []
        for opt_char in ['a', 'b', 'c', 'd']:
            opt_match = re.search(fr'\n{opt_char}\)\s*(.*?)(?=\n[a-dA-D]\)|\nAnswer:|$)', q_body, re.DOTALL | re.IGNORECASE)
            if opt_match:
                opt_text = opt_match.group(1).strip().replace('\n', ' ')
                options.append(f"{opt_char}) {opt_text}")
        
        # Extract answer
        ans_match = re.search(r'Answer:\s*([a-dA-D])', q_body, re.IGNORECASE)
        answer = ""
        if ans_match:
            ans_char = ans_match.group(1).lower()
            for opt in options:
                if opt.startswith(f"{ans_char})"):
                    answer = opt
                    break
        
        # Extract explanation if exists
        expl_match = re.search(r'Explanation:\s*(.*?)(?=\n\d+\.|$)', q_body, re.DOTALL | re.IGNORECASE)
        explanation = expl_match.group(1).strip().replace('\n', ' ') if expl_match else "The correct answer is supported by the technical definitions of the topic."
        
        questions.append({
            "id": current_q_id,
            "question": question_text,
            "options": options,
            "answer": answer,
            "explanation": explanation
        })
        current_q_id += 1
        
    return questions

# Process Units 2 to 5
for u_id in range(2, 6):
    raw_file = f"unit{u_id}_raw.txt"
    if os.path.exists(raw_file):
        print(f"Processing Unit {u_id}...")
        questions = parse_unit_file(raw_file, u_id)
        with open(f"../src/data/ete_unit{u_id}.json", 'w', encoding='utf-8') as f:
            json.dump(questions, f, indent=4)
        print(f"Successfully created ete_unit{u_id}.json with {len(questions)} questions.")

print("All ETE units processed.")
