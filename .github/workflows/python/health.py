import requests
import smtplib, ssl
from email.message import EmailMessage
from requests.exceptions import HTTPError

def checkURLs():
    # for url in ['https://api.github.com', 'https://api.github.com/invalid', 'http://adfkjladslkdfas.com/']:
    for url in ['https://api.github.com', 'https://api.github.com/invalid']:
        try:
            print (url)
            response = requests.get(url)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
            print(f'Send email with url:  {url}  & status code :  {response.status_code}')  
            # send notification if error
#            sendMail(url, response.status_code)
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
            print(f'Send email with url:  {url}  & status code :  {response.status_code}')  
            # send notification if error
#            sendMail(url, response.status_code)
        else:
            print('Success!')


def sendMail(url, code):
    # https://www.wpoven.com/tools/free-smtp-server-for-testing
    port = 25
    smtp_server = "smtp.freesmtpservers.com"
    sender_email =  "juan@testing.com"
    receiver_email = "xxxxxxx@gmail.com"  # Enter receiver address
    subject = "Testing from python"
#    password = "1234567890abcdefgh"
    message = """\
    Subject: Hi there

    This message is sent from Python."""


    server = smtplib.SMTP(smtp_server)
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(message)

    server.send_message(msg)


#    try:    
#        smtpObj = smtplib.SMTP(smtp_server,port)    
#    #    smtpObj.login(sender_email,password)    
#        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
#        smtpObj.sendmail(sender_email, receiver_email, message)    
#        print("Successfully sent email")    
#    except Exception as e:    
#        print("Error: unable to send email")    
#        print(e)

    # Create a secure SSL context
#    context = ssl.create_default_context()

#    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#        server.login(sender_email, password)
#        server.sendmail(sender_email, receiver_email, message)


checkURLs()


