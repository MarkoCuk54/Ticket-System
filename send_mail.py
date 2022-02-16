# from email import message
# import smtplib
# from email.mime.text import MIMEText


# def send_mail(customer, dealer, rating, comments):
#     port = 2525
#     smtp_server = 'smtp.mailtrap.io'
#     login = '1e30343fd4210c'
#     password = '97b1b40c26ce17'
#     message = f"<h3>NOVI TIKET</h3><ul><li>Korisnik: {customer}</li><li>Problem: {dealer}</li><li>Hitno?: {rating}</li><li>Opis: {comments}</li></ul>"

#     sender_email = 'email1@example.com'
#     receiver_email = 'marko.cuk.888@gmail.com'
#     msg = MIMEText(message, 'html')
#     msg['Subject'] = 'Tiket'
#     msg['From'] = sender_email
#     msg['To'] = receiver_email

#     # Send email
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.login(login, password)
#         server.sendmail(sender_email, receiver_email, msg.as_string()) 
        
    
