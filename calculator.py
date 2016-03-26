from Tkinter import *
from functools import partial

root = Tk()
root.title('Calculator')

# Text display
editor = Text(root, height=1, width=30)
editor.grid(row=0, column=0, columnspan= 4)

# Button functions
def clear():
    editor.delete(1.0, END)

def button_add(char):
    global calc
    calc = editor.get('1.0', 'end-1c')
    clear()
    if not calc.isalpha(): # To account for ERROR state
        editor.insert(END, calc+str(char))
    else:
        editor.insert(END, str(char))

def solve(arg): # Return bind passes an argument
    button_add(0) # solve() removes the last character of calc, so this adds a character for the purpose of being removed
    if len(calc) > 0:
        clear()
        try:
            editor.insert(END, str(eval(calc))) # I had A LOT of code written before I realized I could do eval()
        except:
            editor.insert(END, 'ERROR')

root.bind('<Return>', solve)

# Button initializations
def button_factory(char, row, column):
    button = Button(root, text=str(char), command=partial(button_add, str(char)))
    button.grid(row=row, column=column, sticky=N+S+E+W)

button_factory(7,1,0)
button_factory(8,1,1)
button_factory(9,1,2)
button_factory('/',1,3)
button_factory(4,2,0)
button_factory(5,2,1)
button_factory(6,2,2)
button_factory('*',2,3)
button_factory(1,3,0)
button_factory(2,3,1)
button_factory(3,3,2)
button_factory('-',3,3)
button_factory('.',4,2)
button_factory('+',4,3)

zero = Button(root, text='0', command=partial(button_add,'0'))
zero.grid(row=4, column=0, columnspan=2, sticky=N+S+E+W)

solve_button = Button(root, text='=', command=solve)
solve_button.grid(row=5, column=0, columnspan=3, sticky=N+S+E+W)

clear_button = Button(root, text='C', command=clear)
clear_button.grid(row=5, column=3, sticky=N+S+E+W)

for x in range(4):
    root.grid_columnconfigure(x, weight=1)

for y in range(5):
    root.grid_rowconfigure(y, weight=1)

root.mainloop()