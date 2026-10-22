import math

#question 23
N = int(input("enter no "))
count = 0

for count in range(1, N+1):
    N //= 10
    if N == 0:
        break

print(count)  


#QUESTION 24

num = int(input("Enter number: "))

digit_sum = 0
for digit in str(abs(num)):
    digit_sum += int(digit)

print(digit_sum)

#question 25

integer = int(input("enter no :"))
count = 1 
for i in  str(abs(integer)):
    count *=int(i) 
print(count)


#question 26


N = int(input("enter no :"))
count = 0 
for i in  str(abs(N)):
    if int(i)%2 == 0 :
        count += 1
print(count)
    


#queston 27 

N = int(input("enter no :"))
count = 0 
for i in  str(abs(N)):
    if int(i)%2 == 0 :
        count +=int(i) 
print(count)


#question 28 

num = abs(58321)
largest = 0


for i in range(20):
    if num > 0:
        digit = num % 10
        if digit > largest:
            largest = digit
        num //= 10

print(largest)   



#question 29 


n = int(input("enter no :"))
s = str(n)
smallest = int(s[0])
for char in s[1:]:
    digit = int(char)
    if digit < smallest:
        smallest = digit
print(smallest)


#question 30 

n = 58321
rev = 0
for i in range(len(str(n))):
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print(rev)

#question 31

num=int(input("Enter the Number: "))
pallindrome_check=num
digit=int(math.log10(num))+1
rev=0
for i in range(digit):
    rev=rev+num%10
    rev=rev*10
    num=num//10
rev=rev//10
if rev==pallindrome_check:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q32. Count a Specific Digit

num=int(input("Enter a Number: "))
digit=input("Enter the digit to count: ")
check_num=str(num)
count=0

for i in check_num:
    if i==digit:
        count=count+1
print(count)

# Q33. First Digit Using Repeated Division

n=int(input("Enter a Number: "))
digit=int(math.log10(n))+1
for i in range(digit):
    n=n//10
    if n>0 and n<10:
        print(n)

# Q34. Difference Between Largest and Smallest Digit

n=int(input("Enter a Number: "))
digit=int(math.log10(n))+1
max=0
min=10
for i in range(digit):
    if n%10>max:
        max=n%10
    if n%10<min:
        min=n%10
    n=n//10
print(max)
print(min)
print(max-min)

# Q35. Digit Position Value

n=int(input("Enter a Number: "))
digit=int(math.log10(n))+1

for i in range(1,digit+1):
    print(n%10,i)
    n=n//10

# Q36. Armstrong Number — 3 Digit

n=int(input("Enter a Number: "))
check_no=n
digit=int(math.log10(n))+1
arm_no=0
for i in range(digit):
    arm=arm_no+(n%10)**digit
    n=n//10
if arm_no==check_no:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")