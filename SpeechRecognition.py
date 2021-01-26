import speech_recognition as sr
import extraction as key
import sys
import pyttsx3


r = sr.Recognizer()

# need to find a way that can recognize speech faster 

def startListening():
    while(1):
        with sr.Microphone() as source:
            print('Speak anything : ')
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                print('You said : {}'.format(text))
                key.extractInfo(text)
            except:
                print('Sorry couldn\'t recognize your voice', sys.exc_info()[0])


# the second part of the implementation in this file would be text to speech so as to give responses

def main():
    # call initial greeting.
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Hello Dr.Wollowski! My name is Ahaana. I am a little nervous because this is my first demo and I can only update the mental model so far. wish me luck! Thank you!")
    engine.runAndWait()
    startListening()

main()
