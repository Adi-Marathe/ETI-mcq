import re
import json

def parse_unit2(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    questions = []
    
    # Split text by question numbers
    # We look for \n followed by 1 to 3 digits followed by a dot
    # Example: "\n1. " or "\n151."
    
    # Pre-process text to make splitting easier
    text = '\n' + text.strip()
    
    parts = re.split(r'\n(\d+)\.\s*', text)
    
    # parts[0] is the preamble (like "UNIT 2- Internet of Things")
    # parts[1] is '1', parts[2] is the content of question 1, and so on.
    
    for i in range(1, len(parts), 2):
        q_num_str = parts[i]
        q_content = parts[i+1]
        
        q_id = int(q_num_str)
        
        # Now extract the question text, options, answer, and explanation.
        # We know "Answer:" is the marker for the answer.
        # Sometimes there's an "Explanation:" marker.
        
        if 'Answer:' in q_content:
            q_text_options, ans_block = q_content.split('Answer:', 1)
        else:
            print(f"Warning: 'Answer:' not found in question {q_id}")
            continue
            
        explanation = ""
        if 'Explanation:' in ans_block:
            ans_part, exp_part = ans_block.split('Explanation:', 1)
            explanation = exp_part.strip()
        else:
            ans_part = ans_block
            
        answer_raw = ans_part.strip()
        
        # For the options, they are usually marked by a), b), c), d)
        # Let's extract them
        options = []
        q_lines = q_text_options.strip().split('\n')
        
        # The first line (or lines) until an option 'a)' appears is the question
        question_text_lines = []
        opt_lines = []
        
        parsing_options = False
        for line in q_lines:
            line_str = line.strip()
            # If line starts with a letter followed by ')', it's an option.
            if re.match(r'^[a-d]\)', line_str):
                parsing_options = True
                opt_lines.append(line_str)
            elif parsing_options:
                # Might be a continuation of an option, but usually each option is 1 line.
                opt_lines[-1] += " " + line_str
            else:
                question_text_lines.append(line_str)
                
        question = " ".join(question_text_lines).strip()
        
        # Format answer_raw: remove any random newline chars
        answer = " ".join(answer_raw.split())
        
        # If explanation is empty, provide a generic one like I did for unit 1
        if not explanation:
            ans_text = answer.split(')', 1)[-1].strip()
            explanation = f"The correct answer is '{ans_text}'. This concept is essential to the topic of Internet of Things."
            
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
    parse_unit2("unit2_raw.txt", "src/data/unit2_questions.json")
