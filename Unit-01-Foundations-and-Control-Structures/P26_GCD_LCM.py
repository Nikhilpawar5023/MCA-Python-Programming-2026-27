# P26 GCD LCM
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# GCD
if a < b:
    small = a
else:
    small = b
gcd = 1
for i in range(1, small+1):
    if a%i==0 and b%i==0:
        gcd = i
lcm = (a*b)//gcd
print("GCD =", gcd)
print("LCM =", lcm)
