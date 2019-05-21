###### Apples
class apples:

    def __init__(self,name):
        self.name = name

    def get_apple(self):
        return str(self.name)


###### Sum
class sum_method:

    def __init__(self,list_int):
        self.list_int = list_int
    
    def get_sum(self):
        if self.list_int == []:
            return 0
        elif self.list_int != []:  
            return sum(self.list_int)

###### Anagram
def is_anagram(str1, str2):
    return(sorted(str1) == sorted(str2))

###### Count Letters
def count(string):

    list_string = []
    list_string[:] = string

    key_string = set(list_string)
    unique_key = list(key_string)

    new_dict = {}

    for i in unique_key:
        num = 0
        for j in list_string:
            if i == j:
                num += 1
        new_dict[i] = num

    return(new_dict)

###### Fibonacci
def fibo(n):

    a = int(n)

    if a<3 and a>0:
        return 1 
    elif a<0:
        return False
    else:
        return fibo(a-1)+fibo(a-2)

###### Sharpie
class Sharpie:
    def __init__(self, color, width,ink_amount=100.0):
        self.color = color
        self.width = abs(int(width))
        self.ink_amount = abs(int(ink_amount))
    
    def use(self,amount):
        self.ink_amount -= abs(int(amount))
        return(self.color, self.width, self.ink_amount)

###### Animal
class Animal:
    def __init__(self, hunger=50, thirst=50):
        self.hunger = abs(int(hunger))
        self.thirst = abs(int(thirst))
    
    def eat(self, amount=1):
        self.hunger -= abs(int(amount))
        return self.hunger
    
    def drink(self, amount=1):
        self.thirst -= abs(int(amount))
        return self.thirst
    
    def play(self, amount=1):
        self.hunger += abs(int(amount))
        self.thirst += abs(int(amount))
        return(self.hunger, self.thirst)

###### Cows and Bulls
import random
class cows_bulls:
    
    def __init__(self):
        self.number = []
        self.guess = []
        self.attempts = 0
    
    def makeNumber(self):
        for i in range(4):
            x = random.randrange(0,9)
            self.number.append(x)
        return self.number

    def gamestate(self,state_boolean):
        self.game_state = state_boolean
        
    def playgame(self,enter_number):
        self.cows = 0
        self.bulls = 0
        self.guess = enter_number
        
        for i in range(len(self.guess)):
            for j in range(len(self.number)):
                if self.guess[i] == self.number[j]:
                    self.bulls += 1
                    
        for k in range(len(self.guess)):
            if self.guess[k] == self.number[k]:
                self.cows += 1
        
        if(self.cows == 4):
            return "You Won!"
        if(self.cows != 4):
            return "Game Over!"

                