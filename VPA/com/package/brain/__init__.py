import speech_recognition
import pyttsx
import time
from time import ctime
import wikipedia
import urllib3
import logging

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
        #=======================================================================
        # a = recognizer.record(source, duration=4, offset=False)
        #=======================================================================
        audio = recognizer.listen(source)
        #=======================================================================
        # print(a)
        #=======================================================================
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

#speak("Say something!")
#speak("I heard you say " + listen())
def jarvis(data):
    if "wake up" in data:
        speak("yes")
    if "how are you" in data:
        speak("I am fine")
    if "what time is it" in data:
        speak(ctime()) 


time.sleep(2)
speak("Hi Divya, what can I do for you?")
data=listen()
print (data)
if "Could not understand audio" in data:
    speak("please speak again")
    data=listen()
print (wikipedia.search(data, results=3, suggestion=False))
speak("which one")
data=listen()
speak(wikipedia.summary(data, sentences=2, chars=0, auto_suggest=True, redirect=True))

#===============================================================================
# while 1:
#     speak("my job")
#     data = listen()
#     speak("ok")
#     jarvis(data)
#===============================================================================