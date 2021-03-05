# another class example

class House():
    """A class to model a house that is for sale"""
    
    def __init__(self, style, sq_footage, year_built, price):
        """Initialize attribue"""
        self.style = style
        self.sq_footage = sq_footage
        self.year_built = year_built
        self.price = price
        
        self.sold = False
        self.weeks_on_market = 0
        
    
    def display_info(self):
        """Display the information on the house"""
        print('\n --- House for Sale ---')
        print('House Style: \t' + str(self.style))
        print('Square feet: \t' + str(self.sq_footage))
        print('Year Built: \t' + str(self.year_built))
        print('House Price: \t' + str(self.price))
        print('\nThis house has been in the market for ' + str(self.weeks_on_market))
        
        
    def sell_house(self):
        """Sell the house"""
        if self.sold == False:
            print('Congratulation! Your house has sold for $' + str(self.price) + '!')
            self.sold = True
        else:
            print('Sorry this house is no longer for sale')
            
          
    def change_price(self, amount):
        """Change the sell price of the house"""
        self.price += amount
        if amount < 0:
            print('\nPrice drop!!!')
        else:
            print('The house has increased in value by $' + str(amount) + '.')
            
    
    def update_weeks(self, weeks=1):
        """Increment the number of weeks a house has been on the market"""
        self.weeks_on_market += weeks
        
        
my_house = House('Ranch', 1800, 1962, 199900)
        
# print attribute
print(my_house.sq_footage)
print(my_house.style)
print(my_house.year_built)
print(my_house.price)
    
# house on market for 1 week
my_house.update_weeks()
my_house.display_info()
        
# house on market for 15 week
my_house.update_weeks(15)
my_house.display_info()
        
# drop price
my_house.change_price(-15000)        
my_house.display_info()
        
# house on market for 15 week
my_house.update_weeks(5)
my_house.display_info()

# drop price
my_house.change_price(200000)        
my_house.display_info()


# wrong sq ft
my_house.sq_footage -= 150
my_house.change_price(-1000)
my_house.display_info()

# sell house
my_house.sell_house()

my_house.sell_house()
my_house.display_info()