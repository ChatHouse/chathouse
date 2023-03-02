#1️⃣ La primera solicitud es llamar a la libería que instalamos desde la terminal.❗Intrucciones de instalación de recursos: https://telegra.ph/Instalando-Recursos-03-02
import openai


#2️⃣ Realizando la llamada a la API de GPT3: ❗ Intrucciones para acceder a nuestra clave secreta de la API: https://telegra.ph/Solicitud-de-API---OpenAI-03-02

#❗NOTA. PEGAR entre las comillas la clave secreta generada. ▶ Ejemplo: openai.api_key = "SK - ..."
openai.api_key= ""

#3️⃣ Creando nuestro codigo para llamar a la API y generar la cadena conversacional
while True:

    #✅ Toma libertad de cambiar el saludo y sustituye la frase "Hola, ¿En qué puedo ayudarte?"
    prompt = input("\nHola, ¿En qué puedo ayudarte?: ").capitalize() 

    #⭕ Aquí va nuestro comando para finalizar la conversación y solicitudes a la API.
    if prompt== "Finalizar": 
        break
    
    #❗ En este bloque realizaremos los ajustes de salida y tipo de modelo conversacional que usaremos.
    conversation= openai.Completion.create(engine= "text-davinci-003", 
                            prompt= prompt,
                            n=1,
                            max_tokens= 3000)

    #❗ Aquí realizamos la configuración de salida para las respuestas que generará nuestro
    print("\nChatHouse: ", conversation.choices[0].text, "\n")

#NOTAS ESPECIALES:
#✅ Aprende más de las modificaciones, configuraciones y escalabilidad de la API aquí: https://platform.openai.com/docs/api-reference
#✅ Accede a más funciones de las API para Python aquí: https://github.com/openai/openai-python

"""📄GLOSARIO PARA AJUSTES PERSONALIZADOS:

    engine: Hace referencia al modelo con el que realizaremos las solicitudes y recibiremos las salidas de respuesta 🟡text-davinci-003 es el modelo más actual liberado para usuarios en la modalidad de licencia personal.

    prompt: 🟡Es recomendable dejar la variable sin aisgnar algún valor, esto para permitir entrada de preguntas libres.

    n: Hace referencia al número de respuesta que recibiremos a traves de la función de activación - ❗POR DEFECTO ES 1 - ✔ Podrías eliminarlo de las instrucciones, pues es un valor por defecto. Sin embargo, lo dejé colocado para la referencia y conocimiento de la existencia por parte del usuario

    max_tokens: Longitud maxima de la respuesta de salida, el modelo Davinci tiene un limite de salida de 4096, tomate la libertad de ajustarlo."""
