import json

def enhance_unit4_explanations(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    patterns = {
        "MCC": "A Motor Control Center (MCC) is a centralized assembly that controls and protects multiple electric motors from a single location.",
        "IMCC": "An Intelligent MCC (IMCC) uses microprocessors and communication networks (like Profinet) to provide real-time diagnostics and remote control.",
        "Contactor": "A contactor is an electromechanical switch used for switching an electrical power circuit, typically controlled by a lower power level.",
        "Overload Relay": "An overload relay protects the motor by breaking the circuit when it senses excessive current that could cause overheating.",
        "Busbar": "Busbars are thick copper or aluminum strips that distribute high-current power to all the individual units within the MCC.",
        "Smart Relay": "Smart relays (like SIMOCODE) provide advanced motor management, including protection, monitoring, and fieldbus communication.",
        "SCADA": "IMCCs integrate with SCADA systems to provide operators with a digital dashboard for monitoring motor health and energy usage.",
        "Predictive Maintenance": "Predictive maintenance uses data trends (like rising current or vibration) to fix issues before they lead to a total motor failure.",
        "Harmonics": "Harmonics are electrical distortions caused by non-linear loads like VFDs, which can cause overheating and reduce efficiency.",
        "Power Factor": "Power Factor Correction (PFC) uses capacitor banks to improve efficiency and avoid utility penalties for inductive motor loads.",
        "VFD": "A Variable Frequency Drive (VFD) controls motor speed by varying frequency and voltage, leading to significant energy savings.",
        "Cybersecurity": "Because IMCCs are network-connected, they require cybersecurity measures like RBAC and firewalls to prevent unauthorized access.",
        "HMI": "The Human-Machine Interface (HMI) provides a touch-screen display on the MCC panel for viewing real-time diagnostic data.",
        "Soft Starter": "A soft starter reduces the mechanical and electrical stress on a motor during startup by gradually increasing the voltage.",
        "IIoT": "The Industrial Internet of Things (IIoT) allows IMCC data to be sent to the cloud for advanced analytics and enterprise-wide monitoring."
    }

    for q in questions:
        for key, text in patterns.items():
            if key.lower() in q['question'].lower():
                q['explanation'] = text
                break
        else:
            ans_text = q['answer'].split(') ')[1]
            q['explanation'] = f"The correct answer is '{ans_text}', which is a critical component of the Motor Control Center architecture covered in Unit 4."

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=4)

enhance_unit4_explanations('../src/data/ete_unit4.json')
print("Explanations enhanced for ETE Unit 4.")
