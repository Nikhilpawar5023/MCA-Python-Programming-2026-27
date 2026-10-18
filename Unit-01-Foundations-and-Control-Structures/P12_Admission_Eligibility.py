# P12 Admission
maths = float(input("Enter maths marks: "))
physics = float(input("Enter physics marks: "))
chem = float(input("Enter chemistry marks: "))
avg = (maths+physics+chem)/3
if maths>=60 and physics>=50 and chem>=50 and avg>=60:
    print("Eligible for Admission")
else:
    print("Not Eligible")
