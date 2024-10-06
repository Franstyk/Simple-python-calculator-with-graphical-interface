from tkinter import *

# Create the main window
root = Tk()
root.title("Simple Calculator")

# Create an entry widget for the display
entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button click function
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))

# Define clear function
def button_clear():
    entry.delete(0, END)

# Define equal function
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Define button creation function
def create_button(text, row, column, command):
    button = Button(root, text=text, padx=20, pady=20, command=command)
    button.grid(row=row, column=column)

# Create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (text, row, column) in buttons:
    if text == '=':
        create_button(text, row, column, button_equal)
    elif text == 'C':
        create_button(text, row, column, button_clear)
    else:
        create_button(text, row, column, lambda t=text: button_click(t))

# Run the main loop
root.mainloop()
