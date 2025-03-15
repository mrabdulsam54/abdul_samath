# Word Correction tool
from textblob import TextBlob
from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.iconbitmap(r'C:\Users\abdul.samath\Downloads\dictionary.ico')
root.title("Word Correction Tool by Samath")
root.geometry('600x350')

bg = ImageTk.PhotoImage(Image.open(r"C:\Users\abdul.samath\Documents\image\bg1.png"))
label = Label(root, image=bg, width=610, height=610)
label.place(x=0, y=0)

entry = Entry(root, width=90, borderwidth=5, fg='black', bg='white')
entry.insert(0, 'Enter your sentence here!')
entry.grid(row=0, column=0, columnspan=3, padx=30, pady=30)

final = Entry(root, width=90, borderwidth=5, fg='black', bg='white')
final.grid(row=1, column=0, columnspan=3, padx=30, pady=30)


def correct_func():
    words = entry.get()
    word_list = words.split(" ")
    corrected_words = []
    output = []
    for i in word_list:
        corrected_words.append(TextBlob(i))
    for j in corrected_words:
        a = j.correct()
        output.append(str(a))
    final.insert(0, str(" ".join(output)))


def clear_func():
    final.delete(0, END)
    entry.delete(0, END)


Correct_button = Button(root, text='Correct', padx=20, pady=10, command=correct_func, bg='orange', font='bold')
Correct_button.grid(row=2, column=0)

Clear_button = Button(root, text='Clear', padx=20, pady=10, command=clear_func, bg='orange', font='bold')
Clear_button.grid(row=2, column=2)

root.mainloop()


