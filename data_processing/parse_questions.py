import json
import re

raw_text = """
1.	Artificial Intelligence primarily aims to: 
a) Replace hardware 
b) Increase internet speed 
c) Mimic human intelligence 
d) Store large data 
Answer: c) Mimic human intelligence 
2. The father of Artificial Intelligence is: 
a) Alan Turing 
b) Geoffrey Hinton 
c) John McCarthy 
d) Elon Musk 
Answer: c) John McCarthy 
3. AI integrates ideas from: 
a) Only computer science 
b) Mathematics only 
c) Multiple disciplines 
d) Robotics only 
Answer: c) Multiple disciplines 
4. Which discipline contributes probability and statistics to AI? 
a) Psychology 
b) Mathematics 
c) Philosophy 
d) Linguistics 
Answer: b) Mathematics 
5. NLP stands for: 
a) Neural Logic Programming 
b) Natural Language Processing 
c) Network Learning Process 
d) Numerical Learning Program 
Answer: b) Natural Language Processing 
6. Machine Learning is a subset of: 
a) Data Science 
b) AI 
c) Robotics 
d) Statistics 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
Answer: b) AI 
7. Deep Learning is a subset of: 
a) AI 
b) Robotics 
c) Machine Learning 
d) Data Mining 
Answer: c) Machine Learning 
8. Which AI approach focuses on rational thinking? 
a) Act like humans 
b) Think well 
c) Act well 
d) Behaviourist approach 
Answer: b) Think well 
9. ELIZA program is an example of: 
a) Think rationally 
b) Act like humans 
c) Think like humans 
d) Super AI 
Answer: b) Act like humans 
10. Narrow AI is also called: 
a) Strong AI 
b) General AI 
c) Weak AI 
d) Super AI 
Answer: c) Weak AI 
11. General AI currently: 
a) Exists widely 
b) Does not exist 
c) Used in hospitals 
d) Used in cars 
Answer: b) Does not exist 
12. Super AI is: 
a) Available in labs 
b) Used in gaming 
c) Hypothetical 
d) Weak AI 
Answer: c) Hypothetical 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
13. Reactive machines: 
a) Store memory 
b) Learn from past 
c) React to present only 
d) Think independently 
Answer: c) React to present only 
14. IBM Deep Blue is: 
a) General AI 
b) Super AI 
c) Reactive Machine 
d) Theory of Mind AI 
Answer: c) Reactive Machine 
15. Self-driving cars are example of: 
a) Reactive machines 
b) Limited memory AI 
c) Super AI 
d) Self-aware AI 
Answer: b) Limited memory AI 
16. Theory of Mind AI focuses on: 
a) Hardware 
b) Human emotions 
c) Data storage 
d) Coding 
Answer: b) Human emotions 
17. Self-awareness AI: 
a) Exists in robots 
b) Exists in labs 
c) Is hypothetical 
d) Used in banking 
Answer: c) Is hypothetical 
18. Supervised learning uses: 
a) Unlabeled data 
b) Random data 
c) Labeled data 
d) Reinforcement signals 
Answer: c) Labeled data 
19. Spam detection is example of: 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Unsupervised learning 
b) Reinforcement learning 
c) Supervised learning 
d) Deep AI 
Answer: c) Supervised learning 
20. K-Means clustering belongs to: 
a) Supervised learning 
b) Reinforcement learning 
c) Unsupervised learning 
d) Deep learning 
Answer: c) Unsupervised learning 
21. Reinforcement learning works on: 
a) Labels 
b) Rewards and penalties 
c) Manual coding 
d) Static logic 
Answer: b) Rewards and penalties 
22. Q-learning is used in: 
a) Supervised learning 
b) Unsupervised learning 
c) Reinforcement learning 
d) Regression 
Answer: c) Reinforcement learning 
23. Deep Learning uses: 
a) Decision trees 
b) Neural networks 
c) Sorting algorithms 
d) Search trees 
Answer: b) Neural networks 
24. Deep Learning requires: 
a) Small data 
b) Medium data 
c) Large datasets 
d) No data 
Answer: c) Large datasets 
25. Neural networks are inspired by: 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) CPU architecture 
b) Human brain 
c) Hard disk 
d) Internet 
Answer: b) Human brain 
26. Backpropagation is used to: 
a) Increase speed 
b) Adjust weights 
c) Delete data 
d) Encrypt files 
Answer: b) Adjust weights 
27. Data Science mainly focuses on: 
a) Hardware 
b) Extracting insights from data 
c) Robotics 
d) Automation only 
Answer: b) Extracting insights from data 
28. Deep Learning automatically: 
a) Deletes features 
b) Extracts features 
c) Stores hardware 
d) Encrypts data 
Answer: b) Extracts features 
29. One disadvantage of Deep Learning: 
a) Needs small data 
b) Requires low power 
c) Hard to interpret 
d) Easy to explain 
Answer: c) Hard to interpret 
30. AI in healthcare helps in: 
a) Gaming 
b) Diagnosis 
c) Coding 
d) Designing hardware 
Answer: b) Diagnosis 
31. AI in finance is used for: 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Fraud detection 
b) Cooking 
c) Printing 
d) Hardware design 
Answer: a) Fraud detection 
32. Recommendation systems use: 
a) ML 
b) OS 
c) Hardware 
d) BIOS 
Answer: a) ML 
33. Actor-Critic methods belong to: 
a) Supervised learning 
b) Reinforcement learning 
c) Unsupervised learning 
d) NLP 
Answer: b) Reinforcement learning 
34. GANs are used in: 
a) Sorting 
b) Image generation 
c) Typing 
d) Data storage 
Answer: b) Image generation 
35. Generative AI creates: 
a) Only tables 
b) Only code 
c) New content 
d) Hardware 
Answer: c) New content 
36. GPT is based on: 
a) CNN 
b) RNN 
c) Transformer 
d) KNN 
Answer: c) Transformer 
37. Self-attention is part of: 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Neural trees 
b) Transformers 
c) Regression 
d) Sorting 
Answer: b) Transformers 
38. Data poisoning attack affects: 
a) Hardware 
b) Training data 
c) CPU 
d) GPU 
Answer: b) Training data 
39. MFA stands for: 
a) Multi-Function Access 
b) Multi-Factor Authentication 
c) Machine Feature Algorithm 
d) Multiple Firewall Access 
Answer: b) Multi-Factor Authentication 
40. Overfitting means: 
a) Model underperforms 
b) Model memorizes training data 
c) Model deletes data 
d) Model encrypts 
Answer: b) Model memorizes training data 
41. IBM Watson is example of: 
a) Super AI 
b) Narrow AI 
c) Self-aware AI 
d) AGI 
Answer: b) Narrow AI 
42. Computer Vision deals with: 
a) Text 
b) Audio 
c) Images and video 
d) Numbers 
Answer: c) Images and video 
43. Logistic Regression is used in: 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Supervised learning 
b) Clustering 
c) Reinforcement 
d) Sorting 
Answer: a) Supervised learning 
44. PCA is used for: 
a) Clustering 
b) Dimensionality reduction 
c) Encryption 
d) Sorting 
Answer: b) Dimensionality reduction 
45. AI’s goal is to: 
a) Reduce RAM 
b) Mimic intelligence 
c) Increase battery 
d) Format data 
Answer: b) Mimic intelligence 
46. Robotics uses AI for: 
a) Manual work only 
b) Intelligent automation 
c) Storage 
d) Deletion 
Answer: b) Intelligent automation 
47. AI-powered cybersecurity detects: 
a) Hardware faults 
b) Network anomalies 
c) Printer issues 
d) File size 
Answer: b) Network anomalies 
48. Deep Learning works best for: 
a) Small tasks 
b) Complex tasks 
c) Manual coding 
d) Basic math 
Answer: b) Complex tasks 
49. ML improves performance by: 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Explicit programming 
b) Learning from data 
c) Deleting files 
d) Resetting systems 
Answer: b) Learning from data 
50. ANI stands for: 
a) Artificial Neural Intelligence 
b) Artificial Narrow Intelligence 
c) Advanced Network Intelligence 
d) Autonomous Neural Interface 
Answer: b) Artificial Narrow Intelligence 
51. AGI stands for: 
a) Artificial General Intelligence 
b) Advanced Global Interface 
c) Automated General Input 
d) Artificial Graph Intelligence 
Answer: a) Artificial General Intelligence 
52. ASI refers to: 
a) Artificial System Intelligence 
b) Artificial Super Intelligence 
c) Advanced Super Interface 
d) Automated Smart Intelligence 
Answer: b) Artificial Super Intelligence 
53. Which type of AI can perform only a specific task? 
a) General AI 
b) Super AI 
c) Narrow AI 
d) Self-aware AI 
Answer: c) Narrow AI 
54. In supervised learning, output is: 
a) Unknown 
b) Labeled 
c) Random 
d) Encrypted 
Answer: b) Labeled 
55. Which learning method is used in customer segmentation? 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Supervised learning 
b) Unsupervised learning 
c) Reinforcement learning 
d) Deep learning only 
Answer: b) Unsupervised learning 
56. Reinforcement learning is commonly used in: 
a) Email sorting 
b) Game AI 
c) Word processing 
d) Spreadsheet design 
Answer: b) Game AI 
57. Decision Tree is an algorithm used in: 
a) Supervised learning 
b) Unsupervised learning 
c) Reinforcement learning 
d) Robotics only 
Answer: a) Supervised learning 
58. Deep learning models require: 
a) Less computation 
b) Moderate computation 
c) High computational power 
d) No computation 
Answer: c) High computational power 
59. Hidden layers are present in: 
a) Basic algorithms 
b) Neural networks 
c) Search trees 
d) Operating systems 
Answer: b) Neural networks 
60. Backpropagation is mainly used for: 
a) Data cleaning 
b) Weight adjustment 
c) Encryption 
d) Sorting 
Answer: b) Weight adjustment 
61. The input layer in neural network: 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Produces output 
b) Receives data 
c) Deletes data 
d) Encrypts data 
Answer: b) Receives data 
62. Overfitting occurs when: 
a) Model performs well on new data 
b) Model memorizes training data 
c) Model deletes errors 
d) Model underperforms 
Answer: b) Model memorizes training data 
63. One advantage of deep learning: 
a) Requires small dataset 
b) High interpretability 
c) Automated feature extraction 
d) Low computational need 
Answer: c) Automated feature extraction 
64. One disadvantage of deep learning: 
a) Easy to interpret 
b) Low accuracy 
c) Requires large dataset 
d) Needs no hardware 
Answer: c) Requires large dataset 
65. NLP helps machines to: 
a) Build hardware 
b) Understand human language 
c) Repair software 
d) Encrypt networks 
Answer: b) Understand human language 
66. Example of Generative AI: 
a) K-Means 
b) ChatGPT 
c) Excel 
d) Router 
Answer: b) ChatGPT 
67. GAN stands for: 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) General AI Network 
b) Generative Adversarial Network 
c) Global Artificial Node 
d) Graphical AI Network 
Answer: b) Generative Adversarial Network 
68. Transformer architecture is mainly used in: 
a) Hardware design 
b) NLP tasks 
c) Operating systems 
d) Networking 
Answer: b) NLP tasks 
69. Self-attention mechanism helps to: 
a) Delete tokens 
b) Focus on relevant words 
c) Encrypt data 
d) Sort data 
Answer: b) Focus on relevant words 
70. Data Science overlaps with: 
a) AI and ML 
b) Hardware 
c) BIOS 
d) Firmware 
Answer: a) AI and ML 
71. Fraud detection mainly uses: 
a) ML algorithms 
b) Printers 
c) Modems 
d) RAM 
Answer: a) ML algorithms 
72. Robotics combined with AI leads to: 
a) Manual control 
b) Intelligent automation 
c) Data deletion 
d) Network failure 
Answer: b) Intelligent automation 
73. Image recognition is example of: 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Computer Vision 
b) Data entry 
c) Encryption 
d) Formatting 
Answer: a) Computer Vision 
74. Spam filtering is: 
a) Unsupervised learning 
b) Supervised learning 
c) Reinforcement learning 
d) Reactive AI 
Answer: b) Supervised learning 
75. Actor-Critic methods are used in: 
a) Supervised learning 
b) Unsupervised learning 
c) Reinforcement learning 
d) Regression only 
Answer: c) Reinforcement learning 
76. AI in manufacturing is used for: 
a) Predictive maintenance 
b) Formatting drives 
c) Typing 
d) Gaming 
Answer: a) Predictive maintenance 
77. Which AI type understands social interactions? 
a) Limited memory 
b) Reactive machine 
c) Theory of Mind 
d) Narrow AI 
Answer: c) Theory of Mind 
78. AI-powered anomaly detection is used in: 
a) Gaming 
b) Cybersecurity 
c) Cooking 
d) Painting 
Answer: b) Cybersecurity 
79. Deep learning performs feature extraction: 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Manually 
b) Automatically 
c) Randomly 
d) Sequentially 
Answer: b) Automatically 
80. Neural networks are useful for: 
a) Linear problems only 
b) Complex non-linear problems 
c) Hardware repair 
d) File deletion 
Answer: b) Complex non-linear problems 
81. Which ML type does not use labels? 
a) Supervised 
b) Reinforcement 
c) Unsupervised 
d) Deep 
Answer: c) Unsupervised 
82. Example of supervised algorithm: 
a) K-Means 
b) PCA 
c) Decision Tree 
d) Hierarchical clustering 
Answer: c) Decision Tree 
83. Example of unsupervised algorithm: 
a) Logistic Regression 
b) K-Means 
c) SVM 
d) Random Forest 
Answer: b) K-Means 
84. Reinforcement learning agent learns through: 
a) Labels 
b) Instructions 
c) Rewards 
d) Hardcoding 
Answer: c) Rewards 
85. AI in autonomous vehicles is used for: 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Typing 
b) Navigation 
c) Formatting 
d) Printing 
Answer: b) Navigation 
86. Data poisoning attack targets: 
a) Hardware 
b) Training data 
c) CPU 
d) RAM 
Answer: b) Training data 
87. Adversarial attack aims to: 
a) Improve model 
b) Deceive AI model 
c) Train faster 
d) Increase memory 
Answer: b) Deceive AI model 
88. MFA increases: 
a) Storage 
b) Security 
c) Speed 
d) RAM 
Answer: b) Security 
89. Philosophy contributes to AI in: 
a) Ethics 
b) Hardware 
c) Coding 
d) Formatting 
Answer: a) Ethics 
90. Psychology contributes to AI by studying: 
a) CPU 
b) Human behaviour 
c) Hard disk 
d) Networks 
Answer: b) Human behaviour 
91. Neuroscience inspired: 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Firewalls 
b) Neural networks 
c) Modems 
d) BIOS 
Answer: b) Neural networks 
92. Linguistics helps in: 
a) NLP 
b) Robotics 
c) Hardware 
d) Encryption 
Answer: a) NLP 
93. AI in retail is used for: 
a) Hardware repair 
b) Recommendation systems 
c) Formatting 
d) Coding 
Answer: b) Recommendation systems 
94. Deep Learning works best with: 
a) Small data 
b) Large data 
c) No data 
d) Static data 
Answer: b) Large data 
95. ML model generalizes to: 
a) Old data only 
b) New unseen data 
c) No data 
d) Corrupt data 
Answer: b) New unseen data 
96. GPU is required for: 
a) Basic ML 
b) Deep Learning training 
c) Word processing 
d) Printing 
Answer: b) Deep Learning training 
97. Generative AI mainly creates: 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Hardware 
b) Static code only 
c) New content 
d) Operating systems 
Answer: c) New content 
98. Foundation model is: 
a) Small model 
b) Large pre-trained model 
c) Antivirus 
d) Firewall 
Answer: b) Large pre-trained model 
99. Chatbots use: 
a) NLP 
b) BIOS 
c) Hardware 
d) Printer drivers 
Answer: a) NLP 
100. Generative AI is subset of: 
a) AI 
b) ML 
c) Deep Learning 
d) Data Science 
Answer: c) Deep Learning 
101. Who is known as the father of Artificial Intelligence? 
a) Alan Turing 
b) John McCarthy 
c) Andrew Ng 
d) Geoffrey Hinton 
Answer: b) John McCarthy
102. Which discipline is NOT directly a part of AI core contributors? 
a) Mathematics 
b) Psychology 
c) Astrology 
d) Linguistics 
Answer: c) Astrology
103. What is the ultimate goal of Artificial Intelligence? 
a) Only solve mathematical problems. 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
b) Mimic human intelligence to solve complex tasks. 
c) Operate machines without human intervention. 
d) Build hardware devices. 
Answer: b) Mimic human intelligence to solve complex tasks.
104. Which statement its “Weak AI” or Narrow AI? 
a) Has general human-level intelligence. 
b) Excels at multiple tasks simultaneously. 
c) Performs dedicated tasks within a limited scope. 
d) Can reason like a human. 
Answer: c) Performs dedicated tasks within a limited scope.
105. What differentiates Super AI from General AI? 
a) Super AI has narrowly focused skills. 
b) General AI can exceed human intellectual performance. 
c) Super AI surpasses human intelligence in every domain. 
d) Super AI has no cognitive abilities. 
Answer: c) Super AI surpasses human intelligence in every domain.
106. Reactive Machines in AI are characterized by …… 
a) the ability to store past experiences. 
b) purely reacting to current inputs without memory. 
c) being self-aware. 
d) understanding human emotions. 
Answer: b) purely reacting to current inputs without memory.
107. What is the major focus of Theory of Mind AI? 
a) Data storage 
b) Understanding emotions and beliefs 
c) Performing calculations quickly 
d) Robot mechanics 
Answer: b) Understanding emotions and beliefs
108. Which AI category is still hypothetical and involves consciousness? 
a) Reactive Machines 
b) Limited Memory 
c) Self-Awareness AI 
d) Narrow AI 
Answer: c) Self-Awareness AI
109. AI helps in healthcare by …… 
a) Diagnosing diseases and patient monitoring. 
b) Replacing doctors fully. 
c) Only recording patient data. 
d) Eliminating all human interaction. 
Answer: a) Diagnosing diseases and patient monitoring.
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
110. What role does linguistics play in AI? 
a) Hardware design 
b) Natural Language Processing 
c) Robotics control 
d) Statistical analysis 
Answer: b) Natural Language Processing
111. Machine Learning is best described as: 
a) Programming specific instructions explicitly 
b) Training systems to learn from data 
c) Hardware manufacturing 
d) Software debugging 
Answer: b) Training systems to learn from data
112. Which is an example of supervised learning? 
a) Clustering customer groups 
b) Email spam filtering with labeled emails 
c) Random data generation 
d) Exploring databases 
Answer: b) Email spam filtering with labeled emails
113. What algorithm is mainly used in supervised learning? 
a) K-means clustering 
b) Logistic regression 
c) PCA 
d) Reinforcement learning 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
Answer: b) Logistic regression 
114. Unsupervised learning primarily involves: 
a) Learning from labelled data. 
b) Discovering patterns from unlabelled data. 
c) Making decisions based on rewards. 
d) Pre-programmed rules. 
Answer: b) Discovering patterns from unlabelled data. 
115. Reinforcement learning is based on …… 
a) receiving rewards or penalties through trial and error. 
b) grouping data clusters. 
c) identifying keywords. 
d) using labeled data only. 
Answer: a) receiving rewards or penalties through trial and error. 
116. Which of the following is NOT an example of ML application? 
a) Fraud detection. 
b) Spam detection. 
c) Chess playing with fixed rules only. 
d) Customer segmentation. 
Answer: c) Chess playing with fixed rules only. 
117. Q-learning is a technique used in …… 
a) Unsupervised Learning. 
b) Supervised Learning. 
c) Reinforcement Learning. 
d) Data Mining. 
Answer: c) Reinforcement Learning. 
118. ML benefits retail mainly by …… 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Robotics automation. 
b) Customer behaviour analysis and recommendations. 
c) Manufacturing. 
d) Network security. 
Answer: b) Customer behaviour analysis and recommendations. 
119. Which technique is part of unsupervised learning? 
a) Support Vector Machines. 
b) K-means clustering. 
c) Decision Trees. 
d) Reinforcement learning. 
Answer: b) K-means clustering. 
120. Which field overlaps with AI/ML but is focused on data-driven insights? 
a) Physics. 
b) Data Science. 
c) Hardware Engineering. 
d) Linguistics. 
Answer: b) Data Science. 
121. Deep Learning primarily uses …… 
a) Decision Trees. 
b) Neural Networks with many layers. 
c) Statistical methods only. 
d) Simple linear regression. 
Answer: b) Neural Networks with many layers. 
122. Deep Learning models excel at processing …… 
a) Simple numerical data only. 
b) Complex unstructured data like images and speech. 
c) Only texts. 
d) Only numerical data. 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
Answer: b) Complex unstructured data like images and speech. 
123. An advantage of Deep Learning is …… 
a) Manual feature engineering. 
b) High accuracy in complex tasks. 
c) Low computational resources needed. 
d) Easy interpretability. 
Answer: b) High accuracy in complex tasks. 
124. A big challenge in Deep Learning is …… 
a) Lack of data. 
b) Excessive interpretability. 
c) Simplicity of models. 
d) Universal understanding by humans. 
Answer: b) Excessive interpretability. 
125. GPUs are important in DL because they …… 
a) Provide more storage. 
b) Accelerate complex computations efficiently. 
c) Reduce data requirements. 
d) Produce data labels. 
Answer: b) Accelerate complex computations efficiently. 
126. What is overfitting in Deep Learning? 
a) Model performs well on new data only. 
b) Model fits training data too closely reducing generalization. 
c) Model training completed fast. 
d) Data normalization process. 
Answer: b) Model fits training data too closely reducing generalization. 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
127. Deep learning models improve with …… 
a) More data and training time. 
b) Less computational power. 
c) Fixed data only. 
d) Manual intervention in feature selection. 
Answer: a) More data and training time. 
128. Which layer in deep learning captures non-linear transformations? 
a) Input Layer 
b) Hidden Layers 
c) Output Layer 
d) Data preprocessing 
Answer: b) Hidden Layers 
129. An example of DL application in healthcare is …… 
a) Algorithmic trading. 
b) Medical image analysis. 
c) Automated marketing. 
d) Cybersecurity threat detection. 
Answer: b) Medical image analysis. 
130. Which is a disadvantage of DL models? 
a) They require minimal data. 
b) Difficult to interpret results (black-box). 
c) Easy to train on CPUs. 
d) Limited applicability. 
Answer: b) Difficult to interpret results (black-box). 
131. Neural networks are inspired by …… 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Human brain neurons 
b) Computer circuits 
c) Statistical models 
d) Logistic regression 
Answer: a) Human brain neurons 
132. The activation function in neural networks: 
a) Summarizes inputs linearly. 
b) Normalizes weights. 
c) Introduces non-linearity. 
d) Connects layers. 
Answer: c) Introduces non-linearity. 
133. The learning process in neural networks mainly involves …… 
a) manually adjusting weights. 
b) weight adjustment through backpropagation. 
c) clustering data. 
d) data labelling. 
Answer: b) weight adjustment through backpropagation. 
134. What is weighted sum in neural networks? 
a) Sum of all inputs without weights. 
b) Sum of inputs multiplied by weights. 
c) Average of output values. 
d) Total number of nodes. 
Answer: b) Sum of inputs multiplied by weights. 
135. Neural networks are widely used for …… 
a) Pattern recognition and classification. 
b) Operating systems. 
c) Hardware design. 
d) Network set-up. 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
Answer: a) Pattern recognition and classification. 
136. What is the output layer's job? 
a) Process input data. 
b) Adjust weights during training. 
c) Generate final model prediction. 
d) Store training data. 
Answer: c) Generate final model prediction. 
137. Why are neural networks sometimes called "black box" systems? 
a) Because they are simple to understand. 
b) Their internal decision processes are complex and hard to interpret. 
c) Because they use black colored hardware. 
d) They do not produce outputs. 
Answer: b) Their internal decision processes are complex and hard to interpret. 
138. Which method helps neural networks learn from error? 
a) Forward propagation. 
b) Backpropagation. 
c) Data preprocessing. 
d) Parameter tuning. 
Answer: b) Backpropagation. 
139. Layers between input and output layers are called …… 
a) Data layers. 
b) Hidden layers. 
c) Input layers. 
d) Output layers. 
Answer: b) Hidden layers. 
140. Neural networks can adapt and recognize patterns better than …… 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Rule-based systems. 
b) Linear models. 
c) Traditional programming. 
d) All of the above. 
Answer: d) All of the above. 
141. Generative AI is designed to …… 
a) Analyze but not create content 
b) Create new content from learned patterns 
c) Only classify data 
d) Run hardware operations 
Answer: b) Create new content from learned patterns 
142. Which data format is NOT used to train Generative AI? 
a) Text 
b) Images 
c) 3D signals 
d) Only numeric tables 
Answer: d) Only numeric tables 
143. The “Foundation Model” in Generative AI is …… 
a) A small lightweight model. 
b) A large neural network trained on massive diverse data. 
c) A simple decision tree. 
d) A rule-based system. 
Answer: b) A large neural network trained on massive diverse data. 
144. The self-attention mechanism in Transformers helps …… 
a) Focus on all parts of the input sequence for context. 
b) Filter irrelevant data before training. 
c) Generate random outputs. 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
d) Only translate languages. 
Answer: a) Focus on all parts of the input sequence for context. 
145. Multi-head attention means …… 
a) Running several attention layers in parallel. 
b) One attention head per sequence. 
c) Removing attention heads. 
d) Simple output generation. 
Answer: a) Running several attention layers in parallel. 
146. Positional encoding in Transformers is used because …… 
a) Transformers have no inherent sequence processing. 
b) To encode data size. 
c) To speed-up training. 
d) To eliminate tokens. 
Answer: a) Transformers have no inherent sequence processing. 
147. Which is NOT a type of Generative AI? 
a) Text generation 
b) Image generation 
c) Database management 
d) Music generation 
Answer: c) Database management 
148. An example of text generation model is …… 
a) DALL·E 
b) GPT 
c) MidJourney 
d) Jukebox 
Answer: b) GPT 
149. One application of Generative AI in finance is …… 
Mob	No	:	9326050669	/	9372072139	|	Youtube	:	@v2vedtechllp|
Insta	:	v2vedtech	|	App	Link	|	v2vedtech
V2V	EdTech	LLP	|	ETI	(CO/IT)	(316313)	|	Notes
a) Fraud detection. 
b) Automated report generation. 
c) Stock trading without AI. 
d) Network security hardware. 
Answer: b) Automated report generation. 
150. Transformer models use which processing architecture? 
a) Encoder-decoder 
b) Recurrent networks 
c) Feedforward only 
d) Clustering layers 
Answer: a) Encoder-decoder
"""

