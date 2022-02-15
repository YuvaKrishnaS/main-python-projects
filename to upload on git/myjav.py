import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
from keyboard import press
import os
import requests
import smtplib
import bs4
from keyboard import press_and_release



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")

    elif hour >= 12 and hour < 14:
        speak("Good Afternoon sir!")

    elif hour >= 14 and hour <= 18:
        speak("Good Evening sir!")

    else:
        speak("Hi sir!")

    strTime = datetime.datetime.now().strftime("%H:%M")
    speak(f"the time is {strTime}")
    speak("I am Jarvis! Please tell me how may I help you")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('naveenprasad134847@gmail.com', 'Naveen@47')
    server.sendmail('snavinekma@gmail.com', to, content)
    server.close()

def CoronaVirus(Country):

    countries = str(Country).replace(" "," ")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)

    soups = bs4.BeautifulSoup(result.text,'lxml')

    corona = soups.find_all('div',class_ = 'maincounter-number')

    Data = []

    for case in corona:

        span = case.find('span')

        Data.append(span.string)

    cases , Death , recovered = Data
    speak(f"Cases : {cases}")
    speak(f"Death : {Death}")
    speak(f"recovered : {recovered}")


    return cases , Death , recovered

if __name__ == "__main__":
    wishMe()

    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'pause' in query:

            press('space bar')

        elif 'resume' in query:

            press('space bar')

        elif 'full screen' in query:

            press('f')

        elif 'film screen' in query:

            press('t')

        elif 'skip' in query:

            press('l')

        elif 'back' in query:

            press('j')

        elif 'increase' in query:

            press_and_release('SHIFT + .')

        elif 'decrease' in query:

            press_and_release('SHIFT + ,')

        elif 'previous' in query:

            press_and_release('SHIFT + p')

        elif 'next' in query:

            press_and_release('SHIFT + n')
    
        elif 'mute' in query:

            press('m')

        elif 'unmute' in query:

            press('m')

        elif 'my channel' in query:

            webbrowser.open("https://www.youtube.com/channel/UClCR78mI9CMLsnDcJzUVGVg")

        elif 'home screen' in query:

            press_and_release('windows + m')

        elif 'show start' in query:

            press('windows')
            speak("as you wish sir")

        elif 'open setting' in query:

            press_and_release('windows + i')
            speak("opening settings sir")

        elif 'open search' in query:

            press_and_release('windows + s')
            speak("opening search bar sir")

        elif 'screenshot' in query:

            press_and_release('windows + SHIFT + s')
            speak("you can now snip you desktop sir")

        elif 'restore windows' in  query:

            press_and_release('Windows + Shift + M')
            speak("restoring windows sir")

        if 'new tab' in query:

            press_and_release('ctrl + t')
            speak("opening new tab")

        elif 'close tab' in query:

            press_and_release('ctrl + w')
            speak("closing tab sir")

        elif 'new window' in query:

            press_and_release('ctrl + n')
            speak("opening new window sir")

        elif 'history' in query:

            press_and_release('ctrl + h')
            speak("opening your history sir")

        elif 'download' in query:

            press_and_release('ctrl + j')
            speak("downloading sir")

        elif 'bookmark' in query:

            press_and_release('ctrl + d')
            speak("booking mark this page sir")

            press('enter')

        elif 'incognito' in query:

            press_and_release('Ctrl + Shift + n')
            speak("opening new icognito tab sir")

        elif 'switch tab' in query:

            tab = query.replace("switch tab ", "")
            Tab = tab.replace("to","")
        
            num = Tab

            bb = f'ctrl + {num}'

            press_and_release(bb)
            speak("switching the tab sir")

        elif 'search on wikipedia for' in query:
            speak('Searching Wikipedia...')
            print("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'where do you live' in query:
            speak("i am in your computer , in your heart")
            print()

        elif 'switch to desktop 1' in query:
            press_and_release('Windows + ctrl + key_left')
            speak("switching window")

        elif 'hello' in query:
            speak("hello sir")
            print()

        elif 'who is my father' in query:
            speak("you farther's name is mr. naveen prasad. he is retired from navy and currently serving in Bank of India")
            print()

        elif 'why were you asleep' in query:
            speak("I'm very very sorry sir! but as i think you said me to sleep.")
            print()

        elif 'stop talking back' in query:
            speak("sorry sir")
            print()

        elif 'are you there' in query:
            speak('yes sir')
            print()

        elif 'i wanted to say' in query:
            speak("You can tell it to me freely sir!")
            print()

        elif 'i love you' in query:
            speak("yes! i also wanted to say this to you from many years!")
            print()

        elif 'i am fine' in query:
            speak("that's great!")
            print()

        elif 'how are you' in query:
            speak("i am fine sir , how are you")
            print()

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak('opening youtube')

        elif 'open google' in query:
            webbrowser.open("www.google.com")
            speak('opening google')

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")
            speak('opening stackoverflow')

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2021.3.2"
            speak("opening code!")
            os.startfile(codePath)

        elif 'join my evs' in query:
            webbrowser.open("https://meet.google.com/oba-uxvv-jzz")
            speak("opening your evs class")

        elif 'join my maths' in query:
            webbrowser.open("https://meet.google.com/sfh-cwpd-xvr")
            speak("joining you maths class")

        elif 'email to my father' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "snavinekma@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend krishna bhai. I am not able to send this email")

        elif 'corona' in query:

            speak("Which Country's information you want sir")
            content = takeCommand()

            CoronaVirus(content)
