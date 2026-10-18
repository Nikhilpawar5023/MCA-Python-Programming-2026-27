# P08 Triangle
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
