###########################################################################
#OOP
###########################################################################

########## Post it
class PostIt:
    background_color = ""
    text = ""
    text_color = ""

PostIt1 = PostIt()
PostIt2 = PostIt()
PostIt3 = PostIt()

PostIt1.background_color = "orange"
PostIt1.text_color = "blue"
PostIt1.text = "Idea 1"

PostIt2.background_color = "pink"
PostIt2.text_color = "black"
PostIt2.text = "Awesome"

PostIt3.background_color = "yellow"
PostIt3.text_color = "green"
PostIt3.text = "Superb"

print("Background color: " + PostIt1.background_color + 
      ", Text color: " + PostIt1.text_color + ", Text: " + PostIt1.text)

print("Background color: " + PostIt2.background_color + 
      ", Text color: " + PostIt2.text_color + ", Text: " + PostIt2.text)

print("Background color: " + PostIt3.background_color + 
      ", Text color: " + PostIt3.text_color + ", Text: " + PostIt3.text)
	  
	  
########## BlogPost
class BlogPost:
    author_name = ""
    title = ""
    text = ""
    publication_date = ""

blog1 = BlogPost()
blog2 = BlogPost()
blog3 = BlogPost()

blog1.author_name = "John Doe"
blog1.title = "Lorem Ipsum"
blog1.text = "Lorem ipsum dolor sit amet."
blog1.publication_date = "2000.05.04"

blog2.author_name = "Tim Urban"
blog2.title = "blue"
blog2.text = "A popular long-form, stick-figure-illustrated blog about almost everything."
blog2.publication_date = "2010.10.10"

blog3.author_name = "William Turton"
blog3.title = "One Engineer Is Trying to Get IBM to Reckon With Trump"
blog3.text = "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing."
blog3.publication_date = "2017.03.28"

print("Title: " + blog1.title + 
      "\nAuthor: " + blog1.author_name + 
      "\nText: " + blog1.text +
      "\nPublication Date " + blog1.publication_date + "\n")

print("Title: " + blog2.title + 
      "\nAuthor: " + blog2.author_name + 
      "\nText: " + blog2.text +
      "\nPublication Date " + blog2.publication_date + "\n")

print("Title: " + blog3.title + 
      "\nAuthor: " + blog3.author_name + 
      "\nText: " + blog3.text +
      "\nPublication Date " + blog3.publication_date)


###### Animal
class Animal:
    def __init__(self, hunger=50, thirst=50):
        self.hunger = hunger
        self.thirst = thirst
    
    def eat(self, amount=1):
        self.hunger -= amount
        return(self.hunger)
    
    def drink(self, amount=1):
        self.thirst -= amount
        return self.thirst
    
    def play(self, amount=1):
        self.hunger += amount
        self.thirst += amount
        return self.hunger, self.thirst
		
my_animal_eat = Animal(40,40).eat()
my_animal_drink = Animal(40,40).drink()
my_animal_play = Animal(40,40).play()

print(f"Hunger Status: {my_animal_eat} \
      \nThirst Status: {my_animal_drink} \
      \nPlay Status: hunger {my_animal_play[0]} thirst {my_animal_play[1]}")


###### Sharpie
class Sharpie:
    def __init__(self, color,width,ink_amount=100.0):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount
    
    def use(self,amount):
        self.ink_amount -= amount
        return(self.color, self.width, self.ink_amount)
    

use_of_sharpie = Sharpie("Red", 50.0).use(10) 

print(f"Sharpie with color '{use_of_sharpie[0]}', width '{use_of_sharpie[1]}, amount of ink '{use_of_sharpie[2]}'.")


###### Counter
class Counter:
    
    def __init__(self, init = 0):
        self.temp_init = init
        self.original_init = self.temp_init
        
    def add(self,number = 1):
        self.temp_init += number
        return self.temp_init
        
    def gett(self):
        return self.temp_init
    
    def reset(self):
        return self.original_init



###### Pokemon
class Pokemon(object):

    def __init__(self, name, type, effectiveAgainst):

        self.name = name
        self.type = type
        self.effectiveAgainst = effectiveAgainst

    def isEffectiveAgainst(self, anotherPokemon):

        return self.effectiveAgainst == anotherPokemon.type

    def get(self):
        
        return self.name

