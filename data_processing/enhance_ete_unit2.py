import json

def enhance_unit2_explanations(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    patterns = {
        "Smart Grid": "A Smart Grid uses two-way digital communication to monitor and manage the transport of electricity from all generation sources to meet the varying electricity demands of end users.",
        "PMU": "Phasor Measurement Units (PMUs) provide real-time, GPS-synchronized measurements of voltage and current phasors to ensure grid stability.",
        "AMI": "Advanced Metering Infrastructure (AMI) is a two-way communication system between a smart meter and the utility company.",
        "Micro-Grid": "A Micro-Grid is a localized group of electricity sources and loads that can operate independently (Islanding) or connected to the main grid.",
        "Islanding": "Islanding is the ability of a microgrid to disconnect from the main utility grid and continue to provide power locally during an outage.",
        "DER": "Distributed Energy Resources (DERs) are small-scale power generation or storage technologies (like solar panels and batteries) located close to where they are used.",
        "Prosumer": "A prosumer is a consumer who also produces electricity, typically through rooftop solar panels, and feeds excess power back into the grid.",
        "SCADA": "SCADA (Supervisory Control and Data Acquisition) is a system of software and hardware elements that allows industrial organizations to control industrial processes locally or at remote locations.",
        "IEC 61850": "IEC 61850 is an international standard for communication in substations, enabling interoperability between devices from different vendors.",
        "GOOSE": "GOOSE (Generic Object Oriented Substation Event) is a fast communication protocol in IEC 61850 used for critical protection and interlocking signals.",
        "SAS": "Substation Automation System (SAS) uses IEDs to monitor, control, and protect substation equipment automatically.",
        "V2G": "Vehicle-to-Grid (V2G) technology allows electric vehicle batteries to discharge power back into the grid during peak demand to help stabilize it.",
        "Peak Shaving": "Peak shaving involves reducing electricity consumption during maximum demand periods to lower costs and reduce stress on the grid.",
        "CHP": "Combined Heat and Power (CHP) or Cogeneration simultaneously generates electricity and useful heat from the same fuel source, improving efficiency.",
        "Cybersecurity": "In smart grids, cybersecurity is critical because the high level of digital interconnectivity makes the power network vulnerable to remote attacks."
    }

    for q in questions:
        for key, text in patterns.items():
            if key.lower() in q['question'].lower():
                q['explanation'] = text
                break
        else:
            ans_text = q['answer'].split(') ')[1]
            q['explanation'] = f"The correct answer is '{ans_text}', which is a vital component of the Smart Grid / Micro-Grid architecture covered in Unit 2."

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=4)

enhance_unit2_explanations('../src/data/ete_unit2.json')
print("Explanations enhanced for ETE Unit 2.")
