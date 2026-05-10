import json
import os

def enhance_explanation(question_text, answer_text, unit_id):
    q = question_text.lower()
    a = answer_text.lower()
    
    # Common ETI concepts for explanation generation
    concepts = {
        "it act": "The Information Technology Act, 2000 provides the legal framework for e-commerce and cybercrime in India.",
        "dpdp": "The Digital Personal Data Protection (DPDP) Act, 2023 regulates the processing of personal data in India.",
        "blockchain": "Blockchain is a decentralized, distributed ledger technology that ensures data immutability and transparency through a chain of blocks.",
        "5g": "5G technology offers ultra-high speeds, massive device connectivity, and ultra-low latency for real-time applications.",
        "iot": "The Internet of Things (IoT) refers to a network of interconnected devices that collect and exchange data using sensors.",
        "quantum": "Quantum computing utilizes qubits and quantum mechanics (superposition/entanglement) to solve complex problems exponentially faster.",
        "green computing": "Green Computing (Sustainable Computing) focuses on reducing the environmental impact of technology through energy efficiency.",
        "forensics": "Digital Forensics involves the scientific identification, preservation, and analysis of digital evidence for legal investigations.",
        "ethical hacking": "Ethical hacking is the authorized process of bypassingsystem security to identify and fix potential data breaches.",
        "ai": "Artificial Intelligence is the branch of computer science that builds smart machines capable of performing human-like tasks.",
        "ml": "Machine Learning is a subset of AI where systems automatically learn and improve from experience without being explicitly programmed.",
        "dl": "Deep Learning is a subset of ML based on artificial neural networks that can learn from vast amounts of unstructured data.",
        "vr": "Virtual Reality (VR) creates a completely artificial, immersive environment that replaces the user's real-world view.",
        "ar": "Augmented Reality (AR) enhances the real world by overlaying digital elements like images or sounds onto it.",
        "mr": "Mixed Reality (MR) combines both real and virtual worlds where physical and digital objects co-exist and interact in real-time.",
        "section 66": "Section 66 of the IT Act deals with various computer-related offenses like identity theft and cheating by personation.",
        "smart contract": "A smart contract is a self-executing contract with the agreement terms directly written into code on a blockchain.",
        "consensus": "Consensus algorithms (like PoW or PoS) ensure that all nodes in a blockchain network agree on the ledger's state.",
        "supervised": "Supervised learning uses labeled training data to teach algorithms how to predict outcomes or classify data.",
        "unsupervised": "Unsupervised learning finds hidden patterns or intrinsic structures in input data without using labeled responses.",
        "reinforcement": "Reinforcement learning is about taking suitable action to maximize reward in a particular situation.",
        "phishing": "Phishing is a cyber attack that uses disguised email or websites as a weapon to steal sensitive user data.",
        "ransomware": "Ransomware is a type of malware that threatens to publish or block access to data unless a ransom is paid.",
        "zero-day": "A zero-day exploit is an attack that targets a software vulnerability which is unknown to the software developer.",
        "mfa": "Multi-Factor Authentication (MFA) adds a layer of security by requiring two or more verification methods for access.",
        "cert-in": "CERT-In is the national nodal agency for responding to computer security incidents in India.",
        "uml": "Unified Modeling Language (UML) is used to visualize and document the design of software systems, including forensic models.",
        "dfrws": "The DFRWS (Digital Forensic Research Workshop) model is a popular framework used in digital investigations.",
        "adfm": "The Abstract Digital Forensic Model (ADFM) is a comprehensive model that includes a preparation phase.",
        "idip": "The Integrated Digital Investigation Process (IDIP) integrates digital and physical crime scene investigations.",
        "eedip": "The Enhanced Digital Investigation Process (EEDIP) focuses on automation and traceability in forensics.",
        "it act 2000": "The IT Act 2000 is the primary law in India dealing with cybercrime and electronic commerce.",
        "cyber terrorism": "Section 66F of the IT Act specifically addresses cyber terrorism and its legal consequences.",
        "identity theft": "Section 66C of the IT Act prescribes punishment for identity theft using digital resources.",
        "encryption": "Encryption is the process of converting information into a secret code to prevent unauthorized access.",
        "integrity": "In cybersecurity, integrity ensures that data has not been tampered with or modified by unauthorized parties.",
        "authentication": "Authentication is the process of verifying the identity of a user, device, or system.",
        "availability": "Availability ensures that systems and data are accessible to authorized users when needed.",
        "deepfake": "Deepfakes are synthetic media in which a person in an existing image or video is replaced with someone else's likeness using AI.",
        "vulnerability": "A vulnerability is a weakness in a system that can be exploited by an attacker to cause harm."

    }

    # Sort keys by length descending to match more specific terms first (e.g. 'ethical hacking' before 'hacking')
    sorted_keys = sorted(concepts.keys(), key=len, reverse=True)

    matched_concept = None
    for key in sorted_keys:
        if key in q or key in a:
            matched_concept = concepts[key]
            break
    
    if matched_concept:
        return f"{matched_concept} Thus, the correct answer is '{answer_text}'."
    else:
        return f"This question focuses on '{answer_text}'. Understanding this is key to mastering the syllabus content of Unit {unit_id}."

def process_file(file_path, unit_id):
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        # Check if explanation is generic or from previous pass
        current_exp = item.get('explanation', '')
        is_generic = (
            "foundational principle" in current_exp or 
            "essential to" in current_exp or 
            "Thus, the correct answer is" in current_exp or
            "Understanding this is key to mastering" in current_exp or
            not current_exp
        )
        if is_generic:
            item['explanation'] = enhance_explanation(item['question'], item['answer'], unit_id)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"Enhanced {len(data)} explanations in {file_path}")

if __name__ == "__main__":
    files = [
        ("src/data/questions.json", 1),
        ("src/data/unit2_questions.json", 2),
        ("src/data/unit3_questions.json", 3),
        ("src/data/unit4_questions.json", 4),
        ("src/data/unit5_questions.json", 5)
    ]
    for f, uid in files:
        process_file(f, uid)
