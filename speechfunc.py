import speech_recognition as sr
import sys # to exit the program
import random # for the number guessing game
import time # for background listening

def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        text = recognizer.recognize_google(audio)
        print("Google Speech Recognition thinks you said: {}\n". format(text))
    except:
        print("Google Speech Recognition could not understand audio\n")

# doesn't quite work as good as I want it to work.
def listen_in_the_background(recognizer):
    m = sr.Microphone()
    with m as source:
        recognizer.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listenin
    print("OK, I'm listening now")

    #audio is the stuff that's recorded
    stop_listening = recognizer.listen_in_background(m, callback)

    #listen as long as you want, press enter to stop recording.
    choice = "is just an illusion"
    while choice != "": #Funky logic, rework?
        choice = input("Press enter to stop recording:")
        if choice == "":
            stop_listening(wait_for_stop=False)

#capture the audio mate
def say_stuff(recognizer, lang):
    with sr.Microphone() as source:
        print('OK, I\'m listening now')

        #audio is the stuff that's recorded
        audio = recognizer.listen(source)

        # Debugging: print(lang)
        try:
            text = recognizer.recognize_google(audio, language=lang)
            print("You said: '{}'\n". format(text))
        except:
            print('I didn\'t catch that.\n')
        
def game(recognizer):
    with sr.Microphone() as source:
        print("Let's play a game!")
        print("I'm thinking of a number between 0 and 10!")

        random_number = random.randrange(10) # get a number from 0 to 10.
        
        while True:
            print("GUESS WHICH!")
            audio = recognizer.listen(source)
            try:
                text = int(recognizer.recognize_google(audio, language="en-US"))
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
    name = name.lower() # In case people add some upper-case chars
    if name in languages:
        lang = languages[name]
        print('Got it, you want: ' + lang + " tag for " + name + "\n")
        return lang
    else:
        print('This language is not currently supported')
