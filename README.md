# 🏦 AI Loan Risk Assessment Platform

An end-to-end Machine Learning application that predicts whether a loan application is likely to be approved based on applicant and loan details.

The project covers the complete ML workflow—from data analysis and model training to serving predictions through a FastAPI backend and an interactive Streamlit frontend.

---

## 📸 Screenshots

### Streamlit UI
> *(Add screenshot here)*

![Streamlit UI](screenshots/streamlit-ui.png)

---

### Prediction Result
> *(Add screenshot here)*

![Prediction](screenshots/prediction-result.png)

---

### FastAPI Swagger Docs
> *(Add screenshot here)*

![Swagger](screenshots/swagger-docs.png)

---

## ✨ Features

- Exploratory Data Analysis (EDA)
- Data preprocessing & feature engineering
- Multiple ML models comparison
- Random Forest as the final model
- FastAPI REST API
- Interactive Streamlit UI
- Real-time loan prediction with confidence scores

---

## 🛠️ Tech Stack

**Machine Learning**
- Python
- Pandas
- NumPy
- Scikit-learn

**Backend**
- FastAPI
- Uvicorn

**Frontend**
- Streamlit

**Visualization**
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```text
ai-loan-risk-assessment-platform/
│
├── app/
│   ├── main.py
│   ├── model.py
│   └── schema.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── loan_model.pkl
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_model_training.ipynb
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone <your-repository-link>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start FastAPI

```bash
uvicorn app.main:app --reload
```

Start Streamlit

```bash
streamlit run streamlit_app.py
```

---

## 📊 Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | **86.18%** |
| Decision Tree | **73.17%** |
| **Random Forest** | **88.62%** ✅ |

Random Forest was selected as the final model due to its best overall performance.

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/predict` | Predict loan approval |

---

## 👩‍💻 Author

**Khubi Sahu**

GitHub: https://github.com/<your-github-username>

LinkedIn: https://linkedin.com/in/<your-linkedin>