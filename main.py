from art import logo
#calculator
print(logo)

def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply

def multiply(n1, n2):
    return n1 * n2

#divide

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "/": divide,
    "-": subtract,
    "*": multiply
}

def calculation():
    print(logo)
    num1 = float(input("What's the first number?"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    
    while should_continue:
        
        operation_symbol = input("Pick an operation.")
        
        num2 = float(input("What's the next number?"))
        first_answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        stop_or_continue = input(f"Type 'y' to continue calculating with {first_answer} or 'n' to start a new calculation.").lower()
        if stop_or_continue == "y":
            operation_symbol = input("Pick another operation symbol.")
            
            num3 = float(input("What is the number?"))
            
            second_answer = operations[operation_symbol](first_answer,num3)
            
            print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
        else:
            calculation()
            should_continue = False

calculation()