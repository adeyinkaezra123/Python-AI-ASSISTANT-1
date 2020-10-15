import random 
import pyttsx3 #pip install pyttsx3
import psutil
import datetime
from datetime import date
from googletrans import Translator, constants
from pprint import pprint
import subprocess
import tkinter
# from ecapture import ecapture as ec 
import requests, json
import speech_recognition as sr
import wikipedia
import smtplib
import wolframalpha
import webbrowser 
from googlesearch import *
import os
# from ecapture import ecapture as ec 

name = "Jarvis"
engine = pyttsx3.init()
engine.say("This is jarvis")
engine.runAndWait()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def jarvisResponse(audio):
    print(audio)
    for line in audio.splitlines():
        os.system('say'+ audio)


# define the countdown func. 
def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Fire in the hole!!') 
  
  



def time():
    Time  = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)


def date():
    from datetime import date
    # year = int(datetime.datetime.now().year)
    # month = int(datetime.datetime.now().month)
    # date = int(datetime.datetime.now().day)
    today = date.today()
    d2 =today.strftime("%B, %d, %Y")
    speak("Today's date is...")
    print(d2)
    speak(d2)


def greetings():
    speak ('Welcome back sir !!')
    time()
    date()

    hour =int(datetime.datetime.now().hour)
    if hour >= 6 and hour <12:
        print("Good morning sir!")
        speak("Good morning sir!")
    elif hour >= 12 and hour <18:
        print("Good afternoon sir")
        speak("Good afternoon sir!")
    else:
        print("Good evening sir!!")
        speak("Good evening sir!!")
        

    print("This is jarvis reporting for duty")
    speak("This is jarvis reporting for duty!")
    print("Initializing jarvis!")
    speak("Initializing jarvis")
    print("Initialization complete")
    speak("Initialization complete")


    print("Waiting for your command sir...!")
    speak("Waiting for your command sir...!")





def takeCommand():
    r = sr.Recognizer()
    r.energy_threshold = 1000
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return takeCommand()
    return query

def sendmail(to, content):

