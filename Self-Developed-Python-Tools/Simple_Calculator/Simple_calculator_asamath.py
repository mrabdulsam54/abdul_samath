# Simple Calculator by Samath
from tkinter import *
root = Tk()
root.title('Simple Calculator by Samath')

# Creating input text box
entry = Entry(root, width=50, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Creating click action function
def click_button(number):
    current_num = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current_num) + str(number))


# Creating mathematical functions
def add_func():
    x_factor = entry.get()
    global f_num
    global math_function
    math_function = "addition"
    f_num = float(x_factor)
    entry.delete(0, END)


def sub_func():
    x_factor = entry.get()
    global f_num
    global math_function
    math_function = "subtraction"
    f_num = float(x_factor)
    entry.delete(0, END)


def mult_func():
    x_factor = entry.get()
    global f_num
    global math_function
    math_function = "multiplication"
    f_num = float(x_factor)
    entry.delete(0, END)


def div_func():
    x_factor = entry.get()
    global f_num
    global math_function
    math_function = "division"
    f_num = float(x_factor)
    entry.delete(0, END)


def clear_func():
    entry.delete(0, END)


def equal_func():
    x = entry.get()
    entry.delete(0, END)

    if math_function == "addition":
        value = float(x) + f_num
        value = "{:.2f}".format(value)
        if value.split(".")[1] == "00":
            entry.insert(0, value.split(".")[0])
        else:
            entry.insert(0, str(value))
    elif math_function == "subtraction":
        value = f_num - float(x)
        value = "{:.2f}".format(value)
        if value.split(".")[1] == "00":
            entry.insert(0, value.split(".")[0])
        else:
            entry.insert(0, str(value))
    elif math_function == "multiplication":
        value = float(x) * f_num
        value = "{:.2f}".format(value)
        if value.split(".")[1] == "00":
            entry.insert(0, value.split(".")[0])
        else:
            entry.insert(0, str(value))
    elif math_function == "division":
        value = f_num / float(x)
        value = "{:.2f}".format(value)
        if value.split(".")[1] == "00":
            entry.insert(0, value.split(".")[0])
        else:
            entry.insert(0, str(value))
    # print(value.split("."))
    # print(value.split(".")[1])
    # entry.insert(0, str(value))


# Creating Buttons
Button_1 = Button(root, text="1", padx=50, pady=25, command=lambda: click_button(1))
Button_2 = Button(root, text="2", padx=50, pady=25, command=lambda: click_button(2))
Button_3 = Button(root, text="3", padx=50, pady=25, command=lambda: click_button(3))

Button_4 = Button(root, text="4", padx=50, pady=25, command=lambda: click_button(4))
Button_5 = Button(root, text="5", padx=50, pady=25, command=lambda: click_button(5))
Button_6 = Button(root, text="6", padx=50, pady=25, command=lambda: click_button(6))

Button_7 = Button(root, text="7", padx=50, pady=25, command=lambda: click_button(7))
Button_8 = Button(root, text="8", padx=50, pady=25, command=lambda: click_button(8))
Button_9 = Button(root, text="9", padx=50, pady=25, command=lambda: click_button(9))

Button_0 = Button(root, text="0", padx=50, pady=25, command=lambda: click_button(0))
Button_plus = Button(root, text="+", padx=50, pady=25, command=add_func)
Button_equal = Button(root, text="=", padx=50, pady=25, command=equal_func)

Button_clear = Button(root, text="clear", padx=42, pady=25, command=clear_func)
Button_multiply = Button(root, text="*", padx=50, pady=25, command=mult_func)
Button_divide = Button(root, text="/", padx=50, pady=25, command=div_func)

Button_sub = Button(root, text="-", padx=50, pady=25, command=sub_func)
Button_dot = Button(root, text=".", padx=50, pady=25, command=lambda: click_button("."))

# Adding button positions
Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)

Button_0.grid(row=4, column=1)
Button_plus.grid(row=4, column=0)
Button_equal.grid(row=4, column=2)

Button_clear.grid(row=5, column=0)
Button_multiply.grid(row=5, column=1)
Button_divide.grid(row=5, column=2)

Button_sub.grid(row=6, column=0, columnspan=2)
Button_dot.grid(row=6, column=1, columnspan=2)

root.mainloop()
