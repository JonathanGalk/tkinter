#-*-coding:utf8;-*-
#Joguinho simples de campo minado, quando inicia o jogo ele mostra por alguns
#instantes as localizações das bombas, cada acerto garente 1 ponto, divita-se!

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
        
        self.btn1 = Button(janela,image=self.photo2)
        self.btn1.grid(row=1,column=0)

        self.btn2 = Button(janela,image=self.photo2)
        self.btn2.grid(row=1,column=1)

        self.btn3 = Button(janela,image=self.photo2)
        self.btn3.grid(row=1,column=2)

        self.btn4 = Button(janela,image=self.photo2)
        self.btn4.grid(row=1,column=3)

        self.btn5 = Button(janela,image=self.photo2)
        self.btn5.grid(row=1,column=4)

        self.btn6 = Button(janela,image=self.photo2)
        self.btn6.grid(row=1,column=5)

        self.btn7 = Button(janela,image=self.photo2)
        self.btn7.grid(row=1,column=6)

        self.btn8 = Button(janela,image=self.photo2)
        self.btn8.grid(row=1,column=7)

        self.btn9 = Button(janela,image=self.photo2)
        self.btn9.grid(row=1,column=8)

        self.btn10 = Button(janela,image=self.photo2)
        self.btn10.grid(row=1,column=9)

        self.btn11 = Button(janela,image=self.photo2)
        self.btn11.grid(row=2,column=0)

        self.btn12 = Button(janela,image=self.photo2)
        self.btn12.grid(row=2,column=1)

        self.btn13 = Button(janela,image=self.photo2)
        self.btn13.grid(row=2,column=2)

        self.btn14 = Button(janela,image=self.photo2)
        self.btn14.grid(row=2,column=3)

        self.btn15 = Button(janela,image=self.photo2)
        self.btn15.grid(row=2,column=4)

        self.btn16 = Button(janela,image=self.photo2)
        self.btn16.grid(row=2,column=5)

        self.btn17 = Button(janela,image=self.photo2)
        self.btn17.grid(row=2,column=6)

        self.btn18 = Button(janela,image=self.photo2)
        self.btn18.grid(row=2,column=7)

        self.btn19 = Button(janela,image=self.photo2)
        self.btn19.grid(row=2,column=8)

        self.btn20 = Button(janela,image=self.photo2)
        self.btn20.grid(row=2,column=9)

        self.btn21 = Button(janela,image=self.photo2)
        self.btn21.grid(row=3,column=0)

        self.btn22 = Button(janela,image=self.photo2)
        self.btn22.grid(row=3,column=1)

        self.btn23 = Button(janela,image=self.photo2)
        self.btn23.grid(row=3,column=2)

        self.btn24 = Button(janela,image=self.photo2)
        self.btn24.grid(row=3,column=3)

        self.btn25 = Button(janela,image=self.photo2)
        self.btn25.grid(row=3,column=4)

        self.btn26 = Button(janela,image=self.photo2)
        self.btn26.grid(row=3,column=5)

        self.btn27 = Button(janela,image=self.photo2)
        self.btn27.grid(row=3,column=6)

        self.btn28 = Button(janela,image=self.photo2)
        self.btn28.grid(row=3,column=7)

        self.btn29 = Button(janela,image=self.photo2)
        self.btn29.grid(row=3,column=8)

        self.btn30 = Button(janela,image=self.photo2)
        self.btn30.grid(row=3,column=9)

        self.btn31 = Button(janela,image=self.photo2)
        self.btn31.grid(row=4,column=0)

        self.btn32 = Button(janela,image=self.photo2)
        self.btn32.grid(row=4,column=1)

        self.btn33 = Button(janela,image=self.photo2)
        self.btn33.grid(row=4,column=2)

        self.btn34 = Button(janela,image=self.photo2)
        self.btn34.grid(row=4,column=3)

        self.btn35 = Button(janela,image=self.photo2)
        self.btn35.grid(row=4,column=4)

        self.btn36 = Button(janela,image=self.photo2)
        self.btn36.grid(row=4,column=5)

        self.btn37 = Button(janela,image=self.photo2)
        self.btn37.grid(row=4,column=6)

        self.btn38 = Button(janela,image=self.photo2)
        self.btn38.grid(row=4,column=7)

        self.btn39 = Button(janela,image=self.photo2)
        self.btn39.grid(row=4,column=8)

        self.btn40 = Button(janela,image=self.photo2)
        self.btn40.grid(row=4,column=9)

        self.btn41 = Button(janela,image=self.photo2)
        self.btn41.grid(row=5,column=0)

        self.btn42 = Button(janela,image=self.photo2)
        self.btn42.grid(row=5,column=1)

        self.btn43 = Button(janela,image=self.photo2)
        self.btn43.grid(row=5,column=2)

        self.btn44 = Button(janela,image=self.photo2)
        self.btn44.grid(row=5,column=3)

        self.btn45 = Button(janela,image=self.photo2)
        self.btn45.grid(row=5,column=4)

        self.btn46 = Button(janela,image=self.photo2)
        self.btn46.grid(row=5,column=5)

        self.btn47 = Button(janela,image=self.photo2)
        self.btn47.grid(row=5,column=6)

        self.btn48 = Button(janela,image=self.photo2)
        self.btn48.grid(row=5,column=7)

        self.btn49 = Button(janela,image=self.photo2)
        self.btn49.grid(row=5,column=8)

        self.btn50 = Button(janela,image=self.photo2)
        self.btn50.grid(row=5,column=9)

        self.btn51 = Button(janela,image=self.photo2)
        self.btn51.grid(row=6,column=0)

        self.btn52 = Button(janela,image=self.photo2)
        self.btn52.grid(row=6,column=1)

        self.btn53 = Button(janela,image=self.photo2)
        self.btn53.grid(row=6,column=2)

        self.btn54 = Button(janela,image=self.photo2)
        self.btn54.grid(row=6,column=3)

        self.btn55 = Button(janela,image=self.photo2)
        self.btn55.grid(row=6,column=4)

        self.btn56 = Button(janela,image=self.photo2)
        self.btn56.grid(row=6,column=5)

        self.btn57 = Button(janela,image=self.photo2)
        self.btn57.grid(row=6,column=6)

        self.btn58 = Button(janela,image=self.photo2)
        self.btn58.grid(row=6,column=7)

        self.btn59 = Button(janela,image=self.photo2)
        self.btn59.grid(row=6,column=8)

        self.btn60 = Button(janela,image=self.photo2)
        self.btn60.grid(row=6,column=9)

        

