import json

filepath = 'src/data/questions.json'

with open(filepath, 'r') as f:
    questions = json.load(f)

real_explanations = {
    1: "AI's primary goal is to create systems capable of performing tasks that typically require human intelligence, such as visual perception, speech recognition, and decision-making.",
    2: "John McCarthy is considered one of the 'founding fathers' of AI. He coined the term 'Artificial Intelligence' in 1955 for the Dartmouth Conference.",
    3: "AI is an interdisciplinary field that draws upon computer science, mathematics, psychology, linguistics, philosophy, and neuroscience to build intelligent systems.",
    4: "Mathematics provides the theoretical foundation for AI, especially through probability, statistics (for machine learning), calculus, and linear algebra.",
    5: "NLP stands for Natural Language Processing, which is a branch of AI that helps computers understand, interpret, and manipulate human language."
}

for q in questions:
    if q['id'] in real_explanations:
        q['explanation'] = real_explanations[q['id']]

with open(filepath, 'w') as f:
    json.dump(questions, f, indent=4)
print("Added real explanations to the first 5 questions.")
