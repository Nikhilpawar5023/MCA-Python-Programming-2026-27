# P20 Armstrong
n = int(input("Enter number: "))
temp = n
# count digits
c = len(str(n))
sum = 0
while temp > 0:
    d = temp % 10
    sum = sum + d**c
    temp = temp // 10
if sum == n:
    print("Armstrong Number")
else:
    print("Not Armstrong")
