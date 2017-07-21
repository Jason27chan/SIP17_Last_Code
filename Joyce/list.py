
from random import *


#Create the list of words you want to choose from.
Soda = ["water", "Orange Juice", "Sprite"]
Food = ["fries", "burger", "chicken sandwiches"]
Dessert = ["Strawberry Shortcake", "Flan", "Cheesecake", "Ice Cream"]
#Generates a random integer.
x = randint(0, len(Soda)-1)
y = randint(0, len(Food)-1)
z = randint(0, len(Dessert)-1)

print(Soda[x])
print(Food[y])
print(Dessert[z])
