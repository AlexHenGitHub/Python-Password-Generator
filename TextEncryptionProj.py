#Programmer: Alexander Henriquez
#Purpose of this program is to do basic text encryption
#Data: 11/18/2024


import random

import tkinter as tk

def display_input():
    # Get the text from the entry box
    user_text = entry.get()
    # Update the label with the user's input
    output_label.config(text=f"You typed: {user_text}")

# Create the main window
root = tk.Tk()
root.title("Simple Python GUI")
root.geometry("300x200")  # Set window size

# Add a label for instructions
label = tk.Label(root, text="Type something and click Submit:")
label.pack(pady=10)

# Add an entry widget for user input
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Add a button to trigger the display_input function
button = tk.Button(root, text="Submit", command=display_input)
button.pack(pady=10)

# Add a label to display the output
output_label = tk.Label(root, text="", fg="blue")
output_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()







'''   
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
        key = random.randint(-10000000000000000000000000000 * 10000000000000000000000000000,
                             10000000000000000000000000000 * 10000000000000000000000000000)
    print(key)
    print()
    print("Scrambled Output:", scrambled_output, "non scrambled input:", userinput)
    userinput

    again = input("Do you want to go again 1 = yes, 0 = no")

    if again == "1":
        continue

    else:
        print("End")
        break
'''
## need a way to see how the text was changed and track it


## maybe make an if statment that compares input vs scambled text aand that
## can be the bases for the decrypter


##w\whatif I make a program. It assigns where something should be encrypted or not. Then a key is generated that con
## I basically need to find out how to reverse back the text. And use a passcode to do that

## so key plus
