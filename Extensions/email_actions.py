import smtplib
import os

MY_EMAIL = os.environ['MY_EMAIL']
MY_PASSWORD = os.environ['MY_PASSWORD']


class EmailActions:
    @staticmethod
    def send_new_email(sendTo, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=sendTo, msg=message)
            print("Email sent successfully!")