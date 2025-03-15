#Simple email automation
import os
import imghdr
import smtplib
from email.message import EmailMessage
address = os.environ.get('EMAIL_ADDRESS')
password = os.environ.get('EMAIL_PASSWORD')
print(address)
print(password)
url = "https://www.youtube.com/watch?v=JRCJ6RtE3xU"
message = EmailMessage()
message['Subject'] = 'Check out your passport size photo!'
message['From'] = address
message['To'] = 'mrabdulsam54@gmail.com'
content = '''
Hi Abdul Samath,

   Greetings from GCT SRF! Please check your passport size photo in the attachment. This is an automated email and don't right back to us.
   
Thanks,
GCT SRF.
'''
message.set_content(content)
with open(r'C:\Users\abdul.samath\Documents\Personal Documents\samath_photo_white_background.jpg', 'rb') as image:
    file = image.read()
    file_type = imghdr.what(image.name)
    file_with_name = "Samath_Passport_Photo"
message.add_attachment(file, maintype='image', subtype=file_type, filename=file_with_name)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(address, password)
server.send_message(message)
print("Mail sent")
