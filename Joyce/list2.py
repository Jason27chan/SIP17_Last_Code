
from random import *

seven = ["I think I love you a lot", "Sparkling chicken fingers", "Chick-fil-a is unhealthy", "I'll ride in a Paper boat", "Jelly of my Ninja Kicks", "I am worth Twenty-one cents"]
five = ["Oligotrophic water", "Aarushi Tandon and me!", "Please turn on the fan", "Sit on the toilet"]

#Generates a random integer.
x = randint(0, len(five)-1)
y = randint(0, len(seven)-1)
z = randint(0, len(five)-1)

print(five[x])
print(seven[y])
print(five[z])
