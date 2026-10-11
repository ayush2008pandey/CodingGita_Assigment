#question 15

N = int(input("enter no :"))
count = 1
for i in range(N):
    count*=i
print(count)

#question 16

N = int(input("enter no :"))
count =1
for i in range(1,N+1):
    count *=i
    print(f"{i}i = {count}")


#question 17

N = int (input("enter no :"))
count = 1
for i in range (2,N+1):
    if i%2==0:
        count *=i
print(count)


#Question 18

N = int(input("enter no :"))
count =1
for i in range (1,N+1):
    if i%2!=0:
        count *=i
print(count)




#question 19 
N = int(input("enter no :"))
result = 1

for i in range(N, 0, -2):
    result *= i

print(result)  


#question 20 

N= int(input("enter no :"))
count = 0
for i in range (1,N+1):
    count +=i**2
print(count)


#question 21


N= int(input("enter no :"))
count = 0
for i in range (1,N+1):
    count +=i**3
print(count)


#question 22 

N  = int(input("enter no :"))
count = 0
real  = 1
for i in range (1,N+1):
    real *=i
    count +=real
print(count)



