#question - 33
text = "Python is easy"

print(text.split())
#["Python","is","easy"]

#question - 34

data = "apple,banana,mango"

print(data.split(","))

# ['apple', 'banana', 'mango']


#question - 35

text = "Python is easy"

print(text.split(","))
#['Python is easy']

#question - 36

name,middle_name,surname = "Rahul Kumaar Sharma".split()
print(name)
print(middle_name)
print(surname)


#question - 37

first_name,last_name="Rahul Kumar".split()
print("fisrt_name:",first_name)
print("last_name: ",last_name)


#question - 38
num_1,num_2,num_3=input("enter no: ").split()
add = int(num_1)+int(num_2)+int(num_3)
print(add)

#question - 39

name,age,course,city="Rahul,20,BTech,Ahmedabad".split(",")
print("Name:",name)
print("Age:",age)
print("Course:",course)
print("City:",city)

#question - 40

username,domain=input("enter email").split()
print("Username:",username)
print("Domain:",domain)


#Question - 41

first,second,third,last=input("enter sentence").split()
print("first word",first)
print("Last word",last)


