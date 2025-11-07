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


# class Hero:
#     def __init__(self, name, money, inventory):
#         self.name = name
#         self.__money__ = money
#         self.inventory = inventory
#     def buy(self, item, cost):
#         self.inventory.append(item)
#         self.__money__ -= cost
#         print (f"After buying {item}, {self.name} now has ${self.__money__}.")
# Ricky = Hero("Ricky", 150, ["Potion"])
# Ricky.buy("Nathan",6.99)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display_info(self):
        return (f"User: {self.name}, Email: {self.email}")
    
class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)  # Call the parent class constructor
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
    

class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"
    
class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"

student = Student("Alice", "alice@example.com", "S12345")
teacher = Teacher("Mr. Smith", "smith@example.com", "Mathematics")
administrator = Administrator("Ms. Johnson", "johnson@example.com", "Principal")

print(student.display_info())  # Output: Student: Alice, Email: alice@example.com, Student ID: S12345
print(teacher.display_info())  # Output: Teacher: Mr. Smith, Email: smith@example.com, Subject: Mathematics
print(administrator.display_info())  # Output: Administrator: Ms. Johnson, Email: johnson@example.com, Role: Principal