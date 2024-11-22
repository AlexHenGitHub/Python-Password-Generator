#Programmer: Alexander Henriquez
#Purpose of this program is to generate a password for the user with a gui interface
#Data: Ongoing
from tkinter import *
import random

root = Tk()
root.title('Password Generator')
root.geometry("720x480")  # window size

password_list = [

        '/', '#', ')', '(', ':', ';', ',', '?', '$', '%', '&', '+', '*', '{', '}', '[', ']',
        '.', '=', '<', '>', '-', '_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c',
        'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'

    ]
# password generator function
def passgen():

    # this stops the password from stacking on itself after more than 1 use
    inputbox = Entry()
    uno = 1
    new_password_list = password_list[23:85]
    for passloop in range(uno):
        empty = ""
        num_of_slide = slider.get()
        if int(num_of_slide) > 0:
            if var.get() == 0:
                for numbero in range(int(num_of_slide)):
                    list_result = new_password_list[random.randint(0, 61)]
                    empty = empty + list_result
            else:
                for numbero in range(int(num_of_slide)):
                    list_result = password_list[random.randint(0, 84)]
                    empty = empty + list_result  # if empty changes to a different name the output is different???
        else:
            inputbox.insert(0, "Please move to slider to a valid number")

        inputbox.insert(0, empty)
        inputbox.grid(row=6, pady=30, ipadx=285)


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

# check box
var = IntVar()
Checkbutton(root,
            text="Do you want to include special character?" + '\n' + "That includes " + "\\" + "!#$%^&*()-=+_[]"
                                                                                                "{}'"'"'":;?/.,<>",
            variable=var).grid(column=0, row=4, ipady=30)

# password generator button
Button(root, text="Generate Password", bg='BLACK', fg='PINK', command=passgen).grid(column=0, row=5, ipady=5, ipadx=285)
# input box
inputbox = Entry()
inputbox.grid(row=6, pady=30, ipadx=285)

root.mainloop()





