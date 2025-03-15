#Email Automation
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('gctsrf@gmail.com','underresearch')
Subject = "Greetings from GCT SRF!"
body = '''
Hi Samath,
    Greetings from GCT SRF! We hope you are doing great. This is just yourself mailing to you to check whether email automation is happening fine.

Thanks,
GCT SRF.
'''
content = f'Subject: {Subject}\n\n{body}'
server.sendmail('gctsrf@gmail.com','mrabdulsam54@gmail.com', content)
print("Mail sent")