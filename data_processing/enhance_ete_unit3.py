import json

def enhance_unit3_explanations(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    patterns = {
        "Smart City": "A Smart City integrates ICT and IoT to optimize city functions, improve quality of life, and manage resources efficiently.",
        "Metro": "Modern Metro systems use CBTC (Communications-Based Train Control) for automated operation and increased frequency.",
        "EV": "Electric Vehicles (EVs) are essential for sustainable urban mobility, reducing emissions and reliance on fossil fuels.",
        "Charging": "EV charging includes Level 1 (slow AC), Level 2 (fast AC), and Level 3 (DC Fast Charging) to meet different user needs.",
        "Wireless Charging": "Wireless EV charging uses electromagnetic induction to transfer power between a transmitter pad on the ground and a receiver on the vehicle.",
        "Smart Home": "A Smart Home uses interconnected IoT devices to provide remote control and automation of appliances, lighting, and HVAC.",
        "Renewable Energy": "Renewable energy sources like rooftop solar are crucial for decarbonizing cities and ensuring local energy security.",
        "Net Metering": "Net Metering allows prosumers to export excess solar power to the grid and earn credits against their consumption.",
        "CBTC": "Communications-Based Train Control (CBTC) uses real-time data to track and control trains, allowing them to run closer together safely.",
        "ATO": "Automated Train Operation (ATO) manages the speed, stopping, and door operations of trains to improve efficiency and safety.",
        "LiDAR": "LiDAR (Light Detection and Ranging) uses laser pulses to create precise 3D maps for autonomous vehicle navigation.",
        "BMS": "The Battery Management System (BMS) monitors and manages the state of individual cells in an EV battery pack for safety.",
        "Smart Light": "Smart lighting uses sensors and AI to adjust brightness based on occupancy and ambient light levels, saving energy.",
        "E-Governance": "E-Governance provides municipal services digitally to increase transparency, efficiency, and citizen engagement.",
        "FAME": "The FAME India scheme provides subsidies and incentives to accelerate the adoption and manufacturing of electric vehicles."
    }

    for q in questions:
        for key, text in patterns.items():
            if key.lower() in q['question'].lower():
                q['explanation'] = text
                break
        else:
            ans_text = q['answer'].split(') ')[1]
            q['explanation'] = f"The correct answer is '{ans_text}', which is a core concept of the Smart City ecosystem covered in Unit 3."

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=4)

enhance_unit3_explanations('../src/data/ete_unit3.json')
print("Explanations enhanced for ETE Unit 3.")
