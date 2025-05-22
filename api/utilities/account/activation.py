from utilities import mailer

def link():
    # TODO
    token = '...'

    return f"https://client.localhost/activate?token={token}"

def email(recepient):

    # TODO : ERROR HERE WITH mailer.context
    
    print(f"DEBUG:: {mailer}")

    return

    with mailer.context(
        mailer.PROVIDERS['GOOGLE']['APP_PASSWORD'],
        username="riosolved@gmail.com",
        password="123"
    ) as gmail:
        link = generate_link()

        message = f"""\
        From: {sender}
        To: {recepient}
        Subject: Notecrypt activation

        Activation link: {link}
        """

        # TODO
        # mailer.email()
