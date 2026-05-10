import json

def enhance_explanations(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    # Simple mapping of key terms to explanations for Unit 1
    patterns = {
        "Industry 1.0": "Industry 1.0 was characterized by mechanization through steam and water power in the 18th century.",
        "Industry 2.0": "Industry 2.0 (late 19th century) introduced mass production, assembly lines, and electrical energy.",
        "Industry 3.0": "Industry 3.0 brought automation through computers, IT systems, and the use of PLCs in the late 20th century.",
        "Industry 4.0": "Industry 4.0 focuses on Cyber-Physical Systems, IoT, cloud computing, and real-time data interconnectivity.",
        "Industry 5.0": "Industry 5.0 (Human-centric) focuses on the collaboration between humans and machines (Cobots), sustainability, and resilience.",
        "IoT": "The Internet of Things (IoT) enables physical objects to connect and exchange data over the internet using sensors and actuators.",
        "5G": "5G technology provides ultra-low latency, high bandwidth, and massive device connectivity essential for Industry 4.0.",
        "Machine Learning": "Machine Learning (ML) is a subset of AI that allows systems to learn from data patterns without explicit programming.",
        "Cyber-Physical System": "CPS integrates physical mechanical components with advanced computing algorithms and networks for real-time monitoring and control.",
        "Digital Twin": "A Digital Twin is a virtual, real-time replica of a physical asset used for simulation and optimization.",
        "Edge Computing": "Edge computing processes data locally near sensors to reduce latency and bandwidth before sending it to the cloud.",
        "Cobot": "A Collaborative Robot (Cobot) is designed to work safely alongside human workers in a shared workspace.",
        "Circular Economy": "A circular economy aims to minimize waste by designing products for reuse, repair, and recycling.",
        "MQTT": "MQTT is a lightweight messaging protocol specifically designed for resource-constrained IoT devices.",
        "IPv6": "IPv6 provides a vastly larger pool of unique IP addresses, which is critical for identifying billions of IoT devices.",
        "Smart Meter": "An IoT-enabled smart meter records electrical consumption in real-time and allows two-way communication with the utility."
    }

    for q in questions:
        for key, text in patterns.items():
            if key.lower() in q['question'].lower():
                q['explanation'] = text
                break
        else:
            # Fallback if no keyword matches
            ans_text = q['answer'].split(') ')[1]
            q['explanation'] = f"The correct answer is '{ans_text}', which is a core concept of {q['question'].split(' ')[-1]} in the ETE Unit 1 curriculum."

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=4)

enhance_explanations('../src/data/ete_unit1.json')
print("Explanations enhanced for ETE Unit 1.")
