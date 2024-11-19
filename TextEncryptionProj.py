#Programmer: Alexander Henriquez
#Purpose of this program is to do basic text encryption
#Data: 11/18/2024


import random

from numpy.lib.user_array import container

while True:

# Get user input
    userinput = input("Type anything: ")




    if userinput:
        key = random.randint(-10000000000000000000000000000*10000000000000000000000000000,
                         10000000000000000000000000000 * 10000000000000000000000000000)
    print(key)
    again = input("Do you want to go again 1 = yes, 0 = no")



    if again == "1" :
        continue

    else:
        print("End")
        break




'''
# Convert the input into a list of characters
char_list = list(userinput)

# Shuffle the list of characters
random.shuffle(char_list)

# Join the shuffled list back into a string
scrambled_output = ''.join(char_list)

# Print the scrambled output
print("Scrambled Output:", scrambled_output)
print()
'''