#Data types
#String 
print("Hello"[0])
print("Hello"[3])
print("Hello"[4])
print("123 "+"345")
print(123+345)
123_456_789

#Float

3.14159

#Boolean
True
False
#Type Error, Type checking and Type 
print(len("Emmanuel"))
num_char =len(input("What is your name?\n"))
print(type(num_char))
new_num_char =str(num_char)
print("Your name has "+ new_num_char +" characters")
a=str(123)
print(type(a))
b=float(231)
print(type(b))
print(str(70)+ str(100))
two_digit_number=input("Type a 2 digit number\n")
type(two_digit_number)
print(type(two_digit_number))
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
print(first_digit)
print(second_digit)
result=first_digit + second_digit
print(result)

print(6/4)

#Body Mass Index Calculator
weight = input("enter your weight in kg:\n ")
height = input("enter your height in m:\n ")
weight_as_int = int(weight)
height_as_int = int(height)
BMI = weight_as_int / float(height_as_int) ** 2
bmi_as_int = int(BMI)
print(bmi_as_int)

#f-String
score = 75
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#Life in weeks
age = input("What is your current age?")
age_as_int =int(age)
years_remaining = 120 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message =f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining}months left"
print(message)

print("Welcome to the tip Calculator!")
bill= float(input("What was the total bill? $"))
tip =int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
tip_as_percent =tip/100
total_tip_amount =bill * tip_as_percent
total_bill= bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
