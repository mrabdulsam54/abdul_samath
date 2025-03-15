# Source code of Currency conversion tool
from forex_python.converter import CurrencyRates
from tkinter import *
from PIL import ImageTk, Image
import webbrowser
root = Tk()
root.title("Currency Conversion Tool by Samath")
root.iconbitmap(r'C:\Users\abdul.samath\Downloads\currency.ico')
root.geometry('800x520')
Background_image = ImageTk.PhotoImage(Image.open(r'C:\Users\abdul.samath\Downloads\Hnet.com-image.jpg'))
my_image_label = Label(root, image=Background_image)
my_image_label.place(x=0, y=0)
# root.wm_attributes('-transparentcolor', '#F0F8FF')
root.configure(bg='#F0F8FF')


# Defining the currency conversion process
def currency_conversion():
    c = CurrencyRates()
    money = float(amount.get())
    from_currency = str(from_entry.get().upper())
    to_currency = str(to_entry.get().upper())
    global print_form
    if len(from_currency) != 3 or len(to_currency) != 3:
        Result.insert(0, 'Invalid Codes. Please check!')
    else:
        try:
            converted_value = c.convert(from_currency, to_currency, money)
            print_form = f"{round(converted_value, 3)} {to_currency}"
            # print(print_form)
        except BaseException as e:
            print_form = f"{e}. Sorry, this conversion is currently not available"
            # print(f"{e}. Sorry, this conversion is currently not available")
        Result.insert(0, print_form)


# Using Clear function to remove the entries
def clear_func():
    to_entry.delete(0, END)
    from_entry.delete(0, END)
    amount.delete(0, END)
    Result.delete(0, END)
    to_entry.insert(0, 'Enter your "to" currency code')
    from_entry.insert(0, 'Enter your "from" currency code')
    amount.insert(0, 'Enter the amount here')


# Hyperlink function
def callback(url):
    webbrowser.open_new_tab(url)


welcome_text = '''
Welcome to the currency conversion tool. 
Type your from and to currency code in the below and get 
the latest conversion rates!
'''
address = Label(root, text=welcome_text, bg='#F0F8FF', fg='black', font='bold')
address.grid(row=0, column=1)

# Buttons and Entries creation
amount = Entry(root, width=30, borderwidth=5, bg='#F0F8FF', fg='dark green')
amount.grid(row=1, column=0)
amount.insert(0, 'Enter the amount here')

from_entry = Entry(root, width=30, borderwidth=5, bg='#F0F8FF', fg='dark green')
from_entry.grid(row=1, column=1)
from_entry.insert(0, 'Enter your "from" currency code')

in_bet_image = ImageTk.PhotoImage(Image.open(r'C:\Users\abdul.samath\Downloads\rsz_1convert_image.jpg'))
in_bet_label = Label(root, image=in_bet_image, bg='#F0F8FF')
in_bet_label.grid(row=2, column=1)

to_entry = Entry(root, width=30, borderwidth=5, bg='#F0F8FF', fg='dark green')
to_entry.grid(row=1, column=2)
to_entry.insert(0, 'Enter your "to" currency code')

Convert_button = Button(root, text='Convert', padx=20, pady=7, fg='black', bg='orange', command=currency_conversion)
Convert_button.grid(row=3, column=1)

Clear_button = Button(root, text='Clear', padx=20, pady=7, fg='black', bg='orange', command=clear_func)
Clear_button.grid(row=4, column=1)

Fill_up = Label(root, text='Please find the results below!', bg='#F0F8FF', fg='black')
Fill_up.grid(row=5, column=1)

Result = Entry(root, width=52, borderwidth=5, bg='#F0F8FF', fg='dark red')
Result.grid(row=6, column=1)

Help = Label(root, text='Most popular currency codes:', font='bold', fg='black', bg='#F0F8FF')
Help.grid(row=7, column=1)

currency_code_details = Label(root, text='Check here for more codes:', fg='black', bg='#F0F8FF', font='bold')
details_link = Label(root, text='code_link', font=('Helveticabold'), fg="dark green", cursor="hand2", bg='#F0F8FF')

currency_code_details.grid(row=7, column=0)
details_link.grid(row=8, column=0)
details_link.bind("<Button-1>", lambda e: callback('https://www.iban.com/currency-codes'))

popular_codes = '''
USD: American Dollars
INR: Indian Rupees
EUR: European Pounds
YEN: Japanese Yen
CNY: Chinese Yuan Renminbi
AED: UAE Dirhams
NZD: New Zealand Dollars
AUD: Australian Dollars
QAR: Qatari Rial
KWD: Kuwaiti Dinar
'''
label_popular_code = Label(root, text=popular_codes, bg='#F0F8FF', fg='dark green')
label_popular_code.grid(row=8, column=1)

root.mainloop()
