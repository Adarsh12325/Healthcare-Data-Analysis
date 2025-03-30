import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "healthcare_survey.xlsx"  
df = pd.read_excel(file_path)

sns.set_theme(style="whitegrid")

categorical_columns = ["Gender", "Hospital_Type", "Department"]
numeric_columns = ["Satisfaction", "Wait_Time", "Cleanliness", "Staff_Behavior", "Treatment_Cost"]

import os
if not os.path.exists("charts"):
    os.makedirs("charts")

for column in categorical_columns:
    plt.figure(figsize=(6, 6))
    df[column].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, cmap="coolwarm")
    plt.title(f"Distribution of {column}", fontsize=14, fontweight="bold")
    plt.ylabel("")  
    plt.savefig(f"charts/{column}_pie_chart.png", bbox_inches='tight')
    plt.show()

for column in categorical_columns:
    plt.figure(figsize=(8, 5))
    sns.countplot(x=df[column], palette="viridis")
    plt.title(f"{column} Distribution", fontsize=14, fontweight="bold")
    plt.xlabel(column, fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.xticks(rotation=45)
    plt.savefig(f"charts/{column}_bar_chart.png", bbox_inches='tight')
    plt.show()

for column in numeric_columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], bins=10, kde=True, color="purple")
    plt.title(f"Histogram of {column}", fontsize=14, fontweight="bold")
    plt.xlabel(column, fontsize=12)
    plt.ylabel("Number of Patients", fontsize=12)
    plt.savefig(f"charts/{column}_histogram.png", bbox_inches='tight')
    plt.show()

print("All charts saved successfully in the 'charts' folder!")
