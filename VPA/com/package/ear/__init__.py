import speech_recognition as sr
import webbrowser
import pyttsx
from time import sleep

engine = pyttsx.init()
engine.setProperty('rate', 70)
r = sr.Recognizer()

def recognize(audio):
    try:
        return r.recognize(audio)
    except LookupError :
        print("Could not understand audio")
        return "Could not understand audio"
   
    return ''
with sr.Microphone() as source:
    while True:
        engine.say("Hi How can i help you ?")
        sleep(0.15)
        print ("Start Speaking")
        audio = r.listen(source)
        words = recognize(audio)
        print("You said " + words)
        if words == "Facebook":
            engine.say("Shall i open the Facebook page for you ?")
            engine.runAndWait()
            audio = r.listen(source)
            words = recognize(audio)
            if words == "Yes":
                webbrowser.open('https://www.facebook.com')
        elif words == "stop":
            break