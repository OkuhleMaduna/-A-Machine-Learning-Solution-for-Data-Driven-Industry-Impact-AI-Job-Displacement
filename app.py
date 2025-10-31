import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("AI/Automation Impact Dashboard")
st.markdown("Upload your datasets here. Supported formats: CSV or Excel.")

uploaded_files = st.file_uploader(
    "Choose your datasets (upload one at a time)",
    type=['csv', 'xlsx'],
    accept_multiple_files=True
)

dfs = {}
if uploaded_files:
    for file in uploaded_files:
        try:
            if file.name.endswith('.csv'):
                try:
                    df = pd.read_csv(file, encoding='utf-8')
                except UnicodeDecodeError:
                    try:
                        df = pd.read_csv(file, encoding='latin1')
                    except UnicodeDecodeError:
                        df = pd.read_csv(file, encoding='ISO-8859-1')
            else:
                df = pd.read_excel(file)
            
            dfs[file.name] = df
            st.success(f"Loaded {file.name} successfully!")
            st.write(f"Preview of {file.name}:")
            st.dataframe(df.head())
            st.write(f"Columns in {file.name}: {df.columns.tolist()}")
            
        except Exception as e:
            st.error(f"Failed to load {file.name}: {e}")

if 'automation_probability.csv' in dfs:
    auto_df = dfs['automation_probability.csv']
    if 'Probability' in auto_df.columns:
        st.subheader("Automation Probability Distribution")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(auto_df['Probability'], bins=20, ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Column 'Probability' not found in automation dataset.")

if 'occupation_salary.xlsx' in dfs:
    sal_df = dfs['occupation_salary.xlsx']
    numeric_cols = sal_df.select_dtypes(include='number').columns.tolist()
    if numeric_cols:
        st.subheader("Salary Statistics")
        st.dataframe(sal_df[numeric_cols].describe())
    else:
        st.warning("No numeric columns found in salary dataset.")