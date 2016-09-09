import speech_recognition
import pyttsx
import time
from time import ctime
import wikipedia
import urllib3

speech_engine = pyttsx.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)

def speak(text):
    speech_engine.say(text)
    speech_engine.runAndWait()

recognizer = speech_recognition.Recognizer()

def listen():
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        return recognizer.recognize_google(audio)
        # or: return recognizer.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))

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
print (wikipedia.search("Gopichand", results=10, suggestion=False))
speak(wikipedia.search("Gopichand", results=10, suggestion=False))
data=listen()
speech_recognition.Recognizer
speak (wikipedia.summary(data, sentences=2))

#print (wikipedia.summary("Gopichand", sentences=3))
#===============================================================================
#   
# opener = urllib3.make_headers
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# infile = opener.open('http://en.wikipedia.org/w/index.php?title=Albert_Einstein&printable=yes')
# page = infile.read()
# print(page)
#===============================================================================
#===============================================================================
# while 1:
#     speak("my job")
#     data = listen()
#     speak("ok")
#     jarvis(data)
#===============================================================================