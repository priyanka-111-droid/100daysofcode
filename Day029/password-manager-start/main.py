from tkinter import *
from tkinter import messagebox 
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#edited password generator code made in Day5 so that we don't have to type anything from console
#copy pasted day5.py code
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list1=[random.choice(letters) for char in range(nr_letters)]
    password_list2=[random.choice(symbols) for char in range(nr_symbols)]
    password_list3=[random.choice(numbers) for char in range(nr_numbers)]
    password_list=password_list1+password_list2+password_list3

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    #convert to string like this instead of above loop(more pythonic)
    password_answer="".join(password_list)

    # print(f"Your password is: {password}")

    #display password_answer in password entry
    password.insert(0,password_answer)

    #using pyperclip to copy text we want to place in clipboard
    pyperclip.copy(password_answer)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    count=0
    website_answer=website.get().title()
    email_answer=email.get()
    pass_answer=password.get()

    if(len(website_answer)==0 or len(pass_answer)==0 or len(email_answer)==0):
        #if any of the entry fields is left empty,show an error
        #using messagebox
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        is_ok=messagebox.askokcancel(title=website_answer,message=f"These are details entered:\nEmail: {email_answer}\nPassword: {pass_answer}\nIs it ok to save?")
        if is_ok:

            with open("Day029/password-manager-start/data.txt",mode="r") as f:
                data=f.readlines()
                for line in data:
                    lis=line.split("|")
                    if(lis[0].strip(" ")==website_answer):
                        if(lis[1].strip(" ")==email_answer):
                            count=1


            if(count==0):
                #if website entered is not already present in data.txt file
                with open("Day029/password-manager-start/data.txt",mode="a") as f:
                    f.write(f"{website_answer} | {email_answer} | {pass_answer}\n")

                
            else:
                messagebox.showinfo(title="Oops",message="You have already saved a password for this website using the same email!")

            #you can delete before inserting new text again
            website.delete(0,END) #delete from 0th char to last char of website entry
            # email.delete(0,END)
            password.delete(0,END)

            

#-----------------------------REMOVE PASSWORD-------------------------- #
def remove_password():
    count=0
    website_answer=website.get().title()
    email_answer=email.get()

    if(len(website_answer)==0 or len(email_answer)==0):
        messagebox.showinfo(title="Oops",message="Please enter the name of website and email!")
    else:

        with open("Day029/password-manager-start/data.txt",mode="r") as f:
            data=f.readlines()
        with open("Day029/password-manager-start/data.txt",mode="w") as f:
            for line in data:
                lis=line.split("|")
                if(lis[0].strip(" ")!=website_answer):
                    f.write(line)
                else:
                    #if website name matches,we need to check if email is also matching or not
                    if(lis[1].strip(" ")!=email_answer):
                        f.write(line)
                    else:
                        count=1

        if(count==1):
            messagebox.showinfo(title="Successful",message="Password for website deleted successfully!")

        else:
            messagebox.showinfo(title="Oops",message="Website not found,please check spelling or try another website")


        website.delete(0,END) #delete from 0th char to last char of website entry
        password.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas=Canvas(width=200,height=200)
lock_logo=PhotoImage(file="Day029/password-manager-start/logo.png")
canvas.create_image(100,100,image=lock_logo)
canvas.grid(column=1,row=0) #please don't forget to specify layout for canvas!!


#Label and Entry for website
website_label=Label(text="Website: ")
website_label.grid(column=0,row=1)

website=Entry(width=42)
website.grid(column=1,row=1,columnspan=2)
website.focus()

#Label and entry for email/username
email_label=Label(text="Email/Username: ")
email_label.grid(column=0,row=2)

email=Entry(width=42)
email.grid(column=1,row=2,columnspan=2)
email.insert(0,"xyz@gmail.com")

#Label and Entry for password
pass_label=Label(text="Password")
pass_label.grid(column=0,row=3)

password=Entry(width=26)
password.grid(column=1,row=3)

button=Button(text="Generate password",command=generate_password)
button.grid(column=2,row=3)

#Button to add
add_button=Button(text="Add",width=42,command=add_password)
add_button.grid(column=1,row=4,columnspan=2)

#Button to remove password
remove_button=Button(text="Remove",width=42,command=remove_password)
remove_button.grid(column=1,row=5,columnspan=2)


window.mainloop()