# P29 Menu Driven
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
