import json

def enhance_unit5_explanations(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    patterns = {
        "Tariff": "Tariff refers to the schedule of rates and charges defined by a utility to recover the cost of supplying electrical energy to consumers.",
        "PPA": "A Power Purchase Agreement (PPA) is a legally binding contract between a power generator and a buyer (usually a DISCOM) for the sale of electricity over a long period.",
        "Fixed Charge": "Fixed charges (or Capacity Charges) recover the generator's capital investment and fixed operational costs, regardless of the actual energy generated.",
        "Variable Charge": "Variable charges (or Energy Charges) cover the actual cost of fuel (like coal or gas) consumed during the generation process.",
        "Slab": "Slab billing (or Telescopic Tariff) divides consumption into blocks where the price per unit increases as consumption moves into higher blocks to encourage conservation.",
        "Cross Subsidy": "Cross subsidy is the practice of charging higher rates to industrial/commercial users to lower the burden on residential or agricultural consumers.",
        "Smart Meter": "A Smart Meter is a digital device that records energy consumption in near real-time and enables two-way communication between the utility and the consumer.",
        "AMI": "Advanced Metering Infrastructure (AMI) provides the full two-way communication network required for remote reading, disconnects, and firmware updates.",
        "Net Metering": "Net Metering allows prosumers to offset their energy consumption with their own solar generation, paying only for the 'net' units imported from the grid.",
        "Gross Metering": "In Gross Metering, all generated solar power is sold to the grid at one rate, and all consumed power is bought from the grid at another rate.",
        "AMR": "Automated Meter Reading (AMR) is a one-way system where the utility collects readings remotely, eliminating the need for manual meter readers.",
        "ToD": "Time of Day (ToD) tariffs charge different rates based on the time of consumption, with higher rates during peak hours and lower rates during off-peak hours.",
        "MERC": "The Maharashtra Electricity Regulatory Commission (MERC) is the body responsible for approving tariffs and setting rules for the power sector in Maharashtra.",
        "Deep Learning": "Deep learning models (like CNNs) are used in smart billing for Optical Character Recognition (OCR) to read analog meter dials from photographs.",
        "THD": "Total Harmonic Distortion (THD) measures the level of electrical noise in the system; smart meters can monitor this to ensure power quality.",
        "Load Profiling": "Load profiling involves recording energy usage at regular intervals (e.g., 15 mins) to understand consumption patterns over time.",
        "Cybersecurity": "Because smart meters are network-connected, they require robust cybersecurity to prevent hacking and unauthorized remote disconnections."
    }

    for q in questions:
        for key, text in patterns.items():
            if key.lower() in q['question'].lower():
                q['explanation'] = text
                break
        else:
            ans_text = q['answer'].split(') ')[1]
            q['explanation'] = f"The correct answer is '{ans_text}', which is a fundamental concept in power system tariffs and smart billing covered in Unit 5."

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=4)

enhance_unit5_explanations('../src/data/ete_unit5.json')
print("Explanations enhanced for ETE Unit 5.")
