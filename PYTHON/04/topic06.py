#44
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a == b and b == c:
    print("All are Equal")
elif a >= b and a >= c:
    if a == b:
        print("A and B are Equal and Greatest")
    elif a == c:
        print("A and C are Equal and Greatest")
    else:
        print("A is Greatest")
elif b >= a and b >= c:
    if b == c:
        print("B and C are Equal and Greatest")
    else:
        print("B is Greatest")
else:
    print("C is Greatest")


#45

marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance: "))

if attendance >= 75:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 40:
        print("Grade D")
    else:
        print("Grade F")
else:
    print("Not Eligible")


#46

salary = float(input("Enter salary: "))
rating = int(input("Enter performance rating: "))

if salary >= 30000:
    if rating == 5:
        print("Bonus: 20%")
    elif rating == 4:
        print("Bonus: 15%")
    elif rating == 3:
        print("Bonus: 10%")
    else:
        print("Bonus: 5%")
else:
    print("Not Eligible for Bonus")


#47

age = int(input("Enter age: "))
distance = float(input("Enter distance in km: "))

if age < 5:
    print("Free")
elif age <= 59:
    if distance <= 10:
        print("Regular - Short Distance")
    else:
        print("Regular - Long Distance")
else:
    print("Senior")



#48


stock = int(input("Enter product stock: "))
payment_status = input("Enter payment status: ")

if stock > 0:
    status = payment_status.strip().lower()
    
    if status == "paid":
        print("Order Confirmed")
    elif status == "pending":
        print("Payment Pending")
    else:
        print("Invalid Payment Status")
else:
    print("Out of Stock")



#49
age = int(input("Enter age: "))
ticket_type = input("Enter ticket type: ")

if age < 5:
    print("Free Travel")
elif age <= 59:
    ticket = ticket_type.strip().lower()
    
    if ticket == "ac":
        print("AC Ticket")
    elif ticket == "sleeper":
        print("Sleeper Ticket")
    else:
        print("Invalid Ticket Type")
else:
    print("Senior Passenger")




