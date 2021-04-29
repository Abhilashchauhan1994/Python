import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import pyjokes

listener =sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
    
def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    try:
        print('checking Microphone..')
        with sr.Microphone() as source:
            print('I am listening....')
            voice =listener.listen(source)
            command = listener.recognize_google(voice)
            command =command.lower()
            if 'alexa' in command:
                command=command.replace('alexa', '')
                print(command)
    except:
        command='I am not getting your Voice'
        talk(command)
        pass
    return command

def run_alexa():
    command =take_command()
    print(command)
    if 'play' in command:
        command = command.replace('play','')
        talk('searching and Playing' +command)
        pywhatkit.playonyt(command)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(time)    
    elif 'tell me about' in command:
        about = command.replace('tell me about','')
        info =wikipedia.summary(about,1)
        talk(info)
        print(info)
    elif 'joke' in command:
        jokes = pyjokes.get_joke()
        talk(jokes)
        
run_alexa()        