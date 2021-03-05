# Python class example
import random


class Baby():
    """A simple class to simulate the baby"""
    
    def __init__(self, name, gender, age):
        """Initialize an attributes"""
        self.name = name.title()
        self.gender = gender
        self.age = age
        self.tired = True
        
        
    def play(self):
        """simulate playing based on gender"""
        if self.gender == 'male':
            print(self.name + ' is playing with cars.')
        elif self.gender == 'female':
            print(self.name + ' is playing with doll')
        else:
            print('Not a valid gender')
    
    
    def cry(self):
        """Simulate crying"""
        print('WAAAHH WAAAHH')
        print('Even ' + str(self.age) + ' year olds cry.')
        
        
    def sleep(self):
        """Simulates sleeping"""
        if self.tired:
            print(self.name + ' is sleeping... finally!!!')
            self.tired = False
        else:
            print(str(self.name) + ' is awake and playing!!!')
            
    
little_boy = Baby('rohan', 'male', 3)
little_girl = Baby('mary', 'female', 2)

print(little_boy.name + ' is a ' + str(little_boy.age) + ' year old ' + little_boy.gender + '.')

little_boy.cry()
little_boy.play()
little_girl.play()

little_boy.sleep()
little_boy.sleep()

babies = []
for i in range(25):
    num = random.randint(0,1)
    if num == 0:
        gender = 'male'
    else:
        gender = 'female'
        
    age = random.randint(0, 5)
    baby = Baby(str(i + 1), gender, age)
    babies.append(baby)

for baby in babies:
    print('Baby #' + baby.name + ' is a ' + str(baby.age) + ' year old' + baby.gender + '.')



