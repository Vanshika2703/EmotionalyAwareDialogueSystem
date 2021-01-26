import speech_recognition as sr
import nltk

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
                print(nltk.pos_tag(nltk.word_tokenize(text)))
            except:
                print('Sorry couldn\'t recognize your voice')

# the second part of the implementation in this file would be text to speech so as to give responses

def main():
    # call initial greeting.
    startListening()

main()
