import speech_recognition as sr
import sys # to exit the program

# this tries to recognise what's being said, where as "source" is what's captured by microphone
r = sr.Recognizer()

#capture the audio mate
def say_stuff():
    with sr.Microphone() as source:
        print('OK, I\'m listening now')

        #audio is the stuff that's recorded
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language=lang)
            print("You said: '{}'\n". format(text))
        except:
            print('I didn\'t catch that.\n')
        
def pick_language(name):
    global lang
    lang = "en-US"
    languages = []
    if name == "english":
        lang="en-US"
    elif name == "polish":
        lang="pl-PL"
    elif name == "lithuanian":
        lang="lt-LT"
    elif name == "norwegian":
        lang="no-NO"
    elif name == "french":
        lang="fr-Fr"
    elif name == "russian":
        lang="ru-RU"
    elif name == "italian":
        lang="it-IT"
    elif name == "portugese":
        lang="pt-PT"
    else:
        print('You donkey, that doesn\'t exists! ')

# makes an infinite loop so that you can say stuff as many times as you want.
# type in 0 to stop the program or 1 to see how program recognizes what you're saying.
choice = ""
while choice != '0':
    print("1. Speech Recognition")
    print("2. Pick your language")
    print("0. Exit the program\n")
    choice = input('Option: ')

    if choice == '1':
        say_stuff()
    elif choice == '2':
        name = input('Type in your language: ')
        pick_language(name)
    elif choice == '0':
        print('Buh-bye!')
    else:
        print('What you chose is different to what I want.')