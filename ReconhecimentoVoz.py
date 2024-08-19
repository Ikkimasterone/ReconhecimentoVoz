#Importando a biblioteca
import speech_recognition as sr
import os

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone =  sr.Recognizer()

    #Usando o microfone
    with sr.Microphone() as source:

        #Chama um algoritimo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)

        #Frase para o usuário dizer algo
        print("Diga alguma coisa: ")

        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
    try:

        #Passa a variável para o algoritmo reconhecedor de padrôes
        frase = microfone.recognize_google(audio,language='pt-BR')

        #Se houver a frase escrita no áudio que você falou, ele abre um progama

        if "navegador" in frase:
            os.system("start opera.exe")
        

        #Retorna a frase pronunciada
        print("Você disse: " + frase)

    #Se não reconheceu o padrão de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
    
    return frase

ouvir_microfone()