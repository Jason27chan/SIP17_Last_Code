start = '''
 You wake up on a Monday and realize you have have to go through a series of steps in order to make it to school. Make these choices and see where your day takes you!
'''


print(start)


print("Do you want to eat breakfast this morning (yes or no)?")
user_input = input()
if user_input == "yes":
    print("You have eaten breakfast. How do you want to get to school? Type A to drive yourself to school. Type B to walk to school. Type C to take the bus.")
    user_input = input()
    if user_input == "A":
        print ("You have chosen to drive yourself to school. On the way to school your car breaks down and you end up waiting the whole day to get it towed.")
    elif user_input == "B":
        print ("You have chosen to walk to school. Do you want to stop and get coffee on the way? (yes or no)")
        user_input = input()
        if user_input == "yes":
            print ("You are late to school. Since it is your third offense this year, you get a suspension and you can not return to school until next Monday. Adventure over")
        elif user_input == "no":
            print ("You have arrived to school on time! Congratulations!")
        else :
            print ("This is not a valid answer. You must begin the game again.")
    elif user_input == "C":
        print ("Do you want to stop and get coffee on the way? (yes or no)")
        user_input = input()
        if user_input == "yes":
            print ("You are late to school. Since it is your third offense this year, you get a suspension and you can not return to school until next Monday. Adventure over.")
        elif user_input == "no":
            print ("You have arrived to school on time! Congratulations!")
        else :
            print ("This is not a valid answer. You must begin the game again.")
    else :
        print ("This is not a valid answer. You must begin the game again.")

elif user_input == "no":
    print("You have not eaten breakfast. You are too tired to go to school and fall asleep in your bed. You never make it to school.")
else:
    print ("This is not a valid answer. You must begin the game again.")