# Clean noise
lines = raw_text.split('\n')
clean_lines = []
for line in lines:
    line = line.strip()
    if not line:
        continue
    if "Mob No" in line or "Insta" in line or "V2V EdTech" in line or "Youtube" in line or "Notes" in line or "ETI" in line:
        continue
    if line.startswith("Answer:"):
        clean_lines.append(line)
    elif re.match(r'^\d+\.', line):
        clean_lines.append(line)
    elif re.match(r'^[a-d]\)', line):
        clean_lines.append(line)
    elif "Explanation:" in line:
        pass
    else:
        # maybe part of question
        pass

questions = []
current_q = None

for line in clean_lines:
    if re.match(r'^\d+\.', line):
        if current_q:
            questions.append(current_q)
        current_q = {"id": int(re.match(r'^(\d+)\.', line).group(1)), "question": re.sub(r'^\d+\.\s*', '', line), "options": [], "answer": "", "explanation": ""}
    elif re.match(r'^[a-d]\)', line) or re.match(r'^\([a-d]\)', line):
        if current_q:
            current_q["options"].append(line.strip())
    elif line.startswith("Answer:"):
        if current_q:
            ans_str = line.replace("Answer:", "").strip()
            current_q["answer"] = ans_str
    elif line.startswith("Explanation:"):
        if current_q:
            current_q["explanation"] = line.replace("Explanation:", "").strip()

if current_q:
    questions.append(current_q)

with open('src/data/questions.json', 'w') as f:
    json.dump(questions, f, indent=4)
print(f"Parsed {len(questions)} questions")
