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
#     def __init__(self,name,animal):
#         self.__name__ = name
#         self.__animal__ = animal
#     def play(self,happinesslevel):
#         x = input("What game is your pet playing?")
#         y = int(input("How much happiness is your pet gaining?"))
#         happinesslevel += y
#         print (f"After playing {x}, this is your pet's happiness: {happinesslevel}.")
# Cat=Pet("Meow","cat")
# Cat.play(5)


class Hero:
    def __init__(self, name, money, inventory, cost):
        self.name = name
        self.__money = money
        self.inventory = inventory
        self.cost = cost
    def buy(self, item, cost):
        self.inventory.append(item)
        print(self.inventory)
Jillian = Hero("Jillian", 150, ["Potion"])