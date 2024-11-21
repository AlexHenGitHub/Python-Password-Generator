#Programmer: Alexander Henriquez
#Purpose of this program is to do basic text encryption
#Data: 11/18/2024


import random

from numpy.lib.user_array import container

while True:

# Get user input
    userinput = input("Type anything: ")

    # Shuffle the list of characters
    char_list = list(userinput)

    # Convert the input into a list of characters
    random.shuffle(char_list)

    # Join the shuffled list back into a string
    scrambled_output = ''.join(char_list)

    if userinput:
        key = random.randint(-10000000000000000000000000000*10000000000000000000000000000,
                         10000000000000000000000000000 * 10000000000000000000000000000)
    print(key)
    print()
    print("Scrambled Output:", scrambled_output, "non scrambled input:", userinput)
    userinput


    again = input("Do you want to go again 1 = yes, 0 = no")



    if again == "1" :
        continue

    else:
        print("End")
        break



#Text
Label(root, text='PASSWORD GENERATOR').grid(column=0, row=1, ipady=10, ipadx=285)
# Filler
Label(root).grid(column=1, row=2, ipady=30)
Label(root).grid(column=2, row=3, ipady=30)
Label(root).grid(column=3, row=4, ipady=30)

# slider
slider = Scale(root, from_=0, to=100, length=400, resolution=1, orient=HORIZONTAL)
slider.grid(column=0, row=3, ipady=30)
#special character question
Label(root, text='How many characters you want?').grid(column=0, row=3)

## need a way to see how the text was changed and track it




## maybe make an if statment that compares input vs scambled text aand that
## can be the bases for the decrypter


##w\whatif I make a program. It assigns where something should be encrypted or not. Then a key is generated that con
## I basically need to find out how to reverse back the text. And use a passcode to do that

## so key plus