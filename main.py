from tkinter import *
from tkinter import filedialog
from dictionary_attack import PDFcrack
import pyperclip
from brutforce import Brute

file_path = ""
passw_file_path = ""
passw = []
result = ""


def open_passlist():
    global passw_file_path
    passw_file_path = filedialog.askopenfilename()
    with open(passw_file_path, 'r') as f:
        global passw
        passw = f.read().splitlines()

def open_file():
    global file_path
    file_path = filedialog.askopenfilename()

def dictionary():
    global result
    if file_path:
        pdf_cracker = PDFcrack(file_path,passw)
        result = pdf_cracker.crack()
        result_label.config(text=f"Your PDF password is : {result}")
    else:
        result_label.config(text="Please select a PDF file first")

def copy():
    if result:
        pyperclip.copy(result)
# def brute_methode():
#     global result
#     if file_path:
#         brute_force = Brute(pdf_path=file_path, length=len, num_symbols=sym, num_letters=lett, num_numbers=num)
#         result = brute_force.brute_attack()
#         result_label.config(text=f"Your PDF password is : {result}")
#     else:
#         result_label.config(text="Please select a PDF file first")
def brute_methode():
    length = int(pass_length_entry.get())
    sym = int(symbols_entry.get())
    lett = int(letter_entry.get())
    num = int(numbers_entry.get())
    global result
    if file_path:
        brute_force = Brute(path=file_path, length=length, num_symbols=sym, num_letters=lett, num_numbers=num)
        result = brute_force.brute_attack()
        result_label.config(text=f"Your PDF password is : {result}")
    else:
        result_label.config(text="Please select a PDF file first")
     
root = Tk()
root.geometry("450x300")

open_pdf_btn = Button(text="Open pdf", command=open_file)
open_pdf_btn.place(x=20,y=0)

open_passw= Button(text="Open Password File", command=open_passlist)
open_passw.place(x=90,y=0)

dictionary_attack = Button(text="Dictionary Attack", command=dictionary)
dictionary_attack.place(x=220,y=0)

bruteforce_attack = Button(text="Bruteforce Attack",command=brute_methode)
bruteforce_attack.place(x=330,y=0)

result_label = Label(text=f"Your PDF password is : {result}")
result_label.place(x=20,y=50)

copy_btn = Button(text="Copy", command=copy)
copy_btn.place(x= 300,y=50)

pass_length_label = Label(text="Enter your password length")
pass_length_label.place(x=5,y=100)
pass_length_entry = Entry()
pass_length_entry.place(x=200,y=100)

symbols_label = Label(text="How many symbols are there")
symbols_label.place(x=5,y=150)
symbols_entry = Entry()
symbols_entry.place(x=200,y=150)

letter_label = Label(text="How many letters are there")
letter_label.place(x=5,y=200)
letter_entry = Entry()
letter_entry.place(x=200,y=200)

numbers_label = Label(text="How many numbers are there")
numbers_label.place(x=5,y=250)
numbers_entry = Entry()
numbers_entry.place(x=200,y=250)

root.mainloop()

