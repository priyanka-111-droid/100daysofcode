import os,smtplib,random,datetime as dt

my_email=os.environ.get('MY_EMAIL')
password=os.environ.get('PASSWORD')

with open("Day032/Exercise/quotes.txt") as q_file:
    data=q_file.readlines()

now=dt.datetime.now()
weekday=now.weekday()
if(weekday==0):
    connection=smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()#encrypts message so other ppl can't read
    connection.login(user=my_email,password=password)

    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject:Monday motivation\n\n{random.choice(data)}"
    )

    connection.close()

