import smtplib
from utilities.mailer import Mailer

class Mailer (Mailer):
    def __init__(
        self,
        username,
        password
    ):
        self.username = username
        self.password = password
    
    def email(
        self,
        recepient,
        subject,
        body
    ):
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(self.username, recepient, message)

    # TODO
    def close():
        pass

