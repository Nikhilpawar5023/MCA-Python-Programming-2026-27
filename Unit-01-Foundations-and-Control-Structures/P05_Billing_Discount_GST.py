# P05 Billing
print("Enter 3 items")
p1 = float(input("Price 1: "))
q1 = int(input("Qty 1: "))
p2 = float(input("Price 2: "))
q2 = int(input("Qty 2: "))
p3 = float(input("Price 3: "))
q3 = int(input("Qty 3: "))
subtotal = p1*q1 + p2*q2 + p3*q3
if subtotal > 1000:
    discount = subtotal * 0.10
else:
    discount = 0
after_disc = subtotal - discount
gst = after_disc * 0.18
total = after_disc + gst
print("Subtotal", subtotal)
print("Discount", discount)
print("GST", gst)
print("Total Payable", total)
