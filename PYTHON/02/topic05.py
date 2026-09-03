# Question 45 — String Numbers
price = "1200"
quantity = "4"
p_int = int(price)
q_int = int(quantity)
print("Price:", p_int)
print("Quantity:", q_int)
print("Total Price:", p_int * q_int)



# Question 46 — Student Result


python_marks = "85"
math_marks = "78"
physics_marks = "91"
tot = int(python_marks) + int(math_marks) + int(physics_marks)
print("Total Marks:", tot)
print("Average Marks:", tot / 3)



# Question 47 — Bill with Tax



price = "1500"
quantity = "2"
tax_rate = "5"
subtotal = float(price) * int(quantity)
tax_amount = subtotal * (float(tax_rate) / 100)
print("Subtotal:", subtotal)
print("Tax Amount:", tax_amount)
print("Final Bill:", subtotal + tax_amount)



# Question 48 — Discount + GST


cost = 2000
disc_amount = cost * 0.15
price_after_disc = cost - disc_amount
gst_amount = price_after_disc * 0.18
final_price = price_after_disc + gst_amount
print("Discount Amount:", disc_amount)
print("Price after Discount:", price_after_disc)
print("GST Amount:", gst_amount)
print("Final Price:", final_price)



# Question 49 — Debug the Billing Program


price = "500"
quantity = 3
total = int(price) * quantity
print("Total:", total)





# Question 50 — Debug the Marks Program
marks1 = "80"
marks2 = "75"
marks3 = "90"
total = int(marks1) + int(marks2) + int(marks3)
print("Total Marks:", total)