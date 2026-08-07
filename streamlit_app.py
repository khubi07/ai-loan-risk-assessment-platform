import streamlit as st
import requests

st.set_page_config(
    page_title="Loan Risk Assessment",
    page_icon="🏦",
    layout="centered"
)

st.markdown("""
<style>

/* Main container */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:900px;
}

/* Title */
h1{
    text-align:center;
    color:#1f77b4;
    font-size:42px !important;
}

/* Subtitle */
p{
    font-size:20px !important;
}

/* Labels */
label{
    font-size:18px !important;
    font-weight:600 !important;
}

/* Input boxes */
.stSelectbox div[data-baseweb="select"],
.stNumberInput input{
    font-size:18px !important;
}

/* Button */
.stButton>button{
    width:100%;
    height:55px;
    font-size:20px;
    font-weight:bold;
    border-radius:12px;
    background-color:#1f77b4;
    color:white;
}

.stButton>button:hover{
    background-color:#145a96;
    color:white;
}

/* Metric */
[data-testid="stMetricValue"]{
    font-size:34px;
}

[data-testid="stMetricLabel"]{
    font-size:20px;
}

/* Success & Error */
.stSuccess, .stError{
    font-size:20px;
}

</style>
""", unsafe_allow_html=True)

st.title("🏦 AI Loan Risk Assessment")

st.markdown(
"""
### Predict the likelihood of a loan application being approved using a trained Machine Learning model.
"""
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male","Female"])
    married = st.selectbox("Married", ["Yes","No"])
    education = st.selectbox("Education", ["Graduate","Not Graduate"])
    applicant_income = st.number_input("Applicant Income")
    loan_term = st.number_input(
    "Loan Amount Term",
    value=360.0
)

with col2:
    dependents = st.selectbox("Dependents", ["0","1","2","3+"])
    self_employed = st.selectbox("Self Employed", ["No","Yes"])
    coapplicant_income = st.number_input("Coapplicant Income")
    credit_history = st.selectbox(
    "Credit History",
    [1,0]
)
    loan_amount = st.number_input("Loan Amount")
    property_area = st.selectbox(
    "Property Area",
    ["Urban","Semiurban","Rural"]
)



if st.button("Predict Loan Status"):
        total_income = applicant_income + coapplicant_income

        ratio = loan_amount / (total_income + 1)

        payload = {

            "Gender":1 if gender=="Male" else 0,

            "Married":1 if married=="Yes" else 0,

            "Dependents":3 if dependents=="3+" else int(dependents),

            "Education":1 if education=="Graduate" else 0,

            "Self_Employed":1 if self_employed=="Yes" else 0,

            "ApplicantIncome":applicant_income,

            "CoapplicantIncome":coapplicant_income,

            "LoanAmount":loan_amount,

            "Loan_Amount_Term":loan_term,

            "Credit_History":credit_history,

            "TotalIncome":total_income,

            "LoanToIncomeRatio":ratio,

            "Property_Area_Semiurban":1 if property_area=="Semiurban" else 0,

            "Property_Area_Urban":1 if property_area=="Urban" else 0
        }

        response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
        )

        result = response.json()       

        st.divider()

        with st.container(border=True):

            if result["prediction"] == "Approved":
                st.success("🎉 Loan Approved")

            else:
                st.error("❌ Loan Rejected")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Approval Probability",
                    f"{result['approval_probability']*100:.1f}%"
                )

            with col2:
                st.metric(
                    "Rejection Probability",
                    f"{result['rejection_probability']*100:.1f}%"
                )

            st.progress(result["approval_probability"])