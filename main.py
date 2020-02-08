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
            text = r.recognize_google(audio)
            print('You said {}'. format(text))
        except:
            print('You didn\'t say anthing as far as I know')


# makes an infinite loop so that you can say stuff as many times as you want.
# type in 0 to stop the program or 1 to see how program recognizes what you're saying.
choice = ""
while choice != '0':
    print("Type in 1 for the program to transcribe stuff")
    print("0 to exit the program")
    choice = input()

    if choice == '1':
        say_stuff()
    elif choice == '0':
        print('Buh-bye!')
        sys.exit()
    else:
        print('What you chose is different to what I want.')