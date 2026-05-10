import json
import re

text = """
Unit 1: Digitalization beyond Automation
Topic 1.1: Industrial Revolutions (Versions 1.0, 2.0, 3.0 and 4.0)
1. What was the primary driving force behind the First Industrial Revolution (Industry
1.0)?
A) Electricity
B) Steam and water power
C) Computers and IT
D) Cyber-Physical Systems
Answer: B
2. In which century did the First Industrial Revolution primarily take place?
A) 16th Century
B) 18th Century
C) 20th Century
D) 21st Century
Answer: B
3. What was the defining technological advancement that drove Industry 2.0?
A) The mechanical loom
B) The internet
C) Electrical energy and mass production
D) Artificial Intelligence
Answer: C
4. The concept of the "Assembly Line" is most strongly associated with which industrial
revolution?
A) Industry 1.0
B) Industry 2.0
C) Industry 3.0
D) Industry 4.0
Answer: B
5. Who is famously known for pioneering the use of assembly lines in mass production
during Industry 2.0?
A) James Watt
B) Nikola Tesla
C) Henry Ford
D) Alan Turing
Answer: C
6. Which industrial revolution was driven by the introduction of computers, IT systems,
and early automation?
A) Industry 1.0
B) Industry 2.0
C) Industry 3.0
D) Industry 4.0
Answer: C
7. The invention and widespread use of the Programmable Logic Controller (PLC) was a
hallmark of:
A) Industry 1.0
B) Industry 2.0
C) Industry 3.0
D) Industry 5.0
Answer: C
8. What is the central driving force behind the Fourth Industrial Revolution (Industry
4.0)?
A) Steam engines
B) Cyber-Physical Systems, IoT, and interconnected networks
C) The telegraph
D) Mechanization of agriculture
Answer: B
9. Which industrial revolution marks the transition from purely mechanical and analog
electronic technology to digital electronics?
A) Industry 1.0
B) Industry 2.0
C) Industry 3.0
D) Industry 4.0
Answer: C
10. The term "Industry 4.0" originally originated from a high-tech strategy project of
which country's government?
A) United States
B) Japan
C) Germany
D) China
Answer: C
11. Industry 1.0 brought mechanization. What did Industry 4.0 bring?
A) Electrification
B) Digitalization and interconnectivity
C) Manual craftsmanship
D) Steam-powered robotics
Answer: B
12. Which of the following best describes the progression of the four industrial revolutions?
A) Mechanization -> Electrification -> Automation -> Interconnectivity
B) Electrification -> Automation -> Mechanization -> Interconnectivity
C) Interconnectivity -> Mechanization -> Electrification -> Automation
D) Automation -> Electrification -> Interconnectivity -> Mechanization
Answer: A
13. In the context of industrial history, the shift from bespoke, custom-made goods to
standardized goods was the result of:
A) Industry 1.0
B) Industry 2.0
C) Industry 3.0
D) Industry 4.0
Answer: B
14. What enabled the highly automated operations seen in Industry 3.0?
A) Coal
B) Microprocessors and telecommunications
C) Steam turbines
D) Mechanical gears
Answer: B
15. In Industry 4.0, machines are able to communicate with each other directly to optimize
production. This concept is known as:
A) M2M (Machine-to-Machine) communication
B) P2P (Peer-to-Peer) sharing
C) B2B (Business-to-Business) networking
D) Human-to-Machine interaction
Answer: A
16. Which revolution allowed manufacturing to move away from being strictly located next
to rivers or water sources?
A) Industry 1.0
B) Industry 2.0 (due to electrical power grids)
C) Industry 3.0
D) Industry 4.0
Answer: B
17. The widespread use of industrial robotics for repetitive tasks on assembly lines became
standard during:
A) Industry 1.0
B) Industry 2.0
C) Industry 3.0
D) Industry 4.0
Answer: C
18. What makes Industry 4.0 fundamentally different from Industry 3.0?
A) Industry 4.0 uses electricity; Industry 3.0 did not
B) Industry 4.0 integrates physical machines with digital networks, allowing them to make
decentralized decisions
C) Industry 4.0 relies on human muscle power
D) There is no difference; they are the same
Answer: B
19. A "Smart Factory" is the ultimate realization of which industrial revolution?
A) Industry 1.0
B) Industry 2.0
C) Industry 3.0
D) Industry 4.0
Answer: D
20. Which revolution is characterized by the merging of the physical, digital, and biological
worlds?
A) Industry 1.0
B) Industry 2.0
C) Industry 3.0
D) Industry 4.0
Answer: D
Topic 1.2: Components of Industrial Revolution 4.0
21. In the context of Industry 4.0, what does "Digitization" strictly refer to?
A) Moving physical objects
B) The process of converting physical information into digital formats (e.g., converting a paper
manual into a PDF)
C) Generating electricity
D) Hiring more human workers
Answer: B
22. What is a Cyber-Physical System (CPS)?
A) A video game console
B) A system where physical mechanical components are monitored, controlled, and integrated by
advanced computing algorithms and networks
C) A purely mechanical machine with no electronics
D) A database stored entirely in the cloud
Answer: B
23. Which of the following is a core component of a Cyber-Physical System?
A) Actuators and Sensors
B) Steam engines
C) Waterwheels
D) Paper ledgers
Answer: A
24. What role does the Internet of Things (IoT) play in Industry 4.0?
A) It isolates computers from the network
B) It provides the connectivity layer that allows physical machines, sensors, and devices to
communicate and exchange data over the internet
C) It replaces all physical machines with software
D) It forces workers to use paper
Answer: B
25. Cloud Computing in Industry 4.0 provides manufacturing facilities with:
A) Localized, hardware-bound storage that cannot be scaled
B) On-demand availability of computer system resources, data storage, and computing power
without direct active management by the user
C) Weather forecasting for the factory roof
D) Analog communication channels
Answer: B
26. What is "Cloud Manufacturing"?
A) Manufacturing products out of water vapor
B) A new manufacturing paradigm that transforms physical manufacturing resources into
services shared over the cloud (Manufacturing-as-a-Service)
C) Building factories in high-altitude areas
D) Manufacturing that only occurs on airplanes
Answer: B
27. Big Data Analytics is heavily used in Industry 4.0 to:
A) Delete unnecessary files
B) Process the massive amounts of data generated by IoT sensors to identify patterns, optimize
processes, and predict failures
C) Print large posters for the factory
D) Slow down the manufacturing line
Answer: B
28. How does Cloud Computing aid smaller electrical engineering firms?
A) By requiring them to buy massive on-premise servers
B) By allowing them to access powerful, scalable computing resources on a pay-as-you-go basis
without heavy capital investment
C) By disconnecting them from global markets
D) By removing their ability to store data
Answer: B
29. Which component acts as the "bridge" between the physical hardware on the factory
floor and the digital analytics in the cloud?
A) The power supply
B) The Industrial Internet of Things (IIoT) gateway/sensors
C) The mechanical conveyor belt
D) The factory roof
Answer: B
30. In Cloud Manufacturing, physical CNC machines or 3D printers can be:
A) Accessed and commanded remotely over the internet by customers globally
B) Operated only via manual hand-cranks
C) Powered by steam
D) Eliminated completely
Answer: A
31. What is "Edge Computing" in the context of IoT and Cloud?
A) Processing data purely on centralized cloud servers far away
B) Processing data locally near the sensors (at the edge of the network) to reduce latency and
save bandwidth before sending critical summaries to the cloud
C) Computing using analog slide rules
D) Pushing machines to the edge of the factory floor
Answer: B
32. Why is Edge Computing often necessary alongside Cloud Computing in Industry 4.0?
A) Because the cloud is too fast
B) Because some electrical systems (like motor fault protection) require millisecond-level
response times that a distant cloud server cannot guarantee
C) Because edge computing consumes more power
D) Because the cloud cannot store data
Answer: B
33. The integration of CPS, IoT, and Cloud Computing leads to the creation of:
A) A Digital Twin
B) A purely analog system
C) A mechanical loom
D) An assembly line
Answer: A
34. What is a "Digital Twin"?
A) A spare physical machine kept in storage
B) A virtual, real-time replica of a physical asset, process, or system used for simulation,
monitoring, and optimization
C) A factory that produces twin products
D) A backup hard drive
Answer: B
35. If an electrical engineer simulates the thermal stress of a new motor under heavy load
using a virtual model synced with real-world sensor data, they are using:
A) A Digital Twin
B) A physical prototype
C) Cloud Manufacturing
D) A steam engine
Answer: A
36. Which of the following is an example of "Digitalization" (as opposed to mere
digitization)?
A) Scanning a document
B) Using digital data to entirely restructure and optimize a company's business model and
manufacturing process
C) Taking a digital photograph
D) Typing on a keyboard
Answer: B
37. How does IoT improve inventory management in Cloud Manufacturing?
A) By counting items manually
B) By using RFID and smart sensors to track raw materials and finished goods in real-time
across the supply chain
C) By guessing stock levels
D) By hiding inventory from the cloud
Answer: B
38. What is the primary security concern regarding the components of Industry 4.0?
A) Machines running out of oil
B) Cybersecurity vulnerabilities due to the massive interconnectivity of physical machines to
global networks
C) Workers forgetting their physical keys
D) Cloud servers taking up too much physical space
Answer: B
39. In a Cyber-Physical System, which part is responsible for executing the commands
received from the digital controller?
A) The Sensor
B) The Actuator
C) The Cloud
D) The Network Router
Answer: B
40. Interoperability in Industry 4.0 refers to:
A) Machines breaking down simultaneously
B) The ability of different systems, machines, and software from different manufacturers to
connect, communicate, and share data seamlessly
C) The inability of machines to work together
D) Operators working in different factories
Answer: B
41. Which cloud service model provides a platform allowing customers to develop, run, and
manage applications without the complexity of building infrastructure?
A) SaaS (Software as a Service)
B) PaaS (Platform as a Service)
C) IaaS (Infrastructure as a Service)
D) MaaS (Manufacturing as a Service)
Answer: B
42. Which cloud service model provides fully functional applications directly to the enduser over the internet (e.g., Google Workspace)?
A) SaaS
B) PaaS
C) IaaS
D) DaaS
Answer: A
Topic 1.3: Role of 5G, ML, and AI in Industry 4.0
43. What is the primary advantage of 5G communication over 4G in an industrial setting?
A) Slower data speeds
B) Ultra-low latency, massive device connectivity, and much higher bandwidth
C) It requires physical cables
D) It uses analog signals
Answer: B
44. Which specific 5G feature is crucial for real-time control of fast-moving robotics and
autonomous vehicles in a smart factory?
A) eMBB (Enhanced Mobile Broadband)
B) URLLC (Ultra-Reliable Low Latency Communication)
C) mMTC (Massive Machine Type Communication)
D) SMS texting
Answer: B
45. What does the mMTC (Massive Machine Type Communication) feature of 5G enable?
A) High-definition video streaming
B) The connection of up to a million low-power IoT sensors per square kilometer without
network congestion
C) Faster phone calls
D) The elimination of the cloud
Answer: B
46. What is Machine Learning (ML)?
A) A machine learning to assemble products physically
B) A subset of AI that uses algorithms and statistical models to enable systems to learn from data
and improve performance without explicit programming
C) A robot reading a manual
D) Hardwiring logic gates into a circuit
Answer: B
47. In electrical engineering, how is Machine Learning primarily used for motor
maintenance?
A) By scheduling maintenance every 30 days regardless of condition
B) By analyzing vibration, temperature, and current data to predict exactly when a motor will fail
(Predictive Maintenance)
C) By turning the motor on and off randomly
D) By painting the motor
Answer: B
48. Artificial Intelligence (AI) in Industry 4.0 refers to:
A) Machines generating their own electricity
B) Computer systems capable of performing tasks that typically require human intelligence, such
as visual perception, speech recognition, and complex decision-making
C) A mechanical clock
D) A standard calculator
Answer: B
49. How does AI optimize the energy consumption of a smart factory?
A) By keeping all lights on 24/7
B) By dynamically analyzing production schedules and energy grid prices to run power-heavy
tasks during off-peak, cheaper energy hours
C) By turning off the main power supply permanently
D) By replacing electrical machines with manual labor
Answer: B
50. What is "Computer Vision," a prominent AI technology used in smart manufacturing?
A) A worker wearing glasses
B) AI systems analyzing digital images or videos from cameras to automatically detect defects in
products on an assembly line
C) A screen displaying text
D) A blind robot
Answer: B
51. How does 5G support the implementation of AI and ML?
A) By slowing down the transfer of data
B) By providing the massive, instantaneous data pipeline required to send factory floor data to
cloud AI models and return decisions in real-time
C) By replacing the AI completely
D) It does not support AI
Answer: B
52. What is "Supervised Learning" in the context of ML?
A) Learning without any data
B) Training an algorithm using a dataset that is already labeled with the correct answers (e.g.,
images labeled as "defective" or "normal")
C) An algorithm finding hidden patterns in unlabeled data
D) A robot being watched by a manager
Answer: B
53. If an electrical grid uses an ML algorithm to group consumers based on their daily
power usage patterns without predefined categories, it is using:
A) Supervised Learning
B) Unsupervised Learning (Clustering)
C) Reinforcement Learning
D) Manual sorting
Answer: B
54. An AI system that learns to control an HVAC system by receiving "rewards" for saving
energy and "punishments" for letting the room get too hot is using:
A) Supervised Learning
B) Unsupervised Learning
C) Reinforcement Learning
D) Deep Learning
Answer: C
55. Which of the following tasks is an AI expert system best suited for in an electrical
distribution grid?
A) Digging trenches for cables
B) Automatically rerouting power around a fallen transformer to minimize the outage area within
milliseconds
C) Generating electricity
D) Printing customer bills
Answer: B
56. What does "Network Slicing" in 5G allow a factory to do?
A) Cut fiber optic cables
B) Create multiple, dedicated virtual networks over the same physical 5G infrastructure, ensuring
critical machine data is isolated from employee smartphone traffic
C) Share internet with the entire city
D) Slice data into smaller packets manually
Answer: B
57. Without AI and ML, the massive amount of data generated by thousands of IoT sensors
in a factory would be:
A) Extremely easy to read manually
B) Overwhelming and largely useless, as humans cannot process that volume of data to find
meaningful insights quickly
C) Automatically deleted
D) Converted into physical objects
Answer: B
58. Which subset of Machine Learning uses complex Artificial Neural Networks with many
layers to solve highly complex problems like image and voice recognition?
A) Linear Regression
B) Deep Learning
C) Decision Trees
D) K-Means Clustering
Answer: B
59. In the context of 5G, what does "Latency" mean?
A) The total amount of data downloaded
B) The time delay it takes for a packet of data to travel from the source to the destination and
back
C) The physical distance between towers
D) The battery life of the device
Answer: B
60. A self-driving automated guided vehicle (AGV) navigating a busy warehouse relies
heavily on the combination of:
A) Steam power and mechanical gears
B) 5G (for low-latency communication), IoT (sensors), and AI (for obstacle avoidance and
routing)
C) 3G and manual steering
D) Wi-Fi and human remote control
Answer: B
61. What is "Prescriptive Analytics" in AI?
A) Telling you what happened in the past
B) Telling you what will happen in the future
C) Not only predicting a future failure but automatically recommending or executing the specific
actions needed to prevent it
D) Writing a prescription for medicine
Answer: C
62. How does AI assist in Supply Chain Management within Industry 4.0?
A) By predicting demand spikes and automatically adjusting raw material orders and
manufacturing schedules to prevent shortages
B) By hiding inventory data
C) By making transportation slower
D) By eliminating the supply chain
Answer: A
Topic 1.4: Industry Revolution 5.0
63. While Industry 4.0 focuses heavily on automation and machine-to-machine
communication, Industry 5.0 shifts the focus back to:
A) Coal power
B) Human-centricity, bringing the human worker back into the center of the production process
C) Total elimination of the human workforce
D) Manual, non-digital labor
Answer: B
64. Which of the following are the three core pillars of Industry 5.0 according to the
European Commission?
A) Profit, Speed, Automation
B) Human-centricity, Sustainability, and Resilience
C) AI, Cloud, IoT
D) Steam, Electricity, Computers
Answer: B
65. What is a "Cobot"?
A) A robot that fights other robots
B) A Collaborative Robot designed to work safely alongside human workers in a shared
workspace, assisting them with tasks
C) A completely autonomous, caged industrial robot
D) A robot that makes coffee
Answer: B
66. How does Industry 5.0 approach the concept of customization?
A) It promotes strict mass production of identical items
B) It enables "Mass Personalization," combining the efficiency of automated mass production
with the human touch needed to create highly customized, bespoke products
C) It eliminates customization entirely
D) It only allows customization if done completely by hand
Answer: B
67. What does "Sustainability" mean in the context of Industry 5.0?
A) Ensuring the factory stays open forever
B) Designing manufacturing processes that respect planetary boundaries, utilizing circular
economies, renewable energy, and minimizing waste and emissions
C) Sustaining high profit margins at all costs
D) Using non-renewable resources efficiently
Answer: B
68. The concept of a "Circular Economy" is a key part of Industry 5.0. What does it entail?
A) Moving products in a physical circle on the factory floor
B) Transitioning from a "take-make-dispose" model to one where products are designed for
reuse, repair, remanufacturing, and recycling
C) Only trading with neighboring countries
D) Using round packaging
Answer: B
69. What does "Resilience" refer to in Industry 5.0?
A) The physical strength of the factory walls
B) The ability of manufacturing systems and supply chains to adapt to and quickly recover from
massive global disruptions (e.g., pandemics, natural disasters)
C) The inability to change production schedules
D) The rigidity of robots
Answer: B
70. In Industry 5.0, technology is viewed as:
A) A replacement for human workers
B) A tool to empower and augment human workers, protecting them from dangerous tasks while
utilizing their creativity
C) A necessary evil that should be minimized
D) The ultimate authority in the factory
Answer: B
71. Which previous industrial revolution was heavily criticized for ignoring the
psychological well-being of workers and environmental impacts, leading to the
conceptualization of Industry 5.0?
A) Industry 1.0
B) Industry 2.0
C) Industry 4.0
D) All of the above, but 5.0 specifically aims to correct the technology-first approach of 4.0
Answer: D
72. What is ESG, a concept deeply integrated into the goals of Industry 5.0?
A) Electronic System Guidelines
B) Environmental, Social, and Governance criteria used to evaluate a company's collective
conscientiousness
C) Engineering Standard Grades
D) Electrical Safety Gear
Answer: B
73. In a typical Industry 5.0 scenario, what role does the human play?
A) Performing heavy lifting and repetitive physical assembly
B) Providing creative input, complex problem solving, and oversight, while the cobot handles the
heavy lifting and precise repetition
C) Sitting in an office completely disconnected from the factory
D) None; humans are obsolete
Answer: B
74. How does Industry 5.0 handle energy management differently?
A) By consuming maximum power for speed
B) By actively prioritizing energy efficiency, integrating deeply with smart grids, and
maximizing the use of on-site renewable energy sources
C) By relying solely on fossil fuels
D) By turning off machines during the day
Answer: B
75. "Bio-economy" is a concept emerging in Industry 5.0. It involves:
A) Building robots that look like humans
B) Using renewable biological resources from land and sea to produce food, materials, and
energy, replacing fossil-based materials
C) Using biometrics for factory security
D) Making factories out of wood
Answer: B
76. Which of the following is true regarding the relationship between Industry 4.0 and
Industry 5.0?
A) Industry 5.0 replaces and deletes all Industry 4.0 technology
B) Industry 5.0 builds upon the technological foundation of Industry 4.0 (IoT, AI, Cloud) but
shifts the core values towards humanity and the environment
C) They are completely unrelated
D) Industry 4.0 is for electrical engineers, Industry 5.0 is for software engineers
Answer: B
77. An electrical assembly line where a human uses AR glasses to assemble a complex
custom control panel, while a robotic arm hands them the exact parts they need safely,
represents:
A) Industry 2.0
B) Industry 3.0
C) Industry 5.0
D) Pure Industry 4.0
Answer: C
78. Industry 5.0 promotes the idea that workers are an "Investment". In contrast, previous
revolutions often viewed workers as:
A) Gods
B) A "Cost" to be minimized or automated away
C) Shareholders
D) Robots
Answer: B
79. To achieve "Resilience", an Industry 5.0 supply chain might utilize:
A) A single, highly optimized supplier in one country
B) Flexible, modular manufacturing and multiple local suppliers to adapt to sudden border
closures or material shortages
C) Massive warehouses holding 10 years of stock
D) No supply chain at all
Answer: B
80. The ultimate goal of Industry 5.0 is to create a manufacturing industry that is:
A) Faster than light
B) A driver of societal value and ecological preservation, not just economic profit
C) Completely run by AI
D) Based entirely in virtual reality
Answer: B
"""

