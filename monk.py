import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
eng = pyttsx3.init('sapi5')
voices = eng.getProperty('voices')
eng.setProperty('voices', voices[1].id)

def speak(audio):
    eng.say(audio)
    print(audio)
    eng.runAndWait()

def listencommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Interpreting your commands....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1.5,phrase_time_limit=5)

    try:
        print("Recognizing your voice...")
        speak("Recognizing your voice...")
        query =  r.recognize_google(audio , language='en-in')
        speak("Voice Access succesful , executing the command...")
        print(f" Your command was: {query}")

    except Exception as e:
        speak("Sir, please repeat your command ...")
        return "none"
    return query

def greetings():
    hour = int (datetime.datetime.now().hour)

    if hour >=0 and hour <=12:
        speak("Good Morning , Swarnavo ")
        speak(f"Currently the time is: {hour} a.m ")
    elif hour >12 and hour <18:
        speak("Good afternoon, Swarnavvo")
        speak(f"Currently the time is: {hour} p.m ")
    else:
        speak("Good evening, Swarnavo")
        speak(f"Currently the time is: {hour} p.m ")
def sendEmail(to,cont):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('swarnavomukherjee03@gmail.com', 'daft iuyk gkyx fmeh')
    server.sendmail('swarnavomukherjee03@gmail.com',to, cont)
    server.close()





if __name__ == "__main__":
    greetings()
    speak("Welcome , this is monk , how may i help you ? ")

    while True:
        query = listencommand().lower()
        if "open notepad" in query:
            path = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(path)
        elif "open brave" in query:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk"
            os.startfile(path)

        elif "play music" in query:
            music_dir = "E:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        elif "tell my ip" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Sir, Your IP address is {ip}")
        elif " wikipedia" in query:
            speak("Searching in wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia sources")
            speak(results)
            print(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open guitar" in query:
            webbrowser.open("www.github.com")
        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?ogbl#inbox")
        elif "open google" in query:
            speak("What would u like to search on google sir.....")
            str = listencommand().lower()
            webbrowser.open(f"{str}")
        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+917595948490","this is testing message",datetime.datetime.now().hour,datetime.datetime.now().minute+2)
        elif "play song in youtube" in query:
            kit.playonyt("Love me like u do")




        elif "send email" in query:
            try:
                speak("sir, what should i say in the mail")
                cont = listencommand().lower()
                to = "mukherjeechandrasis@gmail.com"
                sendEmail(to,cont)
                speak("Sir, i have succesfully send the email")

            except Exception as e:
                print(e)
                speak("Unfortunately i cant send the mail, sir ")

        elif "no thanks " in query:
            sys.exit()







        speak("sir, is there anything else u want me to do")


















