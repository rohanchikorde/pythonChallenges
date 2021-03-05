import random

def dice_sides():
    """Ask the user how many sides on their die"""
    sides = int(input('\nHow many sides would you like on your dice: '))
    return sides
    
    
def dice_number():
    """Ask the user how many dice to roll"""
    number = int(input('\nHow many dice would you like to roll: '))
    return number
   
def roll_dice(sides, number):
    """Simulate rolling the dice"""
    dice = []
    print('\n You rolled ' + str(number) + ' ' + str(sides) + ' sided dice.')
    print('\n----Results are as followed---')
    for i in range(number):
        value = random.randint(1, sides)
        print('\t' + str(value))
        dice.append(value)
    return dice
    
def sum_dice(dice):
    """Add all values of dice in a list"""
    # using built in sum function
    # print("The total value of your roll is " + str(sum(dice)) + ".")
    # using our own method.
    total = 0
    for die in dice:
        total += die
    print("The total value of your roll is " + str(total) + ".")
    
def roll_again():
    """Ask the user to roll again"""
    choice = input('\nWould you like to roll it again? ').lower().strip()
    if choice == 'yes':
        roll = True
    else:
        roll = False
    return roll
    
# main code
print("\nWelcome to the Python Dice App") 
rolling = True
while rolling:
    # get the info for the types of sides
    d_sides = dice_sides()
    d_number = dice_number()
    
    # roll the dice
    my_dice = roll_dice(d_sides, d_number)
    sum_dice(my_dice)
    
    # roll again
    rolling = roll_again()

print('\nThank you for using the Python Dice App')
    