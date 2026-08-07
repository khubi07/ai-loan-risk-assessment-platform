from pydantic import BaseModel

class LoanRequest(BaseModel):
    Gender: int
    Married: int
    Dependents: int
    Education: int
    Self_Employed: int
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    TotalIncome: float
    LoanToIncomeRatio: float
    Property_Area_Semiurban: int
    Property_Area_Urban: int