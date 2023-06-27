from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from translate import Translator
import tkinter as tk
import webbrowser as wb
import pyttsx3
import pyperclip



lista_idiomas = ['PT','EN','ES','FR']
def traduzir_textos():


    get_caixa_texto = caixa_texto.get('1.0',END)
    get_texto_idiomas= texto_idiomas.get()
    get_texto_idiomas_traducao = texto_idiomas_traducao.get()

    #Verificando se os ComboBox Foram preenchidos
    if get_texto_idiomas != '':
        tradutor = Translator(from_lang=get_texto_idiomas, to_lang=get_texto_idiomas_traducao)
        frase = tradutor.translate(get_caixa_texto)
        messagebox.showinfo('TRADUZINDO TEXTO', 'SEU TEXTO ESTÁ SENDO TRADUZIDO')
        caixa_texto_traducao.insert('insert', frase)



    else:
        tradutor = Translator(from_lang='PT', to_lang='EN')
        frase = tradutor.translate(get_caixa_texto)
        messagebox.showinfo('TRADUZINDO TEXTO', 'SEU TEXTO ESTÁ SENDO TRADUZIDO')
        caixa_texto_traducao.insert('insert', frase)

def limpar_caixaText():
    caixa_texto.delete('1.0', END)
    caixa_texto_traducao.delete('1.0',END)
def audio_texto():

    texto_audio = caixa_texto.get('1.0',END)
    robo = pyttsx3.init('sapi5')
    robo.say(texto_audio)
    robo.runAndWait()
    robo.stop()

def audio_traduzido():
    texto_audio = caixa_texto_traducao.get('1.0', END)
    robo = pyttsx3.init('sapi5')
    robo.say(texto_audio)
    robo.runAndWait()
    robo.stop()

def pesquisar_web():
    get_texto = caixa_texto.get('1.0', END)
    get_idiomaI = texto_idiomas.get().lower()
    get_idiomaII = texto_idiomas_traducao.get().lower()

    wb.open(f'https://translate.google.com.br/?hl=pt-BR&sl={get_idiomaI}&tl={get_idiomaII}&text={get_texto}&op=translate')

def copiar_texto():
    get_texto = caixa_texto.get('1.0',END)
    pyperclip.copy(get_texto)

def copiar_texto_traduzido():
    get_texto = caixa_texto_traducao.get('1.0', END)
    pyperclip.copy(get_texto)
def sair():
    caixa_texto.delete('1.0', END)
    caixa_texto_traducao.delete('1.0', END)
    res= messagebox.askquestion('Sair da Aplicação','Deseja Sair da Aplicação',)

    if res == "yes":
        app.destroy()
        exit()
    else:
        pass

app = tk.Tk()
app.title('APP TRADUTOR')
app.geometry('900x450')
app.iconbitmap(r'icones\icon.ico')
app.configure(bg="#252525")



#Colocando os Campos para digitalizar o Texto que deseja traduzir
texto = Label(app, text='Idioma do Texto: ',compound=LEFT, relief=FLAT, anchor='center' ,border=2,font=("Arial",10,'bold'))
texto.place(y=20 , x=10)

texto_idiomas = Combobox(app,width=40,values=lista_idiomas)
texto_idiomas.place(y=20, x = 150)

caixa_texto = Text(app,font=("Arial",10),border=3)
caixa_texto.place(y=50,x=10,height=205,width=400)

#Colocando os Campos de Tradução do Texto
texto_traducao = Label(app, text='Tradução do Texto: ',compound=LEFT, relief=FLAT, anchor='center' ,border=2,font=("Arial",10,'bold'))
texto_traducao.place(y=20 , x=450)


texto_idiomas_traducao = Combobox(app,width=40,values=lista_idiomas)
texto_idiomas_traducao.place(y=20, x = 610)

caixa_texto_traducao = Text(app,font=("Arial",10),border=3)
caixa_texto_traducao.place(y=50,x=450,height=205,width=420)



#Criando os Comandos / Botões

texto_botao_traducao = Label(text='TRADUZIR',font=("Arial",10,'bold'))
texto_botao_traducao.place(y=300 , x=94)

icone_traducao = PhotoImage(file='icones/Traduzir_IV.png')

botao_traducao = Button(command=traduzir_textos,highlightthickness=0,font=("Arial",10,'bold'),image=icone_traducao,border=3)
botao_traducao.place(y=350, x=100)

#Icone de Audio do lado da tela de Tradução do Texto

icone_audio = PhotoImage(file='icones/Volume_III.png')
botao_audio_traducao = Button(command=audio_traduzido,highlightthickness=0, font=("Arial", 10, 'bold'),image=icone_audio, border=3)
botao_audio_traducao.place(y=225, x=842)

#Icone de Audio do lado da tela de Inserir Texto
botao_audio = Button(command=audio_texto,highlightthickness=0, font=("Arial", 10, 'bold'),image=icone_audio, border=3)
botao_audio.place(y=225, x=382)

#Icone de Copiar Texto

icone_copiar = PhotoImage(file='icones/Copiar_I.png')
botao_copiar = Button(command=copiar_texto,highlightthickness=0, font=("Arial", 10, 'bold'),image=icone_copiar, border=3)
botao_copiar.place(y=225, x=13)

#Icone de Copiar Texto Traduzido

icone_copiar_traduzido = PhotoImage(file='icones/Copiar_I.png')
botao_copiar_traduzido = Button(command=copiar_texto_traduzido,highlightthickness=0, font=("Arial", 10, 'bold'),image=icone_copiar, border=3)
botao_copiar_traduzido.place(y=225, x=455)


#Criando um Botão para a Lixeira

texto_botao_lixeira = Label(text='LIMPAR',font=("Arial",10,'bold'))
texto_botao_lixeira.place(y=300 , x=500)

icone_lixeira = PhotoImage(file='icones/Lixeira_I.png')
botao_audio_traducao = Button( command=limpar_caixaText,highlightthickness=0, font=("Arial", 10, 'bold'),image=icone_lixeira, border=3)
botao_audio_traducao.place(y=350, x=500)


#Criando um Botão para Buscar no Google
icone_buscar = PhotoImage(file='icones/Pesquisar_I.png')

texto_botao_buscar = Label(text='BUSCAR',font=("Arial",10,'bold'))
texto_botao_buscar.place(y=300, x=296)

botao_buscar = Button(command=pesquisar_web,highlightthickness=0, font=("Arial", 10, 'bold'),image=icone_buscar, border=3)
botao_buscar.place(y=350, x=300)

#Criando um Botão para Sair do Aplicativo
icone_sair = PhotoImage(file='icones/Sair_II.png')

texto_botao_sair = Label(text='SAIR',font=("Arial",10,'bold'))
texto_botao_sair.place(y=300,x=702 )

botao_sair=Button(command=sair,highlightthickness=0, font=("Arial", 10, 'bold'),image=icone_sair, border=3)
botao_sair.place(y=350,x=700)

app.mainloop()