def parse_mcqs(text):
    questions = []
    # Split by double newline or number followed by period
    # More reliable: split by number followed by period at start of line
    parts = re.split(r'\n(\d+)\.', '\n' + text)
    
    current_id = 1
    for i in range(1, len(parts), 2):
        q_id = parts[i]
        content = parts[i+1]
        
        # Extract question text
        q_match = re.search(r'^(.*?)(?=\n[A-D]\))', content, re.DOTALL)
        if not q_match:
            continue
        question_text = q_match.group(1).strip().replace('\n', ' ')
        
        # Extract options
        options = []
        for opt_char in ['A', 'B', 'C', 'D']:
            opt_match = re.search(fr'{opt_char}\)\s*(.*?)(?=\n[A-D]\)|\nAnswer:|$)', content, re.DOTALL)
            if opt_match:
                opt_text = opt_match.group(1).strip().replace('\n', ' ')
                options.append(f"{opt_char.lower()}) {opt_text}")
        
        # Extract answer
        ans_match = re.search(r'Answer:\s*([A-D])', content)
        answer = ""
        if ans_match:
            ans_char = ans_match.group(1).lower()
            # Find the option that starts with this char
            for opt in options:
                if opt.startswith(f"{ans_char})"):
                    answer = opt
                    break
        
        questions.append({
            "id": current_id,
            "question": question_text,
            "options": options,
            "answer": answer,
            "explanation": "No explanation provided yet."
        })
        current_id += 1
        
    return questions

questions = parse_mcqs(text)
with open('../src/data/ete_unit1.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=4)

print(f"Successfully converted {len(questions)} questions.")
