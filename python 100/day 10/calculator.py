# Calculator
def add(n1, n2):
    """ This function adds two numbers """
    return n1 + n2

def subtract(n1, n2):
    """ This function subtracts two numbers """
    return n1 - n2

def divide(n1, n2):
    """ This function divides two numbers """
    return n1 / n2

def multiply(n1, n2):
    """ This function multiply two numbers """
    return n1 * n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What's the first number: "))
    for symbol in operation:
        print(symbol)
    should_continue =True

    while should_continue:
        operation_symbol = input("Pick an operation symbol from the list above: ")   
        num2 = float(input("What's the next number: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer} ")

        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculator: ").lower() == "y":
            num1 = answer 
        else:
            should_continue = False
            calculator()

calculator()