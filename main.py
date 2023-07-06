# is_online = False # booleans are capitalized
# name = input("what is your name? ")

# print("Hello " + name)

# birth_year = input("Enter your birth year: ")
#  # parseInt() in js
# age = 2020 - int(birth_year)
# print(age)

# Excercise

# first_number = float(input('First: '))
# second_number = float(input('Second: '))

# sum = first_number + second_number

# print('Sum' + str(sum))

# course = 'Python for Beginners'

# print('Python' in course) #prints true

# temperature = 25
# if temperature > 30:
#     print ("It's a hot day")
#     print("Drink water")
# elif temperature > 20:
#     print("It's a nice day")
# elif temperature > 10:
#     print("It's a bit cold")
# else:
#     print("It's cold")
# print("Done")

# Excercise

# 0.45 kgs/lb
# 2.20 lbs/kg

# weight = float(input("Weight:"))
# lbs_or_kgs = input("(K)g or (L)bs: ")

# if lbs_or_kgs.lower() == 'l':
#     converted_weight = weight / 0.45
#     print('Weight in Lbs: ' + str(converted_weight))
# elif lbs_or_kgs.lower() == 'k':
#     converted_weight = weight * 0.45
#     print('Weight in Kgs: ' + str(converted_weight))

# LOOPS

# i = 0

# while i <= 10:
#     print(i * '*')
#     i += 1

# Lists

# names = ["John", 'Bob', 'Mary']

# names[0] = "Jon"

# print(names[0:3]) # first 3 elements

# numbers = [1, 2, 3, 4, 5]
# numbers.insert(0, -1) #adds the number -1 to the begining
# numbers.remove(1)# removes element with value equal to -1 from numbers array

# print(len(numbers)) # returns boolean

# .append() add to the end of list

# FOR LOOPS

# numbers = [1, 2, 3, 4, 5]

# for item in numbers:
#     print(item)

# Range function

# numbers = (1, 2, 3)

# for number in range(5):
#     print(number)

# has_high_income = True
# has_good_credit = True

# if has_high_income or has_good_credit:
#     print("eligible for loan")

# GUESSING GAME


# secret_number = 9
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input())
#     guess_count += 1
#     if guess == secret_number:
#         print("You Win")
#         break
# else:
#     print("Sorry you lose.")

# Car Game

# command = ""

# car_started = False


# while True:
#     command = input(">").lower
#     if command == "help":
#         print(
#             """
#         start- to start car
#         stop- to stop car
#         quit- to quit
#         """
#         )
#     elif command == "start":
#         print("Car Started... Ready to go!")
#         if car_started:
#             print("car already started!")
#         else:
#             car_started = True
#             print("Car started...")
#     elif command == "stop":
#         print("Car Stopped...")
#         if not car_started:
#             print("Car is already stopped..")
#         else:
#             print("Car stopped")

#     elif command == "quit":
#         break
#     else:
#         print("Sorry i dont understand that...")

# For loops

# for x in range(4):
#     for y in range(3):
#       print(f'({x}, {y})')

# numbers = [5, 2, 5, 2, 2]

# for num in numbers:
#     output = ""
#     for count in range(num):
#         output += "x"
#     print(output)

# 2d lists

# numbers = [5, 2, 1, 7, 4]

# numbers.append(20) #add to the entd
# numbers.insert() # first param is the index to replace with
# numbers.clear() #empties list
# numbers.pop() #remove the last element
# numbers.index() # finds index of first occurrence
# numbers.count() # how many of one element are in it
# numbers.sort() #sorts list
# numbers.remove() # removes element from array

# program to remove duplicates

# numbers = [1, 1, 3, 4, 4, 4, 2, 5, 6]
# uniques = []

# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# UNPACKING

# coordinates = (1, 2, 3)

# x, y, z = coordinates

# Dictionaries (objects in js)

# customer = {
#     'name': 'John Smith',
#     'age': 30,
#     "is_verified": True
# }
# customer["name"] # same as customer.name in js
# customer.get("name")

# Exercise

# phone = input("Phone: ")

# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }

# output = ""
# for char in phone:
#     output += digits_mapping.get(char, "!") + " "
# print(output)

# EMoji converter

# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "😁",
#     ":(": "🙁"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# FUNCTIONS

# def greet_user():
#     print('HI There!')
#     print('Welcome aboard')


# print('Start')
# greet_user()
# print('FInish')

# parameters

# def greet_user(name):
#     print(f'Hi there {name}')
#     print('Welcome Aboard')

# keyword argument


# def greet_user(first_name):
#     print(f"Hi there {first_name}")
#     print("Welcome Aboard")

# greet_user(first_name="John")


# emoji converter function

# message = input(">")


# def emoji_converter(messeage):
#     words = message.split(" ")
#     emojis = {":)": "😁", ":(": "🙁"}
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output

# Error handling/ Exceptions

# try:
#     age= int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid Value')

# Classes

# class Point:
#     def move(self):
#         print('move')
#     def draw(self):
#         print('draw')


# point1 = Point() # just like the "new" keyword in js
# point1.draw()

# Constructotr

# class Point:
#     def __init__(self, x, y): # just like "Constructor" in js
#         self.x = x
#         self.y = y
#         pass
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")

# Exercise

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi there, my name is {self.name}")

# person1 = Person("Amy")
# person1.talk()

# class Mammal:
#     def walk(self):
#         print("walk")

# class Dog(Mammal):
#     pass # means im adding noting else in class

# class Cat(Mammal):
#     pass

# MODULES

# from converters import kgs_to_lbs

# print(kgs_to_lbs(70))

# Exercise
# from utils import find_max

# numbers = [10, 3, 6, 2]

# print(find_max(numbers))

# PACKAGES

# from ecommerce.shipping import calc_shipping

# calc_shipping()

# Generating random numbers

# import random

# # for i in range(3):
# #     print(random.randint(10, 20))

# people = ['JOhn', 'Mary', 'Bob']

# leader = random.choice(people)

# print(leader)

# Exercise

# import random

# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second

# dice = Dice()
# result = dice.roll()
# print("You rolled:", result[0], "and", result[1])

# workng with directory

from pathlib import Path

# Absolute path
#/usr/local/bin
path = Path()

for file in path.glob('*.py'):
    print(file)
#.exists() # checks if path exists on disk / path = Path('emails').exists() // false
#.mkdir() # makes a directory
#.rmdir() # removes dir
#.glob() # searches for specified files in argument

# Relative path


















