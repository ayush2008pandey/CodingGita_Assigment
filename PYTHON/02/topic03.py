#question 21

number = 583
ones = number % 10

print("Ones Digit:", ones)


#question 22


number = 583
tens = (number // 10) % 10

print("Tens Digit:", tens)



#question 23


number = 583
hundreds = number // 100

print("Hundreds Digit:", hundreds)


#question 24

number = 746

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

print("Ones Digit:", ones)
print("Tens Digit:", tens)
print("Hundreds Digit:", hundreds)



#question 25

number = 5829

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

print("Ones Digit:", ones)
print("Tens Digit:", tens)
print("Hundreds Digit:", hundreds)
print("Thousands Digit:", thousands)



#question 26


number = 583

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

digit_sum = hundreds + tens + ones
print("Sum of Digits:", digit_sum)



#question 27


number = 4726

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

digit_sum = thousands + hundreds + tens + ones
print("Sum of Digits:", digit_sum)


#question 28

number = 234

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

product = hundreds * tens * ones
print("Product of Digits:", product)



#question 29

number = 583

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

reversed_number = (ones * 100) + (tens * 10) + hundreds

print("Original Number:", number)
print("Reversed Number:", reversed_number)


#question 30

number = 4726

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

reversed_number = (ones * 1000) + (tens * 100) + (hundreds * 10) + thousands

print("Original Number:", number)
print("Reversed Number:", reversed_number)



#question 31

number = 5834

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

print("Thousands Place:", thousands * 1000)
print("Hundreds Place:", hundreds * 100)
print("Tens Place:", tens * 10)
print("Ones Place:", ones)


#question 32
number = 583

ones = number % 10
hundreds = number // 100

difference = hundreds - ones
print("Difference:", difference)


#question 33


number = 583
ones = number % 10
print("Ones Digit:", ones)


#question 34

number = 9365

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10

print("Thousands Digit:", thousands)
print("Hundreds Digit:", hundreds)
print("Tens Digit:", tens)
print("Ones Digit:", ones)



#question 35

hundreds = 5
tens = 8
ones = 3

number = (hundreds * 100) + (tens * 10) + ones
print("Number:", number)





