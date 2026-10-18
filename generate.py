import os
base = "Unit-01-Foundations-and-Control-Structures"
os.makedirs(base, exist_ok=True)

codes = {}

codes["P01_Total_Average_Percentage.py"] = '''# Name: Nikhil Pawar - Roll No: - P01
# Total, Average, Percentage of 5 subjects
print("Enter marks of 5 subjects")
s1 = int(input("Subject 1: "))
s2 = int(input("Subject 2: "))
s3 = int(input("Subject 3: "))
s4 = int(input("Subject 4: "))
s5 = int(input("Subject 5: "))
total = s1+s2+s3+s4+s5
avg = total/5
per = total/5
print("Total =", total)
print("Average =", avg)
print("Percentage =", per)
'''

codes["P02_Employee_Salary.py"] = '''# P02 Employee Salary
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
'''

codes["P03_Electricity_Bill.py"] = '''# P03 Electricity Bill
units = int(input("Enter units: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100*5 + (units-100)*7
else:
    bill = 100*5 + 100*7 + (units-200)*10
print("Bill is", bill)
'''

codes["P04_Seconds_Conversion.py"] = '''# P04 Seconds to hr min sec
sec = int(input("Enter seconds: "))
hours = sec // 3600
sec = sec % 3600
minutes = sec // 60
seconds = sec % 60
print(hours, "hours", minutes, "minutes", seconds, "seconds")
'''

codes["P05_Billing_Discount_GST.py"] = '''# P05 Billing
print("Enter 3 items")
p1 = float(input("Price 1: "))
q1 = int(input("Qty 1: "))
p2 = float(input("Price 2: "))
q2 = int(input("Qty 2: "))
p3 = float(input("Price 3: "))
q3 = int(input("Qty 3: "))
subtotal = p1*q1 + p2*q2 + p3*q3
if subtotal > 1000:
    discount = subtotal * 0.10
else:
    discount = 0
after_disc = subtotal - discount
gst = after_disc * 0.18
total = after_disc + gst
print("Subtotal", subtotal)
print("Discount", discount)
print("GST", gst)
print("Total Payable", total)
'''

codes["P06_Grade_System.py"] = '''# P06 Grade
per = float(input("Enter percentage: "))
if per < 0 or per > 100:
    print("Invalid percentage")
elif per >= 90:
    print("Grade A")
elif per >= 75:
    print("Grade B")
elif per >= 60:
    print("Grade C")
elif per >= 35:
    print("Grade D")
else:
    print("Fail")
'''

codes["P07_Largest_Smallest_Three.py"] = '''# P07 Largest Smallest
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a>b and a>c:
    print("Largest is", a)
elif b>a and b>c:
    print("Largest is", b)
else:
    print("Largest is", c)

if a<b and a<c:
    print("Smallest is", a)
elif b<a and b<c:
    print("Smallest is", b)
else:
    print("Smallest is", c)
'''

codes["P08_Triangle_Validator.py"] = '''# P08 Triangle
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if a+b>c and b+c>a and a+c>b:
    print("Triangle is valid")
    if a==b and b==c:
        print("Equilateral")
    elif a==b or b==c or a==c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid Triangle")
'''

codes["P09_Leap_Year.py"] = '''# P09 Leap Year
year = int(input("Enter year: "))
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")
'''

codes["P10_Number_Properties.py"] = '''# P10 Number properties
n = int(input("Enter number: "))
if n == 0:
    print("Number is Zero")
else:
    if n > 0:
        print("Positive")
    else:
        print("Negative")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
'''

codes["P11_Loan_Eligibility.py"] = '''# P11 Loan Eligibility
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
'''

codes["P12_Admission_Eligibility.py"] = '''# P12 Admission
maths = float(input("Enter maths marks: "))
physics = float(input("Enter physics marks: "))
chem = float(input("Enter chemistry marks: "))
avg = (maths+physics+chem)/3
if maths>=60 and physics>=50 and chem>=50 and avg>=60:
    print("Eligible for Admission")
else:
    print("Not Eligible")
'''

codes["P13_ATM_Simulation.py"] = '''# P13 ATM
pin = 1234
balance = 10000
user_pin = int(input("Enter PIN: "))
if user_pin == pin:
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance = balance - amount
        print("Withdraw Success")
        print("Remaining balance", balance)
    else:
        print("Insufficient Balance")
else:
    print("Invalid PIN")
'''

codes["P14_Income_Tax.py"] = '''# P14 Income Tax
income = float(input("Enter annual income: "))
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income-250000)*0.05
elif income <= 1000000:
    tax = 12500 + (income-500000)*0.20
else:
    tax = 112500 + (income-1000000)*0.30
print("Tax =", tax)
'''

codes["P15_Data_Usage_Bill.py"] = '''# P15 Data Bill
gb = float(input("Enter data usage in GB: "))
if gb <= 5:
    bill = 0
elif gb <= 10:
    bill = (gb-5)*100
elif gb <= 20:
    bill = 5*100 + (gb-10)*150
else:
    bill = 5*100 + 10*150 + (gb-20)*200
print("Bill =", bill)
'''

codes["P16_Reverse_Number.py"] = '''# P16 Reverse Number
n = int(input("Enter number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev*10 + digit
    n = n // 10
print("Reverse =", rev)
'''

