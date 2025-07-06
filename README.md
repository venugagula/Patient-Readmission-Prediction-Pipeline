# 🏥 Patient Readmission Prediction Pipeline

This project presents an end-to-end **predictive analytics pipeline** built on **AWS Glue, PySpark, and Power BI** to identify patients at high risk of hospital readmission. The pipeline processes over **50,000 daily FHIR-formatted EHR records**, transforming raw clinical data into actionable insights for healthcare teams.

### 🔍 Objective
Reduce preventable hospital readmissions using a scalable ETL and machine learning pipeline integrated with real-time reporting dashboards.

---

## 📦 Key Features

- **Data Processing (ETL)**: Built with AWS Glue and PySpark to extract, clean, and transform FHIR EHR data into structured format using Delta Lake.
- **Modeling**: Logistic Regression model trained on engineered features, with **SMOTE** applied to address class imbalance.
- **Automation**: Daily AWS Glue jobs automate risk score generation and reporting.
- **Reporting**: Power BI dashboards deliver real-time risk insights to care teams.
- **Data Quality**: Integrated **Great Expectations** for validation, ensuring high data accuracy and reliability.

---

## 🛠️ Tech Stack

- **ETL**: AWS Glue, PySpark
- **Storage**: AWS S3 (Bronze → Silver → Gold layers)
- **Machine Learning**: Logistic Regression, SMOTE (imbalanced-learn)
- **Data Quality**: Great Expectations
- **Reporting**: Power BI
- **Format**: FHIR (Fast Healthcare Interoperability Resources)

---

## ✅ Impact

- ⬇️ Reduced preventable readmissions by **28%** in pilot hospital rollout
- ⚡ Automated daily reporting, saving **10+ hours/week**
- 🎯 Achieved **83% model accuracy** with custom feature engineering

---

## 📁 Project Structure (Simplified)

