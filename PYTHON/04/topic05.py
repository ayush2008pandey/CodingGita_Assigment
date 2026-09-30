#Question 36


username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
  if password == "admin123":
    print("Login Successful")
  else:
    print("Wrong Password")
else:
  print("Invalid Username")



  #question 37


age = int(input("Enter age: "))
test_status = input("Enter test status (pass/fail): ").strip().lower()

if age >= 18:
  if test_status == "pass":
    print("License Approved")
  else:
    print("Test Not Passed")
else:
  print("Age Not Eligible")


#question 38

balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount <= balance:
  if amount % 100 == 0:
    print("Withdrawal Successful")
  else:
    print("Amount must be a multiple of 100")
else:
  print("Insufficient Balance")



#question 39


attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter marks: "))

if attendance >= 75:
  if marks >= 40:
    print("Pass")
  else:
    print("Fail")
else:
  print("Not Eligible Due to Attendance")


#questiom 40


account_type = input("Enter account type: ").strip().lower()
balance = float(input("Enter account balance: "))

if account_type == "savings":
  if balance >= 1000:
    print("Minimum Balance Maintained")
  else:
    print("Minimum Balance Not Maintained")
else:
  print("Not a Savings Account")


#question 41


order_amount = float(input("Enter order amount: "))
payment_method = input("Enter payment method (card/upi/etc.): ")

if order_amount >= 500:
    method = payment_method.strip().lower()
    
    if method == "card":
        print("Card Payment Accepted")
    elif method == "upi":
        print("UPI Payment Accepted")
    else:
        print("Unsupported Payment Method")
else:
    print("Minimum Order Amount Not Reached")


#question 42


year = int(input("Enter year of study: "))
attendance = float(input("Enter attendance: "))

if year == 2 or year == 3 or year == 4:
    if attendance >= 75:
        print("Room Eligible")
    else:
        print("Attendance Too Low")
else:
    print("Not Eligible by Year")


#question 43

current_plan = input("Enter current plan: ")
monthly_usage = float(input("Enter monthly usage (in GB): "))

if current_plan.strip().lower() == "basic":
    if monthly_usage > 100:
        print("Recommend Upgrade")
    else:
        print("Basic Plan Is Sufficient")
else:
    print("Already on Higher Plan")




