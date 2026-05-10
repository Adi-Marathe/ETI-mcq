import re
import json

def clean_text(text):
    noise_patterns = [
        r"Mob No:.*?\|.*?\|.*",
        r"Insta:.*?\|.*?\|.*",
        r"V2V EdTech LLP \| (ETI|DFH) \(CO/IT\) \(31631[35]\) \| MCQs",
        r"V2V EdTech LLP \| (ETI|DFH) \(CO/IT\) \(31631[35]\) \| Notes"
    ]
    for pattern in noise_patterns:
        text = re.sub(pattern, "", text)
    # also replace multiple blank lines
    text = re.sub(r'\n\s*\n', '\n', text)
    return text

def parse_unit5(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    text = clean_text(text)
    questions = []
    
    text = '\n' + text.strip()
    parts = re.split(r'\n(\d+)\.\s*', text)
    
    for i in range(1, len(parts), 2):
        q_num_str = parts[i]
        q_content = parts[i+1]
        
        q_id = int(q_num_str)
        
        if 'Answer:' in q_content:
            q_text_options, ans_block = q_content.split('Answer:', 1)
        else:
            print(f"Warning: 'Answer:' not found in question {q_id}")
            continue
            
        answer_raw = ans_block.strip()
        
        options = []
        q_lines = q_text_options.strip().split('\n')
        
        question_text_lines = []
        opt_lines = []
        
        parsing_options = False
        for line in q_lines:
            line_str = line.strip()
            if re.match(r'^[a-d]\)', line_str):
                parsing_options = True
                opt_lines.append(line_str)
            elif parsing_options:
                opt_lines[-1] += " " + line_str
            else:
                question_text_lines.append(line_str)
                
        question = " ".join(question_text_lines).strip()
        answer = " ".join(answer_raw.split())
        
        if ')' in answer:
            ans_text = answer.split(')', 1)[-1].strip()
        else:
            ans_text = answer
        explanation = f"The correct answer is '{ans_text}'. This concept is essential to Digital Forensics and Ethical Hacking."
            
        questions.append({
            "id": q_id,
            "question": question,
            "options": opt_lines,
            "answer": answer,
            "explanation": explanation
        })

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=4)
        
    print(f"Parsed {len(questions)} questions and saved to {output_file}")

if __name__ == "__main__":
    parse_unit5("unit5_raw.txt", "src/data/unit5_questions.json")
