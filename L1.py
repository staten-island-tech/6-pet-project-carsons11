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

class Pet:
    def __init__(self,name):
        self.name = name
    def happiness(self):
        b = False
        while b == False:
            happiness = input("How much happiness does your pet have from a scale of 1-10?")
            if not happiness.isdigit():
                print ("Your happiness level must be a numerical integer. Try again.")
            else: 
                happiness = int(happiness)
                if happiness>10 or happiness<1:
                    print ("Your happiness level must be within a range of 1-10")
                else:
                    b = True
Snowy = Pet("Snowy")
Snowy.happiness()
    

