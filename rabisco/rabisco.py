'''
Pequeno programa para desenhar, coisas de fim de sábado sem nada para fazer kkk
'''
from tkinter import *
from tkinter.colorchooser import askcolor

class Tela():
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('420x450')
        self.janela.title('Rabiscando')
        self.janela.resizable(0, 0)
        #Criando canvas, onde será feito os desenhos
        self.canvas = Canvas(self.janela, width=420,height=400,
                             bg='white',cursor='pencil')
        self.canvas.pack()
        #Assossiando as funções ao mouse
        self.canvas.bind('<B1-Motion>', self.lapis)
        self.canvas.bind('<ButtonRelease-1>', self.parar)
        #Criando um frame para guardar os botões
        self.frame = Frame(self.janela)
        self.frame.pack()
        self.btn = Button(self.frame, text='Borracha', command=self.apagar)
        self.btn.pack(side=LEFT,fill=BOTH)
        self.btn2 = Button(self.frame,text='Lápis',command=self.lapis_n)
        self.btn2.pack(side=LEFT,fill=BOTH)
        self.btn3 = Button(self.frame,text='Limpar tela',command=self.apagar_t)
        self.btn3.pack(side=LEFT,fill=BOTH)
        self.btn4 = Button(self.frame, text='Cores',command=self.cores)
        self.btn4.pack(side=LEFT,fill=BOTH)
        Label(self.frame, text='Tamanho da borracha / Lápis: ').pack(side=LEFT,
                                                                     fill=BOTH)
        self.btn1 = Scale(self.frame,from_=1,to=10,orient='horizontal')
        self.btn1.pack(side=LEFT,fill=BOTH)

        
        #Chamando as configurações iniciais
        self.config()
        self.janela.mainloop()
       

    def config(self):
        #função que contem as configurações padrões
        self.borracha = False
        self.cor = 'black'
        self.xold = None
        self.yold = None
        self.larg = self.btn1.get()
    
    def lapis(self,event):
        #função que cria o lapis e as linhas
        self.larg = self.btn1.get()
        cor1 = 'white' if self.borracha == True else self.cor
        if self.xold  and self.yold:
            self.canvas.create_line(event.x, event.y, self.xold, self.yold,
                          capstyle=ROUND,fill=cor1,width=self.larg)
        self.xold = event.x
        self.yold = event.y
        
    def lapis_n(self):
        #função para retornar as configurações originais do lapis
        self.cor = 'black'
        self.borracha = False
        self.canvas.configure(cursor='pencil')
        
    def parar(self,event):
        #função que zera as coordenadas do mouse, fanzendo assim um traço normal
        self.xold = None
        self.yold = None

    def apagar_t(self):
        #função para limpar toda a tela
        self.canvas.delete('all')
        
    def apagar(self):
        #função que torna o lapis uma borracha
        self.cursor = self.canvas.configure(cursor='target')
        self.borracha = True
        self.larg *= 2
       
    def cores(self):
        #função que chama a palheta de cores, o 1 éo padrão definido na
        #função config la em cima 'black'
        self.cor = askcolor(color=self.cor)[1]
        

Tela()


