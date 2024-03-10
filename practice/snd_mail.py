import smtplib

my_email = "namith230@gmail.com"
password = "bkbrecjvninbciyi"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="inamith23@gmail.com",
    msg="Subject:hello\n\nThis is me")
connection.close()