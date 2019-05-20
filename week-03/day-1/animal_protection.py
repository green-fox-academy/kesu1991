from random import randint

class animal:

    def __init__(self, healthState, healCost, name = "animal"):
        self.name = name
        self.healthState = healthState
        self.healCost = healCost


    def heal(self):
        self.isHealthy = True
        return(self.isHealthy)

    def isAdoptable(self):
        if(self.healthState == True):
            self.adopt = True
            return(self.adopt)
        elif(self.healthState == False):
            self.adopt = False
            return(self.adopt)

    def toString(self):
        if(self.isAdoptable() == True):
            return(f"<{self.name}> is healthy, and adoptable")
        elif(self.isAdoptable() == False):
            return(f"<{self.name}> is not healthy (<{self.healCost}>\u20ac), and not adoptable")

cat = animal(True,randint(0, 6),"cat")
cat.isAdoptable()
cat.toString()

dog = animal(True,randint(1, 8),"dog")
dog.isAdoptable()
dog.toString()

parrot = animal(False,randint(4, 10),"parrot")
parrot.isAdoptable()
parrot.toString()

class shelter:

    def __init__(self, animals, budget = 50):
        self.animals = animals
        # self.adopters = adopters
        self.budget = budget
        self.adopter_name = []

    def rescue(self,refer_animal):
        self.animals.append(refer_animal)
        return(len(self.animals))

    def heal(self):
        for i in range(len(self.animals)):
            if(self.animals[i].isAdoptable() == False):
                self.animals[i].heal()
                self.budget = self.budget - self.animals[i].healCost
                if(self.budget >= 0):
                    self.amount = 1
                    return(self.amount, self.budget)
                elif(self.budget < 0):
                    self.amount = 0
                    return(self.amount, self.budget)
             
    def addAdopter(self, name):
        self.adopter_name.append(name)
        return(self.adopter_name)

    def findNewOwner(self):        
        for i in range(len(self.animals)):

            del self.animals[randint(0, len(self.animals)-1)]
            del self.adopter_name[randint(0, len(self.adopter_name)-1)]

        return(len(self.animals),self.adopter_name)

    def earnDonation(self,amount):
        self.amount = amount
        self.budget += self.amount
        return(self.budget)

    def toString(self):

        print(f"Budget: <{self.budget}>\u20ac,\
            \nThere are <{len(self.animals)}> animals and <{len(self.adopter_name)}> potential adopters")
        
        for i in self.animals:
            if(i.isAdoptable() == True):
                print(f"<{i.name}> is healthy, and adoptable")
            elif(i.isAdoptable() == False):
                print(f"<{i.name}> is not healthy (<{i.healCost}>\u20ac), and not adoptable")

test = shelter([cat,dog])
test.rescue(parrot)
test.heal()
test.addAdopter("Gary")
test.addAdopter("Alvin")
test.addAdopter("Ruby")
test.addAdopter("Masa")
test.earnDonation(600)
print(test.toString())








        