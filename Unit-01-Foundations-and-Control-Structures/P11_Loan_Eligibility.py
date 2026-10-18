# P11 Loan Eligibility
age = int(input("Enter age: "))
income = float(input("Enter income: "))
score = int(input("Enter credit score: "))
if age >= 21 and age <= 60:
    if income >= 25000 and score >= 700:
        print("Eligible for Loan")
    else:
        print("Not Eligible")
else:
    print("Not Eligible - Age criteria failed")
