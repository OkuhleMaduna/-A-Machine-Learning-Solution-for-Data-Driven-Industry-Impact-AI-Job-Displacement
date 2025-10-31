# -A-Machine-Learning-Solution-for-Data-Driven-Industry-Impact-AI-Job-Displacement
📘 README: Analysing Industry Impact of AI on Employment
👩‍💻 Student Details

Name: Maduna OAU
Student Number: 22410169
Module: Machine Learning and Data Analytics
Exam Task: Task 3 — Analysing Industry Impact (Disparities/Segmentation)

🧠 Problem Definition

Artificial Intelligence (AI) and automation are transforming the global workforce.
South Africa, like many other countries, faces growing concern over job displacement, especially in industries relying on repetitive or low-skilled labour.

This project aims to:

Analyse which industries and occupations are most vulnerable to automation.

Identify which demographic groups (such as youth or low-skilled workers) are disproportionately affected.

Provide data-driven insights to support policy, reskilling, and strategic workforce planning.

🎯 Why I Chose This Task

I selected Task 3: Analysing Industry Impact because it connects machine learning with real-world socioeconomic challenges.
This task enables analysis of how AI-related technologies could deepen inequality if unaddressed, while also highlighting opportunities for targeted interventions.

It also allows me to:

Build a classification model (Random Forest) to predict automation risk.

Develop a forecasting model (Prophet) to project future risk trends across sectors.

Present findings in a Streamlit dashboard that helps policymakers, businesses, and labour unions explore data interactively.

📊 Datasets Used

Occupation Salary and Likelihood of Automation Dataset

Source: Kaggle

Contains automation probability per occupation and state-level data across the U.S.

Key Columns: Occupation, Probability, State, SOC

U.S. Employment by Industry Dataset

Source: Kaggle

Includes employment totals, mean wages, and job group classification.

Key Columns: OCC_CODE, OCC_GROUP, TOT_EMP, A_MEAN, H_MEAN

⚙️ Methods & Models

Data Cleaning & Preparation:
Datasets were inspected, missing values handled, and merged on occupation codes.

Exploratory Data Analysis (EDA):
Visualized relationships between employment levels, wages, and automation risk.

Classification Model:
Random Forest Classifier used to predict “high-risk” occupations based on automation probability thresholds.

Forecasting Model:
Prophet used to forecast automation probability trends for a selected sector (24 months).

Dashboard:
Streamlit dashboard developed for interactive exploration of results.
http://localhost:8501
💡 Key Insights

Routine and low-wage occupations show the highest automation probability.

Sectors such as retail, transport, and administration exhibit greater vulnerability.

Forecast trends indicate rising automation risk in mid-level service jobs over the next two years.
