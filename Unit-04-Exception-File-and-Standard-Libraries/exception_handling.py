try:
    a=int(input("Enter num: "))
    print(10/a)
except ZeroDivisionError:
    print("Cannot divide by zero")