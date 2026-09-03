# Question 56 — Debug the Student Program

student_name = "Ravi"
marks = "85"

total = int(marks) + 5

print("Student:", student_name)
print("Marks:", total)
print("Type:", type(total))


# Question 57 — Debug the Number Program

number = 746

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

print("Ones:", ones)
print("Tens:", tens)
print("Hundreds:", hundreds)


# Question 58 — Debug the Discount Program

price = "2000"
discount = "15"

price_num = float(price)
discount_num = float(discount)

discount_amount = (price_num * discount_num) / 100
final_price = price_num - discount_amount

print("Discount:", discount_amount)
print("Final Price:", final_price)


# Question 59 — Complete Debugging Challenge

student_name = "Rahul"
marks1 = "85"
marks2 = "90"
marks3 = "78"

total = int(marks1) + int(marks2) + int(marks3)
average = total / 3

print("Student:", student_name)
print("Total Marks:", total)
print("Average:", average)
print("Marks Type:", type(total))


# Question 60 — Final Challenge: Number + Billing

# Part A — Number Analysis
number = 5836

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10

sum_of_digits = thousands + hundreds + tens + ones
reversed_number = (ones * 1000) + (tens * 100) + (hundreds * 10) + thousands

print("Thousands Digit:", thousands)
print("Hundreds Digit:", hundreds)
print("Tens Digit:", tens)
print("Ones Digit:", ones)
print("Sum of Digits:", sum_of_digits)
print("Reversed Number:", reversed_number)



# Part B — Product Billing



price = "1250"
quantity = "4"
discount = "10"

price_num = float(price)
quantity_num = int(quantity)
discount_num = float(discount)

subtotal = price_num * quantity_num
discount_amount = subtotal * (discount_num / 100)
final_amount = subtotal - discount_amount

print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)