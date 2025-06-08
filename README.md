
# LLM-Centric Challenges in Deep Learning Frameworks
This repo is for the paper of `Understanding LLM-Centric Challenges in Deep Learning Frameworks: An Empirical Analysis`.

This repository contains a series of documents and materials related to our research. Below is a detailed description of the main files in the repository:

## List of Files
1. `Issue Report`

    Description: This fold stores the collected and filtered LLM-related issue Reports. In the folder of each deep learning framework and their LLM toolkits, we present all the issue links from 2023-2025 in each `.txt` file (e.g., ColossalAI_2023.txt) and present all the labeled results of seven volunteers in the `.csv` file  (e.g., ColossalAI.csv) which is named by deep learning framework or LLM toolkits. Besides, we also present the code for calculating  kappa (i.e., kappa.py). Finally, we further present the detail information of the taxonomy, i.e., the symptoms for bug  categories  (i.e.,  bug_symptoms.csv), the question intents for question categories (i.e.,  question_intents.csv), and detailed expectations for requirement categories  (i.e.,  requirement_expections.csv), which can help readers understand but is not included in our taxonomy. 

    Issue Report  
    ├── bug_symptoms.csv  
    ├── kappa.py  
    ├── question_intents.csv  
    ├── requirement_expections.csv  
    ├── ColossalAI   
    │   ├── ColossalAI.csv  
    │   ├── ColossalAI_2023.txt  
    │   ├── ColossalAI_2024.txt  
    │   └── ColossalAI_2025.txt  
    ├── DeepSpeed
    ├── Megatron-LM  
    ├── mindformers   
    ├── mindnlp   
    ├── MindSpeed  
    ├── mindspore  
    ├── pytorch   
    ├── tensorflow   
    ├── TensorRT-LLM 
    └── vllm  

2. `Interviewee Background.xlsx`
    Description: This file introduces the details of the interviewees including the roles, gender, experienced years for using LLMs or developer DL frameworks, and the specific duties related to LLMs.

3. `Interview GuideLine.md`
    Description: This file is structured into four parts and covers participants’ backgrounds, usability questions, bug-related issues, and desired framework improvements. The guide supports validating and extending a taxonomy of LLM-related challenges in DL frameworks through semi-structured, 30–40 minute interviews.

4. `filter_keywords`
    Description: This file stores the keywords for selecting LLM-related issue reports from the three deep learning frameworks, i.e., MindSpore, PyTorch, and TensorFlow as introduced in Section III.A. 

5. `CodeBook.csv`
    Description: This file is an Excel spreadsheet that summarizes interview findings from both LLM users and deep learning framework developers, focusing on challenges related to LLM development. Each entry includes participant type, experience level, framework context, a key quote, linked taxonomy categories, and synthesized research insights. The data supports analysis of common pain points, framework bugs, and unmet needs in LLM workflows.

