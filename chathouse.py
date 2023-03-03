
import openai
import pyttsx3 
import speech_recognition as sr 
import pyautogui as ptg 
from decouple import config 


openai.api_key = ""

r= sr.Recognizer()

while True:

   
    with sr.Microphone() as source:

        audio= r.listen(source)

    try: 
        engine_model_gpt3 = "text-davinci-003"
        
        text= str(r.recognize_google(audio, language= 'es-Es'))
         
        prompt = input("\nUsuario: ").capitalize()
        ptg.hotkey('enter')
        
        if prompt in ['Exit', 'Salir', 'Quit', 'Finalizar', 'Terminar']:
            break
          
        completion = openai.Completion.create(

            engine= engine_model_gpt3,
            prompt = prompt,
            max_tokens= 2048,
            n=1,
            stop= None,
            temperature= 0.3
        )
        
        response = completion.choices[0].text

        print("\nChatHouse, dice: ", response)

        engine1= pyttsx3.init()
        engine1.say(response)
        engine1.runAndWait()

    except:
        print("Los siento, no reconocí tu voz")
        break
