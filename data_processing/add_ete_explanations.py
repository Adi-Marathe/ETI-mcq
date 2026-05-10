import json

# Load the questions
with open('../src/data/ete_unit1.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Define some explanation templates based on keywords
explanations = {
    "Industry 1.0": "Industry 1.0 (late 18th century) was characterized by mechanization through steam and water power, shifting production from manual labor to machine-assisted processes.",
    "Industry 2.0": "Industry 2.0 (late 19th/early 20th century) introduced mass production using electrical energy and assembly lines, pioneered by figures like Henry Ford.",
    "Industry 3.0": "Industry 3.0 (started in the 1970s) was driven by the rise of electronics, computers, and IT systems to automate production (PLC being a key invention).",
    "Industry 4.0": "Industry 4.0 (the current phase) focuses on digitalization, interconnectivity, and 'Smart Factories' using Cyber-Physical Systems, IoT, and Cloud Computing.",
    "Industry 5.0": "Industry 5.0 shifts focus back to human-centricity, sustainability, and resilience, emphasizing collaboration between humans and robots (cobots).",
    "Cyber-Physical System": "CPS integrates physical components (machines) with digital algorithms and networks, allowing real-time monitoring and decentralized decision-making.",
    "IoT": "The Internet of Things (IoT) allows devices and machines to communicate and exchange data over the internet, providing the connectivity layer for Industry 4.0.",
    "Cloud Computing": "Cloud Computing provides on-demand access to shared computing resources and storage, enabling scalable data processing without local infrastructure.",
    "5G": "5G provides ultra-low latency (URLLC), high bandwidth (eMBB), and massive device connectivity (mMTC), essential for real-time industrial automation.",
    "AI": "Artificial Intelligence enables systems to perform tasks that require human-like intelligence, such as pattern recognition, decision-making, and prediction.",
    "Machine Learning": "Machine Learning is a subset of AI where systems learn from data to improve performance without being explicitly programmed for every scenario.",
    "Digital Twin": "A Digital Twin is a virtual replica of a physical asset or process that uses real-time data for simulation, monitoring, and optimization.",
    "Cobot": "Collaborative Robots (Cobots) are designed to work safely alongside humans, augmenting human creativity with robotic precision and strength.",
    "Sustainability": "In Industry 5.0, sustainability involves respecting planetary boundaries and using renewable resources to minimize environmental impact.",
    "Resilience": "Resilience is the ability of manufacturing systems to adapt and recover quickly from global disruptions or supply chain shocks.",
    "Edge Computing": "Edge Computing processes data locally near the sensors to reduce latency and bandwidth usage before sending critical data to the cloud."
}

def get_explanation(question, answer):
    text = (question + " " + answer).lower()
    for key, expl in explanations.items():
        if key.lower() in text:
            return expl
    return "The correct answer is supported by the technical definitions of the topic discussed in the question."

# Update explanations
for q in questions:
    q['explanation'] = get_explanation(q['question'], q['answer'])

# Save back
with open('../src/data/ete_unit1.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=4)

print("Explanations added successfully.")
