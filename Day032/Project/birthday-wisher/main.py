##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas,datetime as dt,random
import os,smtplib

data=pandas.read_csv("Day032/Project/birthday-wisher/birthdays.csv")

now=dt.datetime.now()
year=now.year
month=now.month
day=now.day

available_letters=['letter_1.txt','letter_2.txt','letter_3.txt']

my_email=os.environ.get('MY_EMAIL')
password=os.environ.get('PASSWORD')


for (index,row) in data.iterrows():
    if(row.month==month and row.day==day):
        birthday_name=(data.loc[index,'name'])
        receiver=row.email
        
        with open(f"Day032/Project/birthday-wisher/letter_templates/{random.choice(available_letters)}") as letter_f:
            letter_contents=letter_f.read()
            letter_contents=letter_contents.replace('[NAME]',birthday_name)

        connection=smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()#encrypts message so other ppl can't read
        connection.login(user=my_email,password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver,
            msg=f"Subject:Happy birthday!!\n\n{letter_contents}"
        )

        connection.close()






