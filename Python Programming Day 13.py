def format_name(first_Name,Last_Name):
    formated_first_Name = first_Name.title()
    formated_Last_Name = Last_Name.title()
    return f"{formated_first_Name} {formated_Last_Name}"
print(format_name("ABDULRAHMAN", "AMINU"))


# CALCULATION OF DAYS IN A MONTH
def leap_period(year):
    if year %4 == 0:
        if year %100 == 0:
            if year %400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_available(year, month):
    if month > 12 or month < 1:
        return "invalid Month"
    month_days = [31,28,31,30,31,31,31]
    if leap_period(year) and month == 2:
        return 29
    print (month_days[month - 1])

year = int(input("Enter a year: "))
month = int(input("Enter a month:"))
print("The number of days in the month is ", end=" ")
days = days_available(year, month)



# Python calculator
print("\nTHIS IS A BASIC CALCULATOR")

def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}



def calculator():
    num1 = int(input("\nEnter your first number for basic calculation operation "))
    print("\n Choose an operation")
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_Sign = input("pick an operations: ")
        num2 = int(input("\n Enter the second Number "))
        calculation_function = operations[operation_Sign]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_Sign} {num2} = {answer} ")
        
        if input(f"Type 'y' to continue calculating with the answer ({answer}), or type 'n' to start new calculation: ") == "y":
            num1 = num2
        else:
            should_continue = False
            calculator



calculator()