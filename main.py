import pyautogui
import time
import pyperclip
import pyttsx3
import speech_recognition as sr

msg=[]
# Cria um objeto de sintetização de voz
engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()


# Define a voz a ser usada
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Define a taxa de fala
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)

engine.setProperty('volume', 2.0)

# Função que reproduz a voz
def speak(text):
    engine.say(text)
    engine.runAndWait()

def new():
    # Move o mouse para as coordenadas (x=100, y=100) e clica nele
    pyautogui.moveTo(600, 750) # abrir chrome
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(80, 20) #guia gpt
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(100, 150) #new chat
    #pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(600, 750) # fecha o chrome
    pyautogui.click()  
    time.sleep(1)
    pyautogui.moveTo(600, 600) # clica no prompt para digitar
    pyautogui.click()  

#new()

def novaba():
    pyautogui.moveTo(600, 750) # abrir chrome
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(1)

def copy():
    #pega somente a msg da vez
    
    pyautogui.moveTo(1320, 600) #desce o texto
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1150, 500) #selecionar texto baixo
    time.sleep(1)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.moveTo(100, 50) #selecionar texto alto/new
    time.sleep(1)
    pyautogui.moveTo(300, 110) #selecionar so msg exclui barra lateral 
    time.sleep(1)
    pyautogui.mouseUp(button='left')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    
    msg.append(pyperclip.paste())

def chat(texto):
    pyautogui.moveTo(600, 750) # abrir chrome
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(80, 20) #guia gpt
    pyautogui.click()
    time.sleep(2)   

    pyautogui.moveTo(600, 650) #texto chat
    pyautogui.click()
    time.sleep(2)
    # Escreve "Hello World!" na tela
    pyautogui.typewrite(texto, interval=0.1)
    pyautogui.moveTo(1170, 650) #enviar chat
    pyautogui.click()
    time.sleep(6)

def yt(text):
    novaba()
    string = retira_cmd(text)
    
    pyautogui.typewrite('youtube.com', interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)
    guia_j1()
    pyautogui.moveTo(400, 140) #clica search
    pyautogui.click()
    pyautogui.typewrite(string, interval=0.1)
    time.sleep(3)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.moveTo(350, 500) #clica video
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(760, 500) #clica anuncio manual
    time.sleep(10)
    
    time.sleep(3)

def stop():
    pyautogui.moveTo(600, 750) # abrir chrome
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(300, 20) #guia 2
    pyautogui.click()
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2)

def cotacao(text):
    novaba()

    pyautogui.typewrite(text, interval=0.1)
    pyautogui.hotkey('del')
    pyautogui.press("enter") #clica search
    time.sleep(2)
    pyautogui.moveTo(250, 220) #clica shop
    pyautogui.click()
    time.sleep(2)
    
    guia_j1()
    time.sleep(10)

def guia_j1():
    #adiciona a nova guia para janela 1
    pyautogui.moveTo(80, 15) #guia yt
    pyautogui.mouseDown(button='left')
    time.sleep(2)
    pyautogui.moveTo(300, 15) #guia yt
    time.sleep(2)
    pyautogui.moveTo(200, 20) #guia 2
    time.sleep(2)
    pyautogui.mouseUp(button='left')
    time.sleep(1)

def retira_cmd(textt):
    t = tuple(textt.split(" "))
    t = t[1:]
    string = ''
    time.sleep(2)
    for word in t:
        string = string+' '+word
    return string

def aimg(text):
    novaba()

    pyautogui.typewrite('bing.com/images/create', interval=0.1)
    pyautogui.press("enter")
    time.sleep(20)
    string= retira_cmd(text)
    time.sleep(3)
    guia_j1()
    pyautogui.moveTo(250, 220) #clica search
    pyautogui.click()
    pyautogui.typewrite(string, interval=0.1)
    time.sleep(3)
    pyautogui.press("enter")
    time.sleep(3)
    
    time.sleep(30)

def foto(text):
    novaba()

    texto=retira_cmd(text)
    pyautogui.typewrite(texto, interval=0.1)
    pyautogui.hotkey('del')
    pyautogui.press("enter") #clica search
    time.sleep(2)
    pyautogui.moveTo(250, 220) #clica img
    pyautogui.click()
    time.sleep(2)
    
    guia_j1()
    time.sleep(10)

def chatgrande(texto):
    #le a segunda parte do codigo se a primeira leitura nao for suficiente
    if  msg[-2] in msg[-1]:
        texto = msg[-1]
        texto_restante = texto.split(msg[-2])[1].strip()
        # Substituir valor de msg[-1] pelo novo texto processado
        msg[-1] = texto_restante
        print(f"resposta: {msg[-1]}")
        # Reproduz a fala
        speak(msg[-1])

while True:
    try:
        # Recebe a entrada do usuário
        with sr.Microphone() as source:
            print("Diga alguma coisa!")
            audio = r.listen(source, timeout=5)
            text=''

        # Transcreve o áudio para texto
        try:
            text = r.recognize_google(audio, language='pt-BR')
            
            print(text)
        except sr.UnknownValueError:
            print("Não foi possível reconhecer a fala")

        if text != '':
            if 'toque' in text or 'Toque' in text:
                yt(text)
            elif 'stop' in text or 'Stop' in text :
                stop()
            elif 'Qual o valor' in text or 'qual o valor' in text:
                cotacao(text)
            elif 'crie imagem de' in text or 'Crie imagem de' in text:
                x=retira_cmd(text)
                aimg(x)     
            elif 'foto' in text or 'Foto' in text:
                foto(text)  
            elif 'news' in text or 'News' in text:
                cotacao(text)  
            elif 'chat' in text or 'Chat' in text: 
                chat(text)
                copy()
                # Remover texto até "ChatGPT"
                if 'ChatGPT' in msg[-1]: 
                    texto = msg[-1]
                    texto_restante = texto.split("ChatGPT")[1].strip()
                    # Substituir valor de msg[-1] pelo novo texto processado
                    msg[-1] = texto_restante
                print(f"resposta: {msg[-1]}")
                # Reproduz a fala
                speak(msg[-1])
                #copy()
                #chatgrande(texto)

            pyautogui.moveTo(600, 750) # fecha o chrome
            pyautogui.click() 

    except KeyboardInterrupt:
        print("\nPrograma encerrado.")
        break







