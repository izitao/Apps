import pandas
import datetime as dt
import random
import smtplib


def letter_picker(name, sender, email_adress):
    '''Creates a letter'''

    letter_files = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    letter_file = random.choice(letter_files)

    with open(letter_file) as lf:
        letter = lf.read()

    letter = letter.replace("[NAME]", str(name))
    letter = letter.replace("[SENDER]", str(sender))

    send_letter(letter, email_adress)


def send_letter(letter, email_adress):
    '''Sends a letter to the specific person'''

    my_email = "ilovecreatingapps@gmail.com"
    password = "Apps123@"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_adress,
                            msg=f"Subject:Happy birthday!\n\n{letter}"
                            )


#INPUTS

sender = "Izitao"
persons = pandas.read_csv("birthdays.csv")

now = dt.datetime.today()

for index, row in persons.iterrows():
    if row.month == now.month:
        if row.day == now.day:
            letter_picker(row['name'], sender, row['email'])
