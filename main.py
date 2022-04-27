#dice roll program
import random
while True:
    print("1. Roll the dice")
    print("2. Exit program")
    user_input = int(input("Select one of the options:"))
    if user_input == 1:
        dice_number = random.randint(1,6)
        print("number on the dice is: ", dice_number)
    elif user_input == 2:
        print("end of the program")
        break
    else:
        print("invalid input")

#end of the program.
