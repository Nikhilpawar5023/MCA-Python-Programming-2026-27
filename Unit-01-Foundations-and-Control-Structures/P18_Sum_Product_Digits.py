# P18 Sum Product of digits
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
