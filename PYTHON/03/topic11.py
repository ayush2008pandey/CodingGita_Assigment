#question - 60 
name = input("enter name:")
physics = int(input("enter physics marks:"))
maths = int(input("enter maths marks:"))
python = int(input("enter python marks:"))

total = physics+maths+python
average = total/3
print("Name:",name)
print("Total:",total)
print("Average:",average)


#Question - 61
ID = input("enter id:").split()
Degree,Batch,Branch,Roll_number=ID
print(f"\nDegree:{Degree}\nBatch:{Batch}\nBranch:{Branch}\nRoll Number:{int(Roll_number)}")


#question - 62
full_name = input()
words = full_name.split()
username = words[0].lower() + "." + words[2].lower()
print(username)


#question - 63

take = "Python is very powerful".split()
first,second,third,last=take
print("first word:",first)
print("last word:",last)
print(take[:6])
print(take[-8:])

#Question - 64

email = input()


at_present = "@" in email
print(f"@ Present: {at_present}")


parts = email.split("@")
print(f"Username: {parts[0]}")
print(f"Domain: {parts[1]}")

#question - 65
char = input()
code = ord(char)
print(f"Character: {char}")
print(f"Code: {code}")
print(f"Previous: {chr(code - 1)}")
print(f"Next: {chr(code + 1)}")


#question - 66
product_name = input()
price = float(input())
quantity = int(input())
discount_percentage = float(input())

subtotal = price * quantity
discount = subtotal * discount_percentage / 100
final_total = subtotal - discount

print(f"Product: {product_name}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Total: {final_total:.2f}")


#question - 67


date_str = "09-09-2026"


day, month, year = date_str.split("-")

print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")


extracted_year = date_str[6:]
print(extracted_year)

#question - 68


text = "Python Programming"

words = text.split()
first_word = words[0]
second_word = words[1]


print(f"First Word: {first_word}")
print(f"Second Word: {second_word}")

first_word_rev = first_word[::-1]
second_word_rev = second_word[::-1]


print(f"First Word Reversed: {first_word_rev}")
print(f"Second Word Reversed: {second_word_rev}")


#Question - 69


student_id = "BTECH-2026-CSE-105"


parts = student_id.split("-")

degree = parts[0]
batch = parts[1]
branch = parts[2]
roll = parts[3]


print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll: {roll}")

code = f"{degree[:]}/{branch[:]}/{roll[:]}"
print(f"Code: {code}")


#Question - 70


full_name = input("Enter full name: ")

words = full_name.split()


first_name = words[0]
last_name = words[-1]


first_upper_part = first_name[:3].upper()
last_lower_part = last_name[1:4]

reversed_name = full_name[::-1]

print(f"Original: {full_name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"First Name (Upper Part): {first_upper_part}")
print(f"Last Name (Lower Part): {last_lower_part}")
print(f"Full Name Reversed: {reversed_name}")