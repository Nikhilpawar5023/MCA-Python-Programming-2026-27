# P30 Class Statistics
n = int(input("Enter number of students: "))
marks = []
for i in range(n):
    m = float(input(f"Enter marks of student {i+1}: "))
    marks.append(m)
total = sum(marks)
avg = total / n
max_m = max(marks)
min_m = min(marks)
passed = 0
above75 = 0
for m in marks:
    if m >= 35:
        passed = passed + 1
    if m >= 75:
        above75 = above75 + 1
print("Average =", avg)
print("Highest =", max_m)
print("Lowest =", min_m)
print("Passed =", passed)
print("Above 75 =", above75)
