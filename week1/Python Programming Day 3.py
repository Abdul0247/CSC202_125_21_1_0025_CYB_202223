#comparison
print("welcome to day3")

height= int(input("what is your height in cm "))
if height>120:
    print("you are elegible")
else:
    print("try again after some time")

#checking whether the number is even or odd
number = int(input("enter any number "))

if number % 2==0:
    print("the number is even")
else:
    print("it's an odd number")

#nested loop option
print("welcome to day3")

height= int(input("what is your height in cm "))
if height>=120:
    print("you are elegible")
    age= int(input("what is your age: "))
    if age<=12:
        print("your charges is $10")
    elif age<=18:
        print("you are to pay $25")
    else:
        print("you have to pay $50")
else:
    print("try again after some time")

#CREATING BODY MASS(BMI)
#BMI = w/h**2
print("BMI CALCULATOR")
weight =  input("enter your weight \n")
height= input("enter your height\n")
hei = height**2
BMI=weight/hei
print(BMI)