import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
import os


msg = EmailMessage()
address = os.environ.get('EMAIL_ADDRESS')
password = os.environ.get('EMAIL_PASSWORD')
listener = sr.Recognizer()
engine = pyttsx3.init()
email_list = {"Myself" : "mrabdulsam54@gmail.com", "Official" : "gctsrf@gmail.com"}


def voice_data():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("Hey I am Listening, You can speak now....")
            #print("\n")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            content = str(info).capitalize()
            print(content)
            print("\n")
            return content
    except BaseException as e:
        pass


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_mail_info():
    talk('Who is the receiver of the mail?')
    name = voice_data()
    receiver = email_list[name]
    print(receiver)
    print("\n")
    talk('What is your subject line of the mail?')
    subject = voice_data()
    talk('Tell me what you would like to share to the receiver?')
    content = voice_data()
    msg['From'] = address
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.set_content(content)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(address, password)
    server.send_message(msg)
    print("Mail sent")
    talk('Your mail has been sent successfully!')


get_mail_info()





