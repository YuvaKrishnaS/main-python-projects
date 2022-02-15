import pyttsx3
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Pass(pass_inp):

    password = "python"

    passss = str(password)

    if passss==str(pass_inp):
        speak("Access granted .")
        print(": Access granted...")
        os.startfile("E:\\Krishnaaaaa\\MyJarvis\\myjav.py")

    else:
        speak("Access not granted .")
        print(": Access not granted...")

if __name__ == "__main__":
        print(": Jarvis is password protected, kindly type the password to access .")
        speak("Jarvis is password protected, kindly type the password to access .")
        passssss = input(": Enter your Password here =>  ")

        Pass(passssss)