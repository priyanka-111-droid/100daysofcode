from tkinter import *
from tkinter import messagebox 
import random
import pyperclip
import json

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
    #TODO 2.Create new dictionary
    new_data={
        website_answer:{
            "email":email_answer,
            "password":pass_answer,
        }
    }


    if(len(website_answer)==0 or len(pass_answer)==0 or len(email_answer)==0):
        #if any of the entry fields is left empty,show an error
        #using messagebox
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:

        #TODO 1.Remove the message box to make code simpler
        # is_ok=messagebox.askokcancel(title=website_answer,message=f"These are details entered:\nEmail: {email_answer}\nPassword: {pass_answer}\nIs it ok to save?")
        # if is_ok:


        #TODO 5. Use json.load() to read data and see if website already has password saved for it
        # with open("Day030/Project/password-manager-start/data.txt",mode="r") as f:
        #     data=f.readlines()
        #     for line in data:
        #         lis=line.split("|")
        #         if(lis[0].strip(" ")==website_answer):
        #             if(lis[1].strip(" ")==email_answer):
        #    
        #              count=1

        # TODO 7:Handle FileNotFoundError(assume data.json file has not been created yet and we are trying to read from it)
        try:
            with open("Day030/Project/password-manager-start/data.json",mode="r") as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            with open("Day030/Project/password-manager-start/data.json",mode="w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            if(website_answer in data.keys()):
                if(email_answer==data[website_answer]["email"]):
                    count=1



        if(count==0):
            #TODO 3.Import json module, write to data.json file using json.dump()
            #if website entered is not already present in data.txt file
            # with open("Day030/Project/password-manager-start/data.json",mode="w") as data_file:
            #     json.dump(new_data,data_file,indent=4)


            #TODO 4.Now we want to update new data as only write mode will delete previous data before inserting new data 
            with open("Day030/Project/password-manager-start/data.json",mode="r") as data_file:
               #Reading old data
               data=json.load(data_file)
               #Update old data with new data
               data.update(new_data)

            with open("Day030/Project/password-manager-start/data.json",mode="w") as data_file:
                #Saving updated data
                json.dump(data,data_file,indent=4)
        
        else:
            messagebox.showinfo(title="Oops",message="You have already saved a password for this website using the same email!")

        #you can delete before inserting new text again
        website.delete(0,END) #delete from 0th char to last char of website entry
        # email.delete(0,END)
        password.delete(0,END)


#-----------------------------REMOVE PASSWORD-------------------------- #
def remove_password():
    website_answer=website.get().title()


    if(len(website_answer)==0 ):
        messagebox.showinfo(title="Oops",message="Please enter the name of website!")
    else:
        
        #TODO 6. Remove password saved when user types website name
        # with open("Day030/Project/password-manager-start/data.txt",mode="r") as f:
        #     data=f.readlines()
        # with open("Day030/Project/password-manager-start/data.txt",mode="w") as f:
        #     for line in data:
        #         lis=line.split("|")
        #         if(lis[0].strip(" ")!=website_answer):
        #             f.write(line)
        #         else:
        #             #if website name matches,we need to check if email is also matching or not
        #             if(lis[1].strip(" ")!=email_answer):
        #                 f.write(line)
        #             else:
        #                 count=1


        #TODO 8.Handle Exceptions here for FileNotFound
        try:
            with open("Day030/Project/password-manager-start/data.json",mode="r") as data_file:
                #Reading old data
                data=json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Oops",message="Website not found,please check spelling or try another website")
        else:
            if(website_answer in data.keys()):
                #Delete all data of the website
                data.pop(website_answer)
                messagebox.showinfo(title="Successful",message="Password for website deleted successfully!")

            with open("Day030/Project/password-manager-start/data.json",mode="w") as data_file:
                #Saving updated data
                json.dump(data,data_file,indent=4)

        finally:
            website.delete(0,END) #delete from 0th char to last char of website entry
            password.delete(0,END)

#-----------------------------SEARCH PASSWORD---------------------------#
def search_password():
    website_answer=website.get().title()

    if(len(website_answer)==0 ):
        messagebox.showinfo(title="Oops",message="Please enter the name of website!")
    else:
        try:
            with open("Day030/Project/password-manager-start/data.json",mode="r") as data_file:
                #Reading old data
                data=json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Oops",message="Website not found,sorry!")
        else:
            if(website_answer in data.keys()):
                req_email=(data[website_answer]["email"])
                req_password=(data[website_answer]["password"])
                messagebox.showinfo(title=f"{website_answer}",message=f"Email: {req_email}\nPassword: {req_password}")

        finally:
            website.delete(0,END)


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

website=Entry(width=26)
website.grid(column=1,row=1)
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

#Button to search for website
search_button=Button(text="Search",command=search_password)
search_button.grid(column=2,row=1)
search_button.config(padx=40,pady=0)

window.mainloop()