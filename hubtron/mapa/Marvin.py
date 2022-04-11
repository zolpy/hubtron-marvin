# import pyaudio as pa
import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import pywhatkit
import streamlit as st

recognizer = sr.Recognizer()
audio = sr.Recognizer()
maquina = pyttsx3.init()

st.set_page_config(
     page_title="Marvin",
     page_icon="https://cdn0.iconfinder.com/data/icons/monster-14/64/cyborg_halloween_machine_robot_teen_-256.png",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

# Header
st.image('https://res.cloudinary.com/dmbamuk26/image/upload/v1649696840/hubtron/hubtron_marvin.gif')
maquina.say(
    'Olá, seu sou o primeiro Hubtron, meu nome é Marvin. Meus sintetizadores de voz não estão ajudando muito, sinto muito por isso. Em que eu posso lhe ser útil?')
st.write(
    'Olá, seu sou o primeiro Hubtron, meu nome é Marvin. Meus sintetizadores de voz não estão ajudando muito, sinto muito por isso. Em que eu posso lhe ser útil?')
maquina.runAndWait()

st.markdown("### Os comandos são simples")

st.markdown("Apenas use: ")
st.write("Marvin + relógio : para saber as horas.")
st.write("Marvin + procurar + COISA QUE SE QUEIRA: para saber sobre alguma coisa.")
st.write("Marvin + toque + NOME DA MÚSICA QUE SE QUEIRA: para abrir algum video do YouTube")

def chamaMarvin():
    with sr.Microphone() as source:  # microphone as source
        audio = recognizer.listen(source, None, 3)  # listen for the audio via source
        voice_data = ''

        try:
            voice_data = recognizer.recognize_google(audio, language="pt-BR").lower()  # en-US
        except sr.UnknownValueError:  # error: recognizer does not understand
            print()
        except sr.RequestError:
            print('Serviço offline')  # error: recognizer is not connected

        print(">>", voice_data)  # print what user saidprint
        # for bot_name_variation in BOT_NAMES:
        if (('marvin') in voice_data):
            print(">>>", voice_data)  # print what use
            st.write(">>>", voice_data)  # print what user saidprint
            if ('relógio' in voice_data):
                # if 'hora' in voice_data:
                # voice_data = voice_data.replace('marvin', '')
                print(">>>>", voice_data)  # print what user saidprint
                st.write(">>>>", voice_data)  # print what user saidprint
                hora = datetime.datetime.now().strftime('%H:%M')
                maquina.say('Agora são' + hora)
                st.write(">>>> Agora são " + hora)
                maquina.runAndWait()
            elif 'procurar' in voice_data:
                procurar = voice_data.replace('procurar', '')
                wikipedia.set_lang("pt")
                print(">>>>", voice_data)  # print what user saidprint
                resultado = wikipedia.summary(procurar, 2)
                print(resultado)
                st.write(resultado)
                maquina.say(resultado)
                maquina.runAndWait()

            elif 'toque' in voice_data:
                musica = voice_data.replace('toque', '')
                resultado = pywhatkit.playonyt(musica)
                maquina.say(resultado)
                maquina.runAndWait()


while True:
    chamaMarvin()
