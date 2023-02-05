import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
engine.say(text)
engine.runAndWait()

def get_info():
try:
with sr.Microphone() as source:
print('listening...')
voice = listener.listen(source)
info = listener.recognize_google(voice)
print(info)
return info.lower()
except:
pass

def send_email(receiver, subject, message):
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('projectblind111@gmail.com', 'Project@1,' )
email = EmailMessage()
email['From'] = 'projectblind111@gmail.com'
email ['To'] = receiver
email['Subject'] = subject
email.set_content(message)
server.send_message(email)

email_list = {
'good': 'aganglas11@gmail.com',
'better': 'amishaganglas@gmail.com',
'best': 'aganglas1108@gmail.com',
}

def get_email_info():
talk('to whom you want to send email')
name = get_info()
receiver = email_list[name]
print(receiver)
talk('what is the subject of your mail?')

subject = get_info()
talk('tell me the content of your mail')
message = get_info()
send_email(receiver, subject, message)
talk('Your email has been sent')
talk('Do you want to send more email?')
send_more = get_info()
if 'yes' in send_more:
get_email_info()

get_email_info()
