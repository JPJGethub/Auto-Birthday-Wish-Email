import pandas
import datetime as dt
import random
import smtplib

#BIRTHDAY LIST
birthday = pandas.read_csv("birthdays.csv")
birthday_dict = birthday.to_dict(orient="records")

#RANDOM LETTER
letter_num = random.randint(1, 3)


#DATE AND TIME
current_date = dt.datetime.now()
month = current_date.month
day = current_date.day

for i in birthday_dict:
    if i["day"] == day and i["month"] == month:
        with open(f"letter_{letter_num}.txt") as letters:
            letter = letters.readlines()
            letter = ''.join(letter)
            new_letter = letter.replace("[NAME]", i["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            email_id = "*******.lang@gmail.com"
            password = "**********"
            connection.starttls()
            connection.login(user=email_id, password=password)
            connection.sendmail(from_addr=email_id, to_addrs=i["email"], msg=f"subject: Happy Birthday\n\n {new_letter}")
