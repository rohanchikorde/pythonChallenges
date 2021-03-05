# bank deposit and withdrawal 

def get_info():
    """ get user info in a dict that represent a bank account"""
    print('\n Welcome to the Python First Nation Bank')
    name = input('\nHello, what is your name? ').title().strip()
    print('\nHello, ' + name.title())
    savings = int(input('\nHow much money would you like to set up your saving account with? '))
    checking = int(input('How much money would you like to set up your saving account with? '))
    
    # build a dict that represent a specific bank account
    bank_account = {
        'Name' : name,
        'Savings' : savings,
        'Checking' : checking
        }
    return bank_account
    
def make_deposit(bank_account, account, money):
    """ add money to a specific type of account"""
    bank_account[account] += money
    print('\nDeposited $' + str(money) + ' into ' +  bank_account['Name'] + '\'s ' + account.lower() + ' account.')
    return bank_account
    
def make_withdrawal(bank_account, account, money):
    """ withdraw money from a specific type of account"""
    # check if the balance is positive after withdrawal
    if bank_account[account] - money >= 0:
        bank_account[account] -= money
        print('\nWithdrew $' + str(money) + ' from ' + bank_account['Name'] + '\'s ' + account.lower() + ' account.')
    else:
        print('\nSorry, by withdrawing $' + str(money) + ' from ' + bank_account['Name'] + ', you will have negative balance')
    
def display_info(bank_account):
    """ display all key value pair in a given bank account"""
    print('\nCurrent account info: ')
    for key, value in bank_account.items():
        if key == 'Name':
            print(key + ': ' + str(value))
        else:
            print(key + ': $' + str(value))

    

# main

def main():
    # create a bank account
    my_acc = get_info()
    
    running = True
    while running:
        # show current state of bank account
        display_info(my_acc)
        
        # get user input for the transaction info
        account_type = input('\nWhat account would you like to access (Savings or Checking): ').title().strip()
        choice = input('\nDeposit or Withdrawal: ').title().strip()
        amount = float(input('How much money: '))
        
        # make the correct function call based off previous user input
        if account_type == 'Savings' or account_type == 'Checking':
            if choice == 'Deposit':
                make_deposit(my_acc, account_type, amount)
                display_info(my_acc)
            elif choice == 'Withdrawal':
                make_withdrawal(my_acc, account_type, amount)
            else:
                print('\nSorry we cant do that for you today')
        else:
            print('\nSorry, we dont have that service')
            
        # allow user to make another transaction
        choice = input('\nWould you like make another transaction: ').lower().strip()
        if choice != 'y':
            print('\nThank you for using the bank application')
            running = False
        
main()            
        
