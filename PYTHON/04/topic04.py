#question 29

marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))

if marks >= 60 and attendance >= 75:
  print("Eligible")
else:
  print("Not Eligible")



#question 30

marks = float(input("Enter marks: "))
income = float(input("Enter family income: "))

if marks >= 85 or income < 300000:
  print("Scholarship Available")
else:
  print("No Scholarship")


  #question 31

day = input("Enter day name: ").strip().title()

if day in ["Saturday", "Sunday"]:
  print("Weekend")
else:
  print("Weekday")



#question 32

username = input("Enter username: ")
password = input("Enter password: ")

if username == "student" and password == "python123":
  print("Access Granted")
else:
  print("Access Denied")



#question 33


city = input("Enter city name: ").strip().title()

if city in ["Ahmedabad", "Gandhinagar"]:
  print("Delivery Available")
else:
  print("Delivery Unavailable")

#question 34


num = int(input("Enter an integer: "))

if 10 <= num <= 50:
  print("Inside Range")
else:
  print("Outside Range")



  #question 35

amount = float(input("Enter amount: "))
otp = input("Enter OTP: ")

if amount <= 50000 and otp == "1234":
  print("Transaction Approved")
else:
  print("Transaction Declined")