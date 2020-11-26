import smtplib


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("kalyan.santra29@gmail.com", "tlqzeuwqmqojfeoh")
    subject = "This is a email sent from a python program"
    body = "Hey you get this Message. Wow! it's really works. This mail I send from my python programme."
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail("kalyan.santra29@gmail.com", "reacto.gaming29@gmail.com", msg)
    print("EMAIL HAS BEEN SENT")
    server.quit()


send_email()
