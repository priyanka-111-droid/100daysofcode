import os,smtplib

my_email=os.environ.get('MY_EMAIL')
password=os.environ.get('PASSWORD')
connection=smtplib.SMTP("smtp.gmail.com", port=587)
# smtp.mail.yahoo.com(for YAHOO)

receiver=os.environ.get('RECEIVER')

connection.starttls()#encrypts message so other ppl can't read
connection.login(user=my_email,password=password)
#add a subject else will go to spam
connection.sendmail(
    from_addr=my_email,
    to_addrs=receiver,
    msg="Subject:Hello\n\nThis is the body of my email."
)

connection.close()

