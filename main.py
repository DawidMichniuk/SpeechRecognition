import speech_recognition as sr
import sys # to exit the program
import random # for the number guessing game
import time # for background listening

# this tries to recognise what's being said, where as "source" is what's captured by microphone
r = sr.Recognizer()

#set the default value for language to american english
lang = "en_US"

def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        text = recognizer.recognize_google(audio)
        print("Google Speech Recognition thinks you said: {}\n". format(text))
    except:
        print("Google Speech Recognition could not understand audio\n")

# doesn't quite work as good as I want it to work.
def listen_in_the_background():
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listenin
    print("OK, I'm listening now")

    #audio is the stuff that's recorded
    stop_listening = r.listen_in_background(m, callback)

    #listen as long as you want, press enter to stop recording.
    choice = "is just an illusion"
    while choice != "":
        choice = input("Press enter to stop recording:")
        if choice == "":
            stop_listening(wait_for_stop=False)

#capture the audio mate
def say_stuff():
    with sr.Microphone() as source:
        print('OK, I\'m listening now')

        #audio is the stuff that's recorded
        audio = r.listen(source)

        # Debugging: print(lang)
        try:
            text = r.recognize_google(audio, language=lang)
            print("You said: '{}'\n". format(text))
        except:
            print('I didn\'t catch that.\n')
        
def game():
    with sr.Microphone() as source:
        print("Let's play a game!")
        print("I'm thinking of a number between 0 and 10!")

        random_number = random.randrange(10) # get a number from 0 to 10.
        
        while True:
            print("GUESS WHICH!")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="en-US")
                text = int(text)
                if random_number == text:
                    print("You won!\n")
                    print("The number I though of was: " + random_number)
                    print("And you said: " + text)
                    break # return somehow triggeres the except clause
                elif random_number > text:
                    print("Your number is smaller than what I'm thinking\n")
                elif random_number < text:
                    print('Your number is bigger than what I want!\n')
            except:
                print('I didn\'t catch that.\n')


def pick_language(name):
    global lang
    languages = {
        'english': 'en-US',
        'polish': 'pl-PL',
        'lithuanian': 'lt-LT',
        'norwegian': 'no-NO',
        'french': 'fr-FR',
        'russian': 'ru-RU',
        'italian': 'it-IT',
        'portugese': 'pt-PT',
        'arabic': 'ar-AE', #goes from left to right
        'urdu': 'ur-PK', #goes from left to right, TODO: FIX
        'turkish': 'tr-TR',
        'bulgarian': 'bg-BG',
        'czech': 'cs-CZ',
        'greek': 'el-GR'
    }
    if name in languages:
        lang = languages[name]
        print('Got it, you want: ' + lang + " tag for " + name + "\n")
    else:
        print('This language is not currently supported')


# makes an infinite loop so that you can say stuff as many times as you want.
# type in 0 to stop the program or 1 to see how program recognizes what you're saying.
choice = ""
while choice != '0':
    print("1. Speech Recognition")
    print("2. Pick your language")
    print("3. Play a guessing game")
    print("4. Listen in the background")
    print("0. Exit the program\n")
    choice = input('Option: ')

    if choice == '1':
        say_stuff()
    elif choice == '2':
        name = input('Type in your language: ')
        pick_language(name)
    elif choice == '3':
        game()
    elif choice == '4':
        listen_in_the_background()
    elif choice == '0':
        print('Buh-bye!')
    else:
        print('What you chose is different to what I want.')