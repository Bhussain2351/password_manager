from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


letters = [
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M',
'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = [
'!','@','#','$','%','^','&','*','(',')',
'-','_','=','+','[',']','{','}',';',':',
'"',"'",'<','>','.',',','?','/','\\','|','`','~'
]
def generate():
    n_letters=[choice(letters) for _ in range(4)]
    n_numbers=[choice(numbers) for _ in range(4)]
    n_symbols=[choice(symbols) for _ in range(4)]

    password_list=n_letters+n_numbers+n_symbols
    shuffle(password_list)

    password="".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)

def save():

    website=website_entry.get()
    username=username_entry.get()
    password=password_entry.get()
    if len(website)==0  or len(password)==0:
        messagebox.showinfo(title="opps", message="Please don't left anything unfilled")


    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nUsername: {username}"
                                                              f"\nPassword: {password}\nIs it Ok to save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website}|{username}|{password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)



window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=30)

canvas=Canvas(height=200,width=400)
logo=PhotoImage(file="logo.png")
canvas.create_image(175,150,image=logo)
canvas.grid(row=0,column=1)


website_label=Label(text="Enter website address:")
website_label.grid(row=1,column=0)


username_label=Label(text="username/Email ID:")
username_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry=Entry(width=50)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

username_entry=Entry(width=50)
username_entry.insert(END,"@gmail.com")
username_entry.grid(row=2,column=1,columnspan=2)

password_entry=Entry(width=50)
password_entry.grid(row=3,column=1,columnspan=1)

generate_password_button=Button(text="Generate Password",width=42,highlightthickness=0,command=generate)
generate_password_button.grid(row=4,column=1,columnspan=2)

add_password_button=Button(text="Add Password",width=42,highlightthickness=0,command=save)
add_password_button.grid(row=5,column=1)












window.mainloop()