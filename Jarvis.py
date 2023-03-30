

import speech_recognition as sr
import pyttsx3
import openai


             


def call_jarvis():
    start = "hi sir how can i help you"
    engine = pyttsx3.init()
    engine.say(start)
    engine.runAndWait()
    r = sr.Recognizer()
    text = ""
# Use the default microphone as the audio source
    with sr.Microphone() as source:
    # Adjust for ambient noise
        print("say now")
        r.adjust_for_ambient_noise(source)
    # Listen for audio input
        audio = r.listen(source)
        try:
            text += r.recognize_google(audio)
            openai.api_key = ""
            # use your own openAI api key to run
            response = openai.Completion.create(
              model="text-davinci-003",
              prompt=text,
              temperature=0,
              max_tokens=4000,
              top_p=1,
              frequency_penalty=0.0,
              presence_penalty=0.0,
            )

            generated_text = response.choices[0].text.strip()
            engine = pyttsx3.init()
            engine.say(generated_text)
            engine.runAndWait()
            ask()
        except sr.UnknownValueError:
            text = "can't understand it sir can you say it again"
            engine = pyttsx3.init()  
# convert this text to speech  
            engine.setProperty("rate", 200)  
            engine.say(text)  
# play the speech  
            engine.runAndWait()
            ask()

      
    

def ask():
    text_get = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now")
        audio = r.listen(source)


    try:
        text_get += r.recognize_google(audio)
        if text_get.lower() == "jarvis":
            call_jarvis()
    except sr.UnknownValueError:
        ask()
    
ask()  