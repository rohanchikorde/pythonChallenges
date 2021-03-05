# calculator python

def add(a, b):
    """Add two numbers and return sum"""
    summation = round(a + b, 4)
    print('summation of ' + str(a) + ' and ' + str(b) + ' is ' + str(summation) + '.')
    return str(a) + ' + ' + str(b) + ' = ' + str(summation)
    
def subtract(a, b):
    """Subtract two numbers and return the difference"""
    difference = round(a - b, 4)
    print('Difference of ' + str(a) + ' and ' + str(b) + ' is ' + str(difference) + '.')
    return str(a) + ' - ' + str(b) + ' = ' + str(difference)


def multiply(a, b):
    """multiply two numbers and return the product"""
    product = round(a * b, 4)
    print('Product of ' + str(a) + ' and ' + str(b) + ' is ' + str(product) + '.')
    return str(a) + ' * ' + str(b) + ' = ' + str(product)    

def divide(a , b):
    """divide two numbers and return the quotient"""
    if b == 0:
        print('You cannot be divided by zero')
        return 'Div Error'
    else:
        quotient = round(a / b, 4)
        print('The quotient of ' + str(a) + ' and ' + str(b) + ' is ' + str(quotient) + '.')
        return str(a) + ' / ' + str(b) + ' = ' + str(quotient)    
    
def exponent(a, b):
    """take a number to a power and return the result"""
    power = round(a ** b, 4)
    print('Power of ' + str(a) + ' raised to ' + str(b) + ' is ' + str(power) + '.')
    return str(a) + ' ** ' + str(b) + ' = ' + str(power)        
    

# Main function
def main():
    print('\n--------- Welcome to the Python Calculator! ---------')
    print('\n Enter two numbers and an operation desired')
    
    history = []
    running = True
    while running:
        # get user input
        num1 = float(input('\n Enter a number: '))
        num2 = float(input(' Enter a number: '))
        operator = input('Enter an operation (add, sub, mul, div, exp): ').lower().strip()
        if operator == 'add' or operator == 'a':
            result = add(num1, num2)
        elif operator == 'sub' or operator == 's':
            result = subtract(num1, num2)
        else:
            print('\nThis is not a valid operation ')
            result = 'Opp Error'

        # append the result to the history
        history.append(result)
        
        choice = input('\nWould you like to run again? ').lower().strip()
        if choice != 'y':
            print('\nCalculation Summary: ')
            for cal in history:
                print(cal)
            print('\nThank you for using python calculator')
            running = False
        
        
main()