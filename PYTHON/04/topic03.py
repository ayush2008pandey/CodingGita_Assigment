#question 19 

marks  = int(input("enter marks:"))
if marks>=90 and marks<=100:
    print("A")
elif marks>=80 and marks <=89:
    print("B")
elif  marks >=70 and marks<=79:
    print("C")
elif marks>=60 and marks<=69:
    print("D")
else:
    print("F")



#question 20

temp = int(input("enter temperature:"))
if temp>=40:
    print("Very Hot")
elif temp>=30 and temp<=39:
    print("Hot")
elif temp>=20 and temp<=29:
    print("Warm")
else:
    print("Cold")


#Question 21

light = int(input("enter light color :"))
light= light.lower()
if light =="red":
    print("Stop")
elif light =="yellow":
    print("Wait")
elif light =="green":
    print("Go")
else:
    print("Invalid Signal")




#question 22

unit = int(input("enter unit :"))
if unit >=0 and unit<=100:
    print("Low usage")
elif unit>=101 and unit<=300:
    print("Medium Usage")

elif unit>=301 and unit<=500:
    print("High Usage")
else:
    print("Very High Usage")



#question 23

age  = int(input("enter age :"))
if age <5:
    print("Free Ticket")
elif age>=5 and age<=12:
    print("Child Ticket")
elif age>=13 and age<=59:
    print("Regular Ticket")
else:
    print("Senoir Ticket")



#question 24

BMI = float(input("enter BMI:"))
if BMI <18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<=24.9:
    print("Normal")
elif BMI >=25 and BMI<=29.9:
    print("Overweight")
else:
    print("Obese")



#question 25

month = int(input("Enter month number: "))

if month in [1, 3, 5, 7, 8, 10, 12]:
  print("31 Days")
elif month in [4, 6, 9, 11]:
  print("30 Days")
elif month == 2:
  print("28 or 29 Days")
else:
  print("Invalid Month")




#question 26

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2)
elif op == "*":
  print(num1 * num2)
elif op == "/":
  if num2 != 0:
    print(num1 / num2)
  else:
    print("Error: Division by zero")
else:
  print("Invalid Operator")




#question 27

day = int(input("Enter day number (1-7): "))

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")
else:
  print("Invalid Day")




#question 28

score = int(input("Enter score (0-100): "))

if 90 <= score <= 100:
  print("Excellent")
elif 75 <= score <= 89:
  print("Very Good")
elif 60 <= score <= 74:
  print("Good")
elif 40 <= score <= 59:
  print("Average")
elif 0 <= score < 40:
  print("Needs Improvement")
else:
  print("Invalid Score")



