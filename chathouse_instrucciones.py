#1️⃣ Instalación de librería Open AI: https://telegra.ph/Instalando-Recursos-03-02
import openai

#❗ Correponden al import del paso 5.
import pyttsx3 

#❗ Correponde al import del paso 6
import speech_recognition as sr 
import pyautogui as ptg 
from decouple import config 

#2️⃣ Realizando la llamada a la API de GPT3: ❗ Intrucciones para acceder a nuestra clave secreta de la API: https://telegra.ph/Solicitud-de-API---OpenAI-03-02

#⭕ Leer los puntos acerca de la privacidad de la Clave Secreta.

#❗NOTA. PEGAR entre las comillas la clave secreta generada. ▶ Ejemplo: openai.api_key = "SK-..."
openai.api_key = "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"

#3️⃣ Creando nuestro codigo para llamar a la API y generar la cadena conversacional

r= sr.Recognizer()

while True:

    #❗ Aquí se configura la entrada del audio que se convertirá en texto.
    with sr.Microphone() as source:

        audio= r.listen(source)

    try: 
        engine_model_gpt3 = "text-davinci-003"

        #❗ Aquí se configura el idioma de comprensión de la entrada de audio.
        text= str(r.recognize_google(audio, language= 'es-Es'))

         #✅ Toma libertad de cambiar el ID y sustituye la frase "Usuario"
        prompt = input("\nUsuario: ").capitalize()
        ptg.hotkey('enter')
        
        #⭕ Aquí va nuestro comando para finalizar la conversación y solicitudes a la API.
        if prompt in ['Exit', 'Salir', 'Quit', 'Finalizar', 'Terminar']:
            break
        
        #❗ En este bloque realizaremos los ajustes de salida y tipo de modelo conversacional que usaremos. ¿Te interesa saver que significa cada variable? Entra a este link: https://telegra.ph/Glosario-para-ajuste-de-modelo-conversacional-03-02    
        completion = openai.Completion.create(

            engine= engine_model_gpt3,
            prompt = prompt,
            max_tokens= 2048,
            n=1,
            stop= None,
            temperature= 0.3
        )

        #❗ Aquí realizamos la configuración de salida para las respuestas que generará nuestro.
        response = completion.choices[0].text

        print("\nChatHouse, dice: ", response)

        #Configuración de la salida de audio de nuestro asistente. Aquí puedes ingresar los parametros para aumentar la velocidad, suvizar la voz y cambiar el genero del audio.
        engine1= pyttsx3.init()
        engine1.say(response)
        engine1.runAndWait()

    except:
        print("Los siento, no reconocí tu voz")
        break

#4️⃣ Ejecuta desde la terminal o Shell para realizar las primeras pruebas de tu codigo y API, instrucciones aquí -> https://telegra.ph/Ejecuta-tu-primera-prueba-de-API-desde-Terminal-03-02

#5️⃣ 🗣🗣🗣🗣🗣🗣DANDO VOZ A NUESTRO CHAT CONVERSACIONAL. Recursos a instalar -> https://telegra.ph/Recursos-para-la-voz-de-nuestro-asistente-03-02

#6️⃣Es hora de que el programa convierta nuestra voz a texto. Recursos a instalar -> https://telegra.ph/Recursos-para-convertir-nuestra-voz-a-texto-03-03