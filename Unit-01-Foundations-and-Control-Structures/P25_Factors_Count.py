# P25 Factors
n = int(input("Enter number: "))
print("Factors are:")
count = 0
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
        count = count + 1
print("\nTotal factors =", count)
