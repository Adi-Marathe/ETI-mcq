import json
import re

def clean_text(text):
    # Remove footers/headers
    text = re.sub(r'Click to Join our Channel\nThis is Free Study Material Provided by Campusifyplus.in', '', text)
    return text

def parse_ete_unit2(filepath):
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
        
        # Extract question text (until the first option A))
        q_text_match = re.search(r'^(.*?)(?=\s*[A-D]\))', q_body, re.DOTALL)
        if not q_text_match:
            continue
        question_text = q_text_match.group(1).strip().replace('\n', ' ')
        
        # Extract options
        options = []
        for opt_char in ['A', 'B', 'C', 'D']:
            pattern = fr'{opt_char}\)\s*(.*?)(?=\s*[A-D]\)|\s*Answer:|$)'
            opt_match = re.search(pattern, q_body, re.DOTALL)
            if opt_match:
                opt_text = opt_match.group(1).strip().replace('\n', ' ')
                options.append(f"{opt_char.lower()}) {opt_text}")
        
        # Extract answer
        ans_match = re.search(r'Answer:\s*([A-D])', q_body)
        answer = ""
        if ans_match:
            ans_char = ans_match.group(1).lower()
            for opt in options:
                if opt.startswith(f"{ans_char})"):
                    answer = opt
                    break
        
        # Placeholder explanation
        explanation = f"The correct answer is {answer.split(') ')[1]} as per the Unit 2 syllabus on Smart Grids."
        
        questions.append({
            "id": current_q_id,
            "question": question_text,
            "options": options,
            "answer": answer,
            "explanation": explanation
        })
        current_q_id += 1
        
    return questions

questions = parse_ete_unit2('ete_unit2_new.txt')
with open('../src/data/ete_unit2.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=4)

print(f"Successfully processed {len(questions)} questions for ETE Unit 2.")
