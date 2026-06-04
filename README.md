# 🏥 Insurance Premium Predictor

An end-to-end Machine Learning project that predicts medical insurance charges based on demographic and health-related features.

The project demonstrates the complete Machine Learning lifecycle:

* Data Collection
* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model Training
* Model Evaluation
* Streamlit Deployment

---

## 🚀 Live Application

🌐 Streamlit App:

https://insurance-premium-predictor-grdji9lwwoz8bjkswuqesy.streamlit.app

---

## 📂 Dataset

Dataset Used:

**Medical Cost Personal Dataset** by Miri Choi

Kaggle Dataset:
https://www.kaggle.com/datasets/mirichoi0218/insurance

The dataset contains **1,338 records** and **7 features** related to health insurance charges, including age, gender, BMI, smoking status, number of children, and region. The target variable is medical insurance charges.

### Features

| Feature  | Description                              |
| -------- | ---------------------------------------- |
| age      | Age of the primary beneficiary           |
| sex      | Gender of beneficiary                    |
| bmi      | Body Mass Index                          |
| children | Number of dependents                     |
| smoker   | Smoking status                           |
| region   | Residential region                       |
| charges  | Medical insurance cost (Target Variable) |

---

## 🎯 Problem Statement

Build a regression model capable of predicting an individual's medical insurance charges using demographic and lifestyle information.

This is a **Supervised Machine Learning Regression Problem**.

---

## 🛠️ Tech Stack

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* Pickle

---

## 📊 Project Workflow

### 1️⃣ Data Collection

* Imported dataset from Kaggle
* Loaded data using Pandas

### 2️⃣ Data Cleaning

* Checked missing values
* Verified data types
* Removed inconsistencies

### 3️⃣ Exploratory Data Analysis (EDA)

* Univariate Analysis
* Bivariate Analysis
* Correlation Analysis
* Outlier Detection
* Feature Distribution Analysis

### 4️⃣ Feature Engineering

* Label Encoding
* Feature Scaling using StandardScaler
* Train-Test Split

### 5️⃣ Model Building

Implemented:

* Linear Regression

### 6️⃣ Model Evaluation

Metrics Used:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

### 7️⃣ Deployment

Developed an interactive web application using Streamlit for real-time insurance premium prediction.

---

## 📁 Project Structure

```bash
Insurance-Premium-Predictor/
│
├── app.py
├── requirements.txt
├── README.md
│
├── Models/
│   ├── linear.pkl
│   └── scaler.pkl
│
├── notebook/
│   └── Insurance_Prediction.ipynb
│
└── dataset/
    └── insurance.csv
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Dhruvit-Jalodhara/Insurance-Premium-Predictor.git
cd Insurance-Premium-Predictor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📸 Application Preview

Add screenshots after deployment.

### Home Page

![Home Page](Screenshot 2026-06-04 at 6.56.24 PM.png)

### Prediction Result

![Prediction Result](images/prediction.png)

---

## 📈 Future Improvements

* Ridge Regression
* Lasso Regression
* Elastic Net Regression
* Random Forest Regressor
* XGBoost Regressor
* Hyperparameter Tuning
* Docker Deployment
* CI/CD Pipeline

---

## 🔗 Project Links

### GitHub Repository

https://github.com/Dhruvit-Jalodhara/Insurance-Premium-Predictor

### LinkedIn

https://www.linkedin.com/in/dhruvit-jalodhara

### Streamlit Deployment

https://insurance-premium-predictor-grdji9lwwoz8bjkswuqesy.streamlit.app

---

## 👨‍💻 Author

**Dhruvit Jalodhara**

AI Engineering Student | Machine Learning Enthusiast

Currently learning:

* Machine Learning
* Deep Learning
* Data Structures & Algorithms
* AI Engineering

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
