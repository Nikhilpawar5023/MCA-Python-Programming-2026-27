# P10 Number properties
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
