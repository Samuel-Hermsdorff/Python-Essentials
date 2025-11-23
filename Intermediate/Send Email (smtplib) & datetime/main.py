# import smtplib

# my_email = "samuelqhtoledo@gmail.com"
# password = "lamy cagc rdae hkfv"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="samuel.hermsdorff@aluno.ufabc.edu.br", 
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

import datetime as dt
import random as rd
import smtplib

MY_EMAIL = "samuelhermsdorff@gmail.com"
PASSWORD = "miuz mztq fsur ynvn"

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

if day_of_week == 0:
    with open(file="./quotes.txt", encoding="utf-8") as quotes_file:
        lines = quotes_file.readlines()
        quote = rd.choice(lines)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="samuel.hermsdorff@aluno.ufabc.edu.br",
            msg=f"Subject:Hello\n\n{quote}"
            )
# date_of_birth = dt.datetime(year=2001, month=3, day=9, hour=1)
