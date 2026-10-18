# P06 Grade
per = float(input("Enter percentage: "))
if per < 0 or per > 100:
    print("Invalid percentage")
elif per >= 90:
    print("Grade A")
elif per >= 75:
    print("Grade B")
elif per >= 60:
    print("Grade C")
elif per >= 35:
    print("Grade D")
else:
    print("Fail")
