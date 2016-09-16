import speech_recognition
import pyttsx
import time
from time import ctime
import wikipedia
import urllib3
import logging
from logging.config import thread

speech_engine = pyttsx.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)

def speak(text):
    speech_engine.say(text)
    speech_engine.runAndWait()

recognizer = speech_recognition.Recognizer()

def listen():
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(recognizer.energy_threshold))
       
        audio = recognizer.listen(source)
        print(audio)
    try:
        return recognizer.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
        return "Could not understand audio"
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))
        return "Could not understand audio"
    return ""


def jarvis(data):
    if "wake up" in data:
        speak("yes")
    if "how are you" in data:
        speak("I am fine")
    if "what time is it" in data:
        speak(ctime()) 

def logic():
    speak("Hi Divya, what can I do for you?")
    #listen again if sound is not clear#
    loop=True
    while loop:
        data=listen()
        if "Could not understand audio" in data:
            speak("please speak again")
            continue
        else:
            loop=False
    
    print (data)
    if "news" in data:
        print("call java to parse site https://news.google.co.in/")
    elif "weather" in data:
        print("call java to parse site https://weather.co.in/")
    else:
        print (wikipedia.search(data, results=3, suggestion=False))
        speak("which one")
        data=listen()
        speak(wikipedia.summary(data, sentences=2, chars=0, auto_suggest=True, redirect=True))
    
    speak("You want to know anything else")
    data=listen()
    if "no" in data:
        speak("bye bye")
    else:
        logic()
    return "done";

time.sleep(2)
count=1
while 1:
    print(thread.__name__)
    print(count)
    data = listen()
    if "Jarvis" in data:
        result = logic();
        
        

    
    


