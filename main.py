import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
e = pyttsx3.init()
voices = e.getProperty('voices')
e.setProperty('voice', voices[1].id) #Establezco la voz femenina

def talk(text):
    e.say(text)
    e.runAndWait()

def take_command():
    try:
        with sr.Microphone(device_index=0) as source:
            listener.adjust_for_ambient_noise(source)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="es-ES")

            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                #talk(command)
                
    except Exception as e:
        print(e)
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '') 
        print('playing')
        pywhatkit.playonyt(song)

run_alexa()