#Programmer: Alexander Henriquez
#Purpose of this program is to do basic text encryption
#Data: 11/18/2024


import random


# Get user input
userinput = input("Type anything: ")

# Convert the input into a list of characters
char_list = list(userinput)

# Shuffle the list of characters
random.shuffle(char_list)

# Join the shuffled list back into a string
scrambled_output = ''.join(char_list)

# Print the scrambled output
print("Scrambled Output:", scrambled_output)