# P23 Prime in Range
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
print("\nTotal prime count =", count)
