

# Some little play with methods

""" Name = 'Douglas'
print(name)
print(len(name))
print(name.find('o'))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isalpha())
print(name.isdigit())
print(name.count('o'))
print(name.replace('o', '-'))
print(name*3) """

############################################################

#About typecasting

""" x = 1
y = 2.0
z = "3"

print(str(x))
print(int(y))
print(float(z)*3) """

###############################################################

# input basics

""" Name = input('What is your name?: ')
Age = (input('What is your age?: '))

print('hello, ' + Name + ' your age is ' + Age +".") """

###############################################################

# importing Math module

""" import math

pi = math.pi
x = 1
y = 3
z = 4

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 2))
print(math.sqrt(425))
print(max(x, y, z))
print(min(x, y, z)) """

################################################################

# Indexing and Slice Operations

""" name = "Doug Holz"

FirstName = name[:5]
LastName = name[5:]
CodeName = name[::2]
ReverseName = name[::-1]

website1 = "http://google.com"
website2 = "http://wikipedia.com"

server = slice(7,-4)

print(website1[server])
print(website2[server]) """

################################################################

#Basic if/else operations

""" #age = int(input("Enter age: "))

if age >= 18: 
    print("You are an adult.")
elif age <= 0:
    print("You haven't been born yet.")   
else:
    print("You are not an adult.")
 """

################################################################

#logical operators and, or

""" temp = int(input("What is the temperature outside? "))

if temp >= 0 and temp <= 30:
    print("The temperature outside is good today")
    print("Go outside!")
elif temp <= 0 or temp > 30:
    print("The temperature bad is good today")
    print("Stay inside!") """
    
################################################################
    
# while loops
    
""" name = ""

while len(name) = 0:
    name = input("What is your name?: ")
    
print("Hello, " + name + ".") """

################################################################

# For loops

""" import time

for i in range(10, 21, 2):
    print(i)
    
for i in "Test Range":
    print(i)

for seconds in range(10,0,-1):
        print(seconds)
        time.sleep(1)
print("Happy New Year!") """

################################################################

#nested loops

""" Rows = int(input('How many rows: '))
Cols = int(input('how many columns: '))
Symbols = input("Enter a symbol: ") """

#will draw a rectangle of symbols with rows as height and collums as lenght :4

""" for row in range(Rows):
        for col in range(Cols):
            print(Symbols, end = '')
        print()
    print() """

################################################################

#Loop Control Statements

""" while True:
    name = input("Enter your name: ")
    if name != "": 
        break

phone_number = "53911534-0636"

for i in phone_number:
    if i == "-":
        continue
    print(i, end=" ") """
"""     
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i, end=" ") """
        
################################################################

# Lists

""" food_list = ["pizza", "ham", "hotdogs", "spam"]

print(food_list[0])

food_list[1] = "sushi"

print(food_list[1])

for i in food_list:
    print(i)
    
food_list.append("Banana")
food_list.remove("ham")
food_list.pop()
food_list.insert("Cake")
food.sort()
food_list.clear() """

################################################################

# 2D list

""" drinks = ["coffee", "soda", "tea"]
dinner = ['pizza', 'hamburger', 'hotdogs']
deserts = ['cake', 'ice cream']

food = [drinks, dinner, deserts]

print(food[0] [0])
print(food[1] [2]) """

################################################################

#tuples

""" student = ('John', 21 , 'male')

print(student.count("John"))
print(student.index('John'))

if "John" in student:
        print("Student is enroled")
else:
    print("Student is not enrolled") """
    
################################################################

#Sets

""" utensils = {"fork", "spoon", "knife"}
dishes = {"bow", "plate", "cup"}


utensils.add("napkins")
utensils.remove("fork")

print(utensils.difference(dishes)) 

dishes.update(utensils)

dinner_table = utensils.union(dishes)

for x in dishes:
    print(x)
   
print(dinner_table) """


################################################################

# dictionaries

""" Capitals = {"USA":"Washington DC", 
            "India":"New Dehli",
            "Brazil": "Brasilia"
            }

print(Capitals['India'])
print(Capitals.get('Germany'))
print(Capitals.values())
print(Capitals.keys())
print(Capitals.items())

for key,value in Capitals.items():
    print(key, value)
    
Capitals.pop('India')
print(Capitals.items())

Capitals.clear()
print(Capitals.items())
 """

################################################################

#index operator
""" 
name = "douglas Holz"

if(name[0].islower()):
    name = name.capitalize()

print(name)

firstName = name[:4].upper()
lastName = name[8:].lower()
lastCharacter = name[-1]

print(firstName)
print(lastName)
print(lastCharacter) """

################################################################

#intro to Functions
""" 
def greeting(name, age):
    print("Hello, " + name)
    print("Your age is " + age)

userName = input("Enter your username: ")
userAge = input("Enter your age: ")

greeting(userName, userAge) """

https://www.britannica.com/plant/cinnamon

# return statement

""" def multiply(a, b):
    return a * b

data = multiply(6,8)

print(data) """




################################################################
