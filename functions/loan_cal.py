# loan calculator app
from matplotlib import pyplot

def get_loan_info():
    """Get the basic information of a loan and store it in a dictionary"""
    loan = {}
    
    # get user input for the categories of the loan
    loan['principal'] = float(input('\nEnter the loan amount: '))
    loan['rate'] = float(input('Enter the interest rate: '))/100
    loan['monthly payment'] = float(input('Enter the desired monthly payment: '))
    loan['money paid'] = 0
    return loan


def show_loan_info(loan, number):
    """Display the current loan status"""
    print('\n----Loan Information after ' + str(number) + ' months----')
    for key, value in loan.items():
        print(key.title() + ": " + str(value))
    
    
def collect_interest(loan):
    """update loan for interest per month"""
    # divide by 12 to simulate collecting interest monthly
    loan['principal'] = loan['principal'] + loan['principal'] * loan['rate']/12
    
    
def make_monthly_payment(loan):
    """simulate a monthly payment to pay down a principal"""
    loan['principal'] = loan['principal'] - loan['monthly payment']
    if loan['principal'] > 0:
        loan['money paid'] += loan['monthly payment']
    else:
        loan['money paid'] += loan['monthly payment'] + loan['principal']
        loan['principal'] = 0
    
def summarize_loan(loan, number, initial_principal):
    """Display the results of paying off the loan"""
    print('\nCongratulations! you paid off your loan in ' + str(number) + ' months!')
    print('\nYour initial loan was $' + str(initial_principal) + ' at a rate of ' + str(100*loan['rate']))
    print('Your monthly payment was $' + str(loan['monthly payment']) + '.')
    print('You spent $' + str(round(loan['money paid'], 2)) + ' in total.')
    
    interest = round(loan['money paid'] - initial_principal, 2)
    print('You spent $' + str(interest) + ' on interest!')
        
    
def create_graph(data, loan):
    """Create a graph to show a relationship between principal and time"""
    x_values = []
    y_values = []
    
    # loop through a dataset. 
    # point is a tuple. point[0] represent month number and point[1] is a principal value
    for point in data:
        x_values.append(point[0])
        y_values.append(point[1])
        
    # create a plot for x values and y values (month number and principal)
    pyplot.plot(x_values, y_values)
    pyplot.title(str(100*loan['rate']) + '% Interest with $' + str(loan['monthly payment']) + ' Monthly Payment')
    pyplot.xlabel('Month Number')
    pyplot.ylabel('Principal of Loan')
    pyplot.show()
    
    
# Main
def main():
    print('Welcome to the Loan Calculator App!')
    
    month_number = 0
    my_loan = get_loan_info()
    starting_principal = my_loan['principal']
    data_to_plot = []
    
    show_loan_info(my_loan, month_number)
    input('Press Enter to begin paying off your loan.')
    
    # simulate paying off the loan as long as the loan's principal > 0
    while my_loan['principal'] > 0:
        # you cannot get ahead of the interest, you will never pay off the loan so break
        if my_loan['principal'] > starting_principal:
            break
        # it is possible to pay off the loan. so simulate a single month
        month_number += 1
        collect_interest(my_loan)
        make_monthly_payment(my_loan)
        data_to_plot.append((month_number, my_loan['principal']))
        show_loan_info(my_loan, month_number)
        
    # the loan is either paid off full or it can Never be paid off..
    if my_loan['principal'] <= 0:
        summarize_loan(my_loan, month_number, starting_principal)
        create_graph(data_to_plot, my_loan)
    else:
        print('\nYou will never pay off your loan!!!')
        print('You cannot get ahead of the interest :(')


if __name__ == '__main__':
        main()
