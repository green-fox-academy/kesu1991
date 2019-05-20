###### Hero battle

class MarvelHero:

    def __init__(self, name,motivation = 40):
        self.name = name
        self.motivation = motivation

    def getMotivationLevel(self):

        if(self.motivation < 25):
            self.moti_level = 0
            return(self.moti_level)

        elif(self.motivation >= 25 and self.motivation <= 40):
            self.moti_level = 1
            return(self.moti_level)

        elif(self.motivation > 40):
            self.moti_level = 2
            return(self.moti_level)


    def punch(self,other_hero):
        self.moti_level = self.getMotivationLevel()

        if(self.moti_level >= 1):
            self.punched_damage = other_hero.bepunched()[0]
            return(self.punched_damage)       

    def bepunched(self):
        self.damage = self.motivation / 1.5
        self.motivation = self.motivation - (self.damage/self.motivation)
        return[self.damage,self.motivation]

    def toString(self):
        self.getMotivationLevel() 

        if(self.moti_level == 0):
            return(f"{self.name} is not motivated anymore.")
        if(self.moti_level == 1):
            return(f"{self.name} is motivated.")
        if(self.moti_level == 2):
            return(f"{self.name} is well motivated.")

tony = MarvelHero("Tony",100)
hulk = MarvelHero("Hulk",80)
tony.punch(hulk)
print(hulk.toString())





class DCHero:

    def __init__(self, name,motivation = 45):
        self.name = name
        self.motivation = motivation

    def getMotivationLevel(self):

        if(self.motivation < 25):
            self.moti_level = 0
            return(self.moti_level)

        elif(self.motivation >= 25 and self.motivation <= 40):
            self.moti_level = 1
            return(self.moti_level)

        elif(self.motivation > 40):
            self.moti_level = 2
            return(self.moti_level)

    def punch(self,other_hero):

        self.moti_level = self.getMotivationLevel()

        if(self.moti_level >= 1):
            self.punched_damage = other_hero.bepunched()[0]
            return(self.punched_damage)       

    def bepunched(self):
        self.damage = self.motivation / 1.5
        self.motivation = self.motivation - (self.damage/self.motivation)
        return[self.damage,self.motivation]

    def toString(self):
        self.getMotivationLevel() 
        
        if(self.moti_level == 0):
            return(f"{self.name} is not motivated anymore.")
        if(self.moti_level == 1):
            return(f"{self.name} is motivated.")
        if(self.moti_level == 2):
            return(f"{self.name} is well motivated.")

superman = DCHero("Superman",100)
batman = DCHero("Batman")
superman.punch(batman)
print(batman.toString())


