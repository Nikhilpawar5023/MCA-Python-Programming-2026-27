# P19 Digit Analysis
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
