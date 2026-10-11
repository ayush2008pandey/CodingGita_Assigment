#Quedtion 7

num = int(input("enter no :"))
num_2 = int(input("enter no 2:"))
count=0 
for i in range (num,num_2+1):
    count+=i
print(count)


#question 8
N = int(input("enter no :"))
count= 0 
for i in range (1,N):
    if i%3==0:
        count+=1
print(count)


#question 9  

N = int(input("enter no: "))
count = 0
for i in range (1,N+1):
    if i%4==0:
        count+=i
print(count)


#question 10 
N = int(input("enter no :"))

count= 0 
for i in range (1,N+1):
    if i%3==0 and i%5==0:
        count+=1
print(count)


#question 11

N = int(input("enter no: "))
count = 0
for i in range (1,N+1):
    if i%3!=0:
        count+=i
print(count)


# question 12

N = int(input ("enter no :"))
even = 0
odd = 0
for i in range (1,N+1):
    if i%2==0:
        even +=1
    else:
        odd +=1 
print("even =",even)
print("odd = ",odd)



#question 13


N = int(input("enter no :"))
count = 0
for i in range (1,N+1):
    count+=i
    print(count)

#Question 14 

N = int(input("enter no :"))
count =1
for i in range (1,N+1):
    count *=i
    print(count)



