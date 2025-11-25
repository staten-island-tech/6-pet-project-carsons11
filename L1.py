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
    def __init__(self):
        self.happiness = 5
        self.cleaniness = 5
        self.hunger = 5
        
    def happiness_change(self):
        randomhappinessdecrease = random.randint(1,5)
        self.happiness - randomhappinessdecrease
        if self.happiness < 5:
            print (f"{name} happiness is at {self.happiness}. You need to play with your pet.")
            print ("1: Play with your pet.")
            print ("2: Leave him sad.")
        x = input ("")
        
         
def petplay():
    name = input("What is your pet's name?").strip()
    randomvariable=random.randint(1,3)
    if randomvariable==1:
        Pet.happiness_change
    if randomvariable==2:
        Pet.
