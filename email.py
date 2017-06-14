import smtplib

def send_email(to_address, msg):
    subject = "Recommended Recipes"

    text = msg

    receiver = to_address

    message = 'Subject: {}\n\n{}'.format(subject, text)


    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('iamnotasmith@gmail.com', 'iamnotasmith5')

    mail.sendmail('iamnotasmith@gmail.com', receiver, message)


    mail.close()