def initializePokemons():

        pokemon = []

        pokemon.append(Pokemon("Balbasaur", "leaf", "water"))
        pokemon.append(Pokemon("Pikatchu", "electric", "water"))
        pokemon.append(Pokemon("Charizard", "fire", "leaf"))
        pokemon.append(Pokemon("Balbasaur", "water", "fire"))
        pokemon.append(Pokemon("Kingler", "water", "fire"))
        
        return pokemon

pokemon = initializePokemons()

wildPokemon = Pokemon("Oddish", "leaf", "water")

for i in range(len(pokemon)):
    if (pokemon[i].isEffectiveAgainst(wildPokemon)):
        print(f"Ash should Choose {pokemon[i].get()}")
		

###### Fleet of Things

from Fleet import Fleet

from Thing import Thing

# Create a fleet of things to have this output:

# 1. [ ] Get milk
c = Thing("Get milk")
milk = c.__str__()
fleet = Fleet()
fleet.add(milk)

# 2. [ ] Remove the obstacles
c = Thing("Remove the obstacles")
remove = c.__str__()
fleet.add(remove)

# 3. [x] Stand up
c = Thing("Stand up")
true_complete = c.complete()
stand = c.__str__()
fleet.add(stand)

# 4. [x] Eat lunch
c = Thing("Eat Lunch")
true_complete = c.complete()
stand = c.__str__()
fleet.add(stand)
print(fleet.__str__())


###### Roll dice
import random



class DiceSet(object):

    def __init__(self):
        self.dices = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dices)):
            self.dices[i] = random.randint(1, 6)
        return self.dices

    def get_current(self, index = None):
        if index != None:
            return self.dices[index]
        else:
            return self.dices

    def reroll(self, index = None):
        if index != None:
            self.dices[index] = random.randint(1, 6)
        else:
            self.roll()


dice_set = DiceSet()
print(dice_set.get_current())
dice_set.reroll(2)
print(dice_set.get_current())
dice_set.reroll(3)
print(dice_set.get_current())


###### Dominoes
from domino import Domino

def initialize_dominoes():

    dominoes = []

    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))

    return dominoes

dominoes = initialize_dominoes()

# You have the list of Dominoes
# Order them into one snake where the adjacent dominoes have the same numbers on their adjacent sides
# eg: [2, 4], [4, 3], [3, 5] ...

c0 = dominoes[0]
c1 = dominoes[1]
c2 = dominoes[2]
c3 = dominoes[3]
c4 = dominoes[4]
c5 = dominoes[5]

print(c0.__repr__()+","+c4.__repr__()+","+c1.__repr__()+","+
      c3.__repr__()+","+c5.__repr__()+","+c2.__repr__())
	  

###### Teacher Student
class Teacher:
    
    def __init__(self, name):
        self.name = name
    
    def teach(self,student): 
        self.stu = student
        self.book = Student(student).learn()
        return f"{self.name} teaches {self.stu} {self.book}."
        
    def answer(self):
        self.problem = "List"
        return self.problem
        
        
class Student:
    
    def __init__(self, name):
        self.name = name
        
    def question(self,teacher):
        self.tea = teacher
        self.problem = Teacher(teacher).answer()
        return f"{self.name} ask {self.tea} {self.problem}."
        
    def learn(self):
        self.book = "Python"
        return self.book
 

c = Teacher("Gary")
c1 = Student("Alvin")

print(c.teach("Alvin"))
print(c1.question("Gary"))


###### Petrol Station
class Station:
    
    def __init__(self, gas_amount_s):
        self.gas_amount_s = gas_amount_s
    
    def refill(self,car):
        self.capacity = car
        self.gas_amount_s -= Car(self.capacity,self.capacity).capacity
        self.gas_amount_c = Car(self.capacity,self.capacity).gas_amount_c
        return f"The amount of gas in station is {self.gas_amount_s}.\nThe amount of gas in car is {self.gas_amount_c}."
        
        
        
class Car:
    
    def __init__(self, gas_amount_c = 0, capacity = 100):
        self.gas_amount_c = gas_amount_c
        self.capacity = capacity
        

c = Station(1000)
print(c.refill(200))