codes["P17_Palindrome_Number.py"] = '''# P17 Palindrome
n = int(input("Enter number: "))
temp = n
rev = 0
while temp > 0:
    rev = rev*10 + temp%10
    temp = temp//10
if rev == n:
    print("Palindrome")
else:
    print("Not Palindrome")
'''

codes["P18_Sum_Product_Digits.py"] = '''# P18 Sum Product of digits
n = int(input("Enter number: "))
s = 0
p = 1
while n > 0:
    d = n % 10
    s = s + d
    p = p * d
    n = n // 10
print("Sum =", s)
print("Product =", p)
'''

codes["P19_Digit_Analysis.py"] = '''# P19 Digit Analysis
n = int(input("Enter number: "))
count = 0
large = 0
small = 9
temp = n
while temp > 0:
    d = temp % 10
    count = count + 1
    if d > large:
        large = d
    if d < small:
        small = d
    temp = temp // 10
print("Count =", count)
print("Largest digit =", large)
print("Smallest digit =", small)
'''

codes["P20_Armstrong_Number.py"] = '''# P20 Armstrong
n = int(input("Enter number: "))
temp = n
# count digits
c = len(str(n))
sum = 0
while temp > 0:
    d = temp % 10
    sum = sum + d**c
    temp = temp // 10
if sum == n:
    print("Armstrong Number")
else:
    print("Not Armstrong")
'''

codes["P21_Number_Guessing_Game.py"] = '''# P21 Guessing Game
import random
secret = random.randint(1, 100)
print("Guess number between 1 to 100")
while True:
    guess = int(input("Enter your guess: "))
    if guess == secret:
        print("Correct! You guessed it")
        break
    elif guess < secret:
        print("Too Low")
    else:
        print("Too High")
'''

codes["P22_Prime_Check.py"] = '''# P22 Prime Check
n = int(input("Enter number: "))
if n <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
'''

codes["P23_Prime_Range.py"] = '''# P23 Prime in Range
a = int(input("Enter start: "))
b = int(input("Enter end: "))
count = 0
for num in range(a, b+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
            count = count + 1
print("\\nTotal prime count =", count)
'''

codes["P24_Fibonacci_Series.py"] = '''# P24 Fibonacci
n = int(input("Enter number of terms: "))
a = 0
b = 1
sum = 0
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    sum = sum + a
    c = a + b
    a = b
    b = c
print("\\nSum =", sum)
'''

codes["P25_Factors_Count.py"] = '''# P25 Factors
n = int(input("Enter number: "))
print("Factors are:")
count = 0
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
        count = count + 1
print("\\nTotal factors =", count)
'''

codes["P26_GCD_LCM.py"] = '''# P26 GCD LCM
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# GCD
if a < b:
    small = a
else:
    small = b
gcd = 1
for i in range(1, small+1):
    if a%i==0 and b%i==0:
        gcd = i
lcm = (a*b)//gcd
print("GCD =", gcd)
print("LCM =", lcm)
'''

codes["P27_Multiplication_Tables.py"] = '''# P27 Tables 1 to 10
for i in range(1, 11):
    print("Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print("")
'''

codes["P28_Number_Pattern.py"] = '''# P28 Pattern
n = int(input("Enter rows: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
'''

codes["P29_Menu_Driven_Maths.py"] = '''# P29 Menu Driven
while True:
    print("1. Prime Check")
    print("2. Palindrome")
    print("3. Armstrong")
    print("4. Factorial")
    print("5. Fibonacci")
    print("6. Exit")
    ch = int(input("Enter choice: "))
    if ch == 6:
        print("Exit")
        break
    num = int(input("Enter number: "))
    if ch == 1:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    print("Not Prime")
                    break
            else:
                print("Prime")
        else:
            print("Not Prime")
    elif ch == 2:
        if str(num) == str(num)[::-1]:
            print("Palindrome")
        else:
            print("Not Palindrome")
    elif ch == 3:
        s = sum(int(d)**len(str(num)) for d in str(num))
        if s == num:
            print("Armstrong")
        else:
            print("Not Armstrong")
    elif ch == 4:
        fact = 1
        for i in range(1, num+1):
            fact = fact * i
        print("Factorial =", fact)
    elif ch == 5:
        a=0
        b=1
        for i in range(num):
            print(a, end=" ")
            c=a+b
            a=b
            b=c
        print()
'''

codes["P30_Class_Statistics.py"] = '''# P30 Class Statistics
n = int(input("Enter number of students: "))
marks = []
for i in range(n):
    m = float(input(f"Enter marks of student {i+1}: "))
    marks.append(m)
total = sum(marks)
avg = total / n
max_m = max(marks)
min_m = min(marks)
passed = 0
above75 = 0
for m in marks:
    if m >= 35:
        passed = passed + 1
    if m >= 75:
        above75 = above75 + 1
print("Average =", avg)
print("Highest =", max_m)
print("Lowest =", min_m)
print("Passed =", passed)
print("Above 75 =", above75)
'''

for name, code in codes.items():
    with open(os.path.join(base, name), "w", encoding="utf-8") as f:
        f.write(code)

print(f"Done! Created {len(codes)} files - Simple student style")