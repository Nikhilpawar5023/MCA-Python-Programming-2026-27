# P02 Employee Salary
basic = float(input("Enter basic salary: "))
da = basic * 10 / 100
hra = basic * 15 / 100
gross = basic + da + hra
if gross > 50000:
    tax = gross * 5 / 100
else:
    tax = 0
net = gross - tax
print("DA =", da)
print("HRA =", hra)
print("Gross =", gross)
print("Tax =", tax)
print("Net Salary =", net)