#Funções do jogo
    def inicio(self,event):
        #configuração para começar o jogo
        if event == True:
            self.config()
        else:
            for i in self.btns:
                i.configure(state='disabled')
            
    def config(self):
    #função com as configurações iniciais
    #cria um lista com todos os botões e uma lista vazia, escolhe alguns
    #e dessa lista nova são colocados com a função de bomba
        self.btns = [
            self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,
            self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,
            self.btn11,self.btn12,self.btn13,self.btn14,self.btn15,
            self.btn16,self.btn17,self.btn18,self.btn19,self.btn20,
            self.btn21,self.btn22,self.btn23,self.btn24,self.btn25,
            self.btn26,self.btn27,self.btn28,self.btn29,self.btn30,
            self.btn31,self.btn32,self.btn33,self.btn34,self.btn35,
            self.btn36,self.btn37,self.btn38,self.btn39,self.btn40,
            self.btn41,self.btn42,self.btn43,self.btn44,self.btn45,
            self.btn46,self.btn47,self.btn48,self.btn49,self.btn50,
            self.btn51,self.btn52,self.btn53,self.btn54,self.btn55,
            self.btn56,self.btn57,self.btn58,self.btn59,self.btn60]
        
        self.lista = []
        
        for i in self.btns:
            i.config(command=lambda event=i: self.ponto(event),
            relief='raised',state='normal',image=self.photo2)
        #vezes que um botão é adicionado a lista    
        while len(self.lista) < 15:
            esc = choice(self.btns)
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
