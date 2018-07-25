#-*-coding:utf8;-*-
#Joguinho simples de campo minado, quando inicia o jogo ele mostra por alguns
#instantes as localizações das bombas, cada acerto garente 1 ponto, divirta-se!

#Importações
from tkinter import *
from tkinter import messagebox
from random import choice

class Campo_minado():
    '''
        Classe que cria a interface dos botões no tkinter
    '''
    def __init__(self, janela):
        self.photo = PhotoImage(file='bomb.gif')
        self.photo2 = PhotoImage(file='fund.gif')
        self.photo3 = PhotoImage(file='ponto.gif')
        self.pontos = 0
            
        self.texto = Label(janela,text=self.pontos,bg='#778899',
                           font=('Verdana', 20),padx=5,fg='#FF0000')
        self.texto.grid(row=0,column=3,columnspan=7,sticky='ew')

        self.start = Button(janela,text='Começar',font=('Verdana', 12),
                          command=lambda event = True:self.inicio(event))
        self.start.grid(row=0,column=0,columnspan=3,sticky='ewns')
        
        #Cria os botões e os armazena em uma lista
        self.botoes = []
        for i in range(0,60):
            btn = Button(janela, image=self.photo2)
            self.botoes.append(btn)
        #Define as posições dos botões
        row, column = 1, 0
        for botao in self.botoes:
            botao.grid(row = row, column = column)
            if column == 9: 
                column = 0
                row+=1
            else:
                column+=1 

#Funções do jogo
    def inicio(self,event):
        #configuração para começar o jogo
        if event == True:
            self.config()
        else:
            for i in self.botoes:
                i.configure(state='disabled')
            
    def config(self):
    #função com as configurações iniciais
    #cria um lista com todos os botões e uma lista vazia, escolhe alguns
    #e dessa lista nova são colocados com a função de bomba
        
        self.lista = []
        
        for i in self.botoes:
            i.config(command=lambda event=i: self.ponto(event),
            relief='raised',state='normal',image=self.photo2)
        #vezes que um botão é adicionado a lista    
        while len(self.lista) < 15:
            esc = choice(self.botoes)
            if esc not in self.lista:
                self.lista.append(esc)
        for item in self.lista:
            item.config(command=lambda event = item:self.bomba(event))
            print(item)
        print('-----------')
        self.radar()


        
    def ponto(self,event):
        #função que marca os pontos e muda a imagem
        global pontos, novo
        event.config(relief=SUNKEN, image=self.photo3)
        event.config(command=0)
        self.pontos += 1
        self.texto.config(text=self.pontos)
        if self.pontos == 45:
            messagebox.showinfo('VITÓRIA!','Você venceu este desafio!!!')
            self.pontos = 0
            self.inicio(False)

    def bomba(self, event):
        #essa função é para explodir e terminar o jogo, alem de mostrar a bomba
        global pontos
        event.config(relief=SUNKEN, image=self.photo)
        messagebox.showinfo('BOOM!','Fim de Jogo!')
        self.pontos = 0
        self.inicio(False)
        
    def radar(self):
        for i in self.lista:
            i.config(image=self.photo)
        janela.after(1500, self.normal)
        
    def normal(self):
        for i in self.lista:
            i.config(image=self.photo2)
    
janela = Tk()
janela.title('Campo minado')
janela.geometry('360x253+500+200')
janela.resizable(0,0)
Campo_minado(janela)
janela.mainloop()
