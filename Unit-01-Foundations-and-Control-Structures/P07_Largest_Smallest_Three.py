# P07 Largest Smallest
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
