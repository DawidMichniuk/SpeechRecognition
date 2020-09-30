#!/usr/bin/python3
import speech_recognition as sr
import sys # to exit the program
import random # for the number guessing game
import time # for background listening
import speechfunc # for all the actual functions.

print("Hello!")

    # makes an infinite loop so that you can say stuff as many times as you want.
    # type in 0 to stop the program or 1 to see how program recognizes what you're saying.
def menu():
    # this tries to recognise what's being said, where as "source" is what's captured by microphone
    r = sr.Recognizer()

    #set the default value for language to american english
    lang = "en_US"

    choice = ""
    while choice != '0':
        print("1. Speech Recognition")
        print("2. Pick your language")
        print("3. Play a guessing game")
        print("4. Listen in the background")
        print("0. Exit the program\n")
        choice = input('Option: ')

        if choice == '1':
            speechfunc.say_stuff(r, lang)
        elif choice == '2':
            name = input('Type in your language: ')
            lang = speechfunc.pick_language(name)
        elif choice == '3':
            speechfunc.game(r)
        elif choice == '4':
            speechfunc.listen_in_the_background(r)
        elif choice == '0':
            print('Buh-bye!')
            sys.exit()
        else:
            print('What you chose is probably in-accessible')

# Makes it so the menu runs at startup!
if __name__ == "__main__":
    menu()