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
    server = smptlib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('adeyinkaezra123@gmail.com','adeyinka123')
    server.sendmail('adeyinkaezra123@gmail.com', to, content)
    server.close()


if __name__ == "__main__": 
    greetings()
    while True:
        query = takeCommand().lower()

        if 'fuck' in query:
            speak("Fuck is a mean word")
            print("F**k is a mean word!")
        elif 'the time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Working on it sir!")
            speak("Searching wikipedia...")
            query = query.replace("Wikipedia"," ")
            result = wikipedia.summary(query, sentences= 3)
            print(result)
            speak(result)
        elif "Send email" in query:
            try:
                speak("What message do you want to send?")
                content = takeCommand().lower() 
                to ='adeyinkaezra123@gmail.com'
            # sendmail(to,content)
                speak("Working on it sir!")
                speak(content)
                speak("Email succesfully delivered")
            except Exception as e:
                print(e)
                speak("Sorry sir, Unable to deliver your mail!")


        elif 'change voice' in query:
            voices = engine.getProperty('voices')       #getting details of current voice
                #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
            engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
            speak("Voice changed succesfully")
        elif 'search google' in query:
            speak("what should I search for?")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            webbrowser.get(chrome_path).open_new_tab(search)
        elif 'shutdown' in query:
            os.system('shutdown -l')
        elif 'restart' in query:
            os.system('shutdown /r /t l')
 # Logic for executing tasks based on query
        elif 'who' in query:
            speak("Working on it sir!")
            print("Searching Google...")
            speak('Searching Google...')
            query = query.replace("google", "")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
                print("This is what I found according to your search")
                speak("This is what I found according to your search")
        elif 'remember that' in query:
            speak("What should I remember")
            data = takeCommand()
            speak("You asked me to remember that" + remember.read())
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close

        elif 'who are you' in query:
            print("I am here to do cool things for you!.\n Anyways, I am you A.I assistant")
            speak("I am here to do cool things for you!.Anyways, I am you A.I assistant")

        # elif "Translate" in query:
        #     # init the Google API translator
        #     speak("What language do you want me to translate")
        #     dest = 
        #     translator = Translator()
        #     translations = translator.translate


        # elif 'countdown'or 'set a timer' in query:
        #     # input time in seconds 
        #     speak("Enter the time in seconds")
        #     t = input("Enter the time in seconds: ") 
        #     # function call 
        #     countdown(int(t)) 

        elif 'when' in query:
            speak("Working on it sir!  ")
            print("Searching Google...")
            speak('Searching Google...')
            query = query.replace("google", "")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
                print("This is what I found according to your search")
                speak("This is what I found according to your search")

        elif 'where' in query:
            speak("Working on it sir!")
            print("Searching Google...")
            speak('Searching Google...')
            query = query.replace("google", "")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
                print("This is what I found according to your search")
                speak("This is what I found according to your search")
        elif "what's your name" in query or "What is your name" in query: 
            speak("Did I forget to introduce myself") 
            speak("Hi") 
            speak("My name is Jarvis", ) 
            print("My name is", name)
        elif 'why' in query:
            speak("Working on it sir!")
            print("Searching Google...")
            speak('Searching Google...')
            query = query.replace("google", "")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
                print("This is what I found according to your search")
                speak("This is what I found according to your search")
        elif "What" in query:
            speak("Working on it sir!")
            print("Searching Google...")
            speak('Searching Google...')
            query = query.replace("google", "")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
                print("This is what I found according to your search")
                speak("This is what I found according to your search")
        elif 'how' in query:
            speak("Working on it sir!  ")
            print("Searching Google...")
            speak('Searching Google...')
            query = query.replace("google", "")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
                print("This is what I found according to your search")
                speak("This is what I found according to your search")


        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop jarvis from listening to commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 
  
        elif 'open youtube' in query:
            speak("Working on it sir!")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Working on it sir!")
            webbrowser.open("google.com")

        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("You asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
            print("This is what I found according to your search")
            speak("This is what I found according to your search")
        
        elif "snap" in query or "take a photo" in query: 
            ec.capture(0, "Jarvis Camera ", "img.jpg") 

        elif "weather" in query: 
            # Google Open weather website 
            # to get API of Open weather  
            api_key = "Api key" 
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ") 
            print("City name : ") 
            city_name = takeCommand() 
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name 
            response = requests.get(complete_url)  
            x = response.json()  
            if x["cod"] != "404":  
                y = x["main"]  
                current_temperature = y["temp"]  
                current_pressure = y["pressure"]  
                current_humidiy = y["humidity"]  
                z = x["weather"]  
                weather_description = z[0]["description"]  
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
            else:  
                speak(" City Not Found ") 


        elif 'play music' in query:
            speak('Online or local?')
            pref = takeCommand().lower()
            if 'online' in pref:
                speak("Working on it sir!")
                print('Working on it sir!')
                speak('What artiste or genre')
                artiste = query
                webbrowser.open("https://www.boomplay.com" + artiste + "")
            else:
                # song_dir = 'D:\\Music'
                song_dir = "C:\\Users\\Adeyinka\\Music"
                songs = os.listdir(song_dir)
                print(songs)
                random = os.startfile(os.path.join(song_dir,songs[0]))


        elif "offline" in query:
            speak("Going offline sir!! It is my pleasure to be your assistant!")
            print("Going offline sir!! It is my pleasure to be your assistant!")
            speak("Goodbye Ezra!!")
            print("Goodbye Ezra!")
            quit()


        elif "goodbye jarvis" in query:
            speak("Going offline sir!! It is my pleasure to be your assistant!")
            print("Going offline sir!! It is my pleasure to be your assistant!")
            speak("Goodbye Ezra!!")
            print("Goodbye Ezra!")
            quit()

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M: %p")
            speak(f"the time is {strTime}")

        elif 'date' in query:
            strTime = datetime.datetime.now().strftime("%Y/%m/%d")
            speak(f"the date is {strTime}")

        elif 'email Ezekiel' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ""
                sendEmail(to, content)
                speak("Email sent.")
            except Exception as e:
                print(e)
                speak("Sorry Ezra. I was not able to send this email")

        elif 'change voice' in query:
            voices = engine.getProperty('voices')       #getting details of current voice
            #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
            engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

        elif 'calculate' in query:
            app_id = "Wolframalpha api id" 
            client = wolframalpha.client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res  = clent.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is" + answer)
            speak("The answer is " + answer)

        elif 'are you doing' in query: 
            random_word_list = ['Great','fantastic','admirable', "awesome" ,"bitchin", "boffo" ,'brill' ,'chillin',
            'blissful' ,'crucial', 'dope', 'excellent', 'fantastic','fine','first-rate', 'good', 'hunky-dory' ,
            "jim-dandy","marvellous",'ecstatic','joyful','optimistic','satisfied','pleasant','lovestruck', "superb",
             "terrific","the dog's bollocks" ,'topping','tremendous','wonderful'] 
            random_word = random.choice(random_word_list) 

            speak("I am feeling {}, Thank you").format(random_word)
            speak("How are you, Sir") 
            positive_emotions = ['Great','fantastic','admirable', "awesome" ,"bitchin", "boffo" ,'brill' ,'chillin',
            'blissful' ,'crucial', 'dope', 'excellent', 'fantastic','fine','first-rate', 'good', 'hunky-dory' ,
            "jim-dandy","marvellous",'ecstatic','joyful','optimistic','satisfied','pleasant','lovestruck', "superb",
            "terrific","the dog's bollocks" ,'topping','tremendous','wonderful','clever','concentrated','confident',
            'blissful','brave','careful','cautious','ecstatic','excited','fair','fantastic','friendly','glad','good','great',
            'interested','joyful','mediative','nice','optimistic','pleasant','quiet','satisfied','sensible','serious','surprised',
            'to be pleased','to be proud of','wonderful','curious','honest','innocent','in love','lovestruck','happy','fantabulous']


            negative_emotions = ['aggressive','agonized','angry','annoyed','arrogant','awful','bad','bored','confused','crazy','disappointed',
            'disbelieving','disgusted','enraged','exhausted','frightened','frustrated','grieving','guilty','hangover','helpless','horrified',
            'hurt','hysterical','idiotic','indifferent','lonely','lovesick','mad','mischievous','miserable','nasty','nervous','puzzled',
            'sad','sheepish','shocked','silly','smug','sorry','strange','stupid','suspicious','terrible','jealous of','upset',]

            feelings =takeCommand().lower()
            if feelings in positive_emotions:
                print("Glad to hear that. Let me know if ther is anything I can do for you")
                speak("Glad to hear that. Let me know if ther is anything I can do for you")
            elif feelings in negative_emotions:
                speak("I'm sorry to hear that. Mind if i could help?")



 

        elif "battery" in query:
            battery = psutil.sensors_battery()
            percent = str(battery.percent)
            print('''Your device has been running on ''' + percent +" % " +"battery")
            speak('I still have {} percent of battery left!'.format(percent))
        # elif 'use keyboard'in query:
              
        elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
                  
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled") 
  
        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop jarvis from listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 
           # most asked question from google Assistant 
        elif "will you be my gf" in query or "will you be my bf" in query:    
            speak("I'm not sure about, may be you should give me some time") 
  
        elif "how are you" in query: 
            speak("I'm fine, glad you me that") 
  
        elif "i love you" in query: 
            speak("It's hard to understand") 
  
        elif "what is" in query or "who is" in query: 
              
            # Use the same API key  
            # that we have generated earlier 
            client = wolframalpha.Client("API_ID") 
            res = client.query(query) 
              
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results") 
