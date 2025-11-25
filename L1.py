# class Hero:
#     def __init__(self, name, money, inventory):
#         self.name = name
#         self.money = money
#         self.inventory = inventory

#     def buy(self, item):
#         self.inventory.append(item)
#         print(self.inventory)
# Jillian = Hero("Jillian", 150, ["Potion"])
# Jillian.buy({"title": "Sword", "atk": 34})
# print(Jillian.__dict__) 

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # double underscore means "private"
#     def deposit(self, amount):
#         self.__balance += amount
#     def show_balance(self):
#         print(f"{self.owner} has ${self.__balance}")


# class Hero:
#     def __init__(self, name, money, inventory):
#         self.name = name
#         self.money = money
#         self.inventory = inventory

#     def buy(self, item):
#         self.inventory.append(item)
#         print (f"This is your inventory {self.inventory}")
# Nathan = Hero("Batman", 200, ['Batarang'])
# print (Nathan.__dict__)
# Nathan.buy({"title": "Batmobile", "maxspeed": "Mach 1"})


# class Pet:
#     def __init__(self,name,happinesslevel):
#         self.__name__ = name
#         self.__happinesslevel__= happinesslevel
#     def play(self,game,happinesslevelgain):
#         self.__happinesslevel__ += happinesslevelgain
#         print (f"After playing {game}, this is your pet's happiness: {self.__happinesslevel__}.")
# Cat=Pet("Fluffy",0)
# Cat.play("Laser",10)


""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.__money__ = money
        self.inventory = inventory
    def buy(self, item, cost):
        self.inventory.append(item)
        self.__money__ -= cost
        print (f"After buying {item}, {self.name} now has ${self.__money__}.")
Ricky = Hero("Ricky", 150, ["Potion"])
Ricky.buy("Nathan",6.99) """


import random
class Pet:
    def __init__(self, name):
        self.name = name
        self.petscore = 50
        self.happiness = 5
        self.cleaniness = 5
        self.hunger = 5
        
    def happiness_change(self):
        randomhappinessdecrease = random.randint(1,5)
        self.happiness - randomhappinessdecrease
        print (f"Pet Happiness: {self.happiness}    Pet Cleaniness: {self.cleaniness}    Pet Hunger: {self.hunger}")
        if self.happiness < 5:
            print (f"{self.name} is feeling sad. You need to play with your pet.")
            print ("1: Play with your pet.")
            print ("2: Ignore him/her.")
        x = input ("Choose the number that accommodates the action you wanna do:")
        if x == "1":
            self.happiness = 10
            print ("Hooray, your pet's happiness is now max.")
            self.petscore += 15
        if x == "2":
            self.happiness = 0
            print ("Your pet is depressed. You lost 15 points to your pet score.")
            self.petscore -= 15
        print (f"Your pet score is now at {self.petscore}") 
Pet = Pet("Pet")

def petplay():
    print ("Welcome. Your goal is to get all your pet's attributes to max which is 10 and achieve the highest pet score possible. Your pet score starts at 50 with max being 100.")
    randomvariable=random.randint(1,3)
    if randomvariable==1:
        Pet.happiness_change
    if randomvariable==2:
        Pet.
petplay()