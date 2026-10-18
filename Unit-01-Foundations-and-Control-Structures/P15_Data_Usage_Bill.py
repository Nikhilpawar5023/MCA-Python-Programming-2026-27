# P15 Data Bill
gb = float(input("Enter data usage in GB: "))
if gb <= 5:
    bill = 0
elif gb <= 10:
    bill = (gb-5)*100
elif gb <= 20:
    bill = 5*100 + (gb-10)*150
else:
    bill = 5*100 + 10*150 + (gb-20)*200
print("Bill =", bill)
