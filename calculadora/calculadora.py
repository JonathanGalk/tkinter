from tkinter import *

class calculadora:
    def __init__(self, master):
        #Imagens dos botões
        self.btn1Img = PhotoImage(file='btn1.gif')
        self.btn2Img = PhotoImage(file='btn2.gif')
        self.btn3Img = PhotoImage(file='btn3.gif')
        self.btn4Img = PhotoImage(file='btn4.gif')
        self.btn5Img = PhotoImage(file='btn5.gif')
        self.btn6Img = PhotoImage(file='btn6.gif')
        self.btn7Img = PhotoImage(file='btn7.gif')
        self.btn8Img = PhotoImage(file='btn8.gif')
        self.btn9Img = PhotoImage(file='btn9.gif')
        self.btn0Img = PhotoImage(file='btn0.gif')
        self.btnSomImg = PhotoImage(file='btnSom.gif')
        self.btnSubImg = PhotoImage(file='btnSub.gif')
        self.btnDivImg = PhotoImage(file='btnDiv.gif')
        self.btnMultImg = PhotoImage(file='btnMult.gif')
        self.btnPonImg = PhotoImage(file='btnPon.gif')
        self.btnIgImg = PhotoImage(file='btnIg.gif')
        self.btnCImg = PhotoImage(file='btnC.gif')
        

        self.frame1 = Frame(master)
        self.frame2 = Frame(master)
 

        self.frame1.grid(column=0,row=0)
        self.frame2.grid(column=0,row=1)
     

        self.ent = Entry(self.frame1,justify='right',font=('verdana', 13),bd=5)
        self.ent.grid(column=0,row=0,columnspan=4)
        self.ent.config(state='disable')
        
        #Botões de 7 a porcentagem
        self.btn7 = Button(self.frame2, image=self.btn7Img,
                           command=lambda:self.insert('7'))
        self.btn8 = Button(self.frame2, image=self.btn8Img,
                           command=lambda:self.insert('8'))
        self.btn9 = Button(self.frame2, image=self.btn9Img,
                           command=lambda:self.insert('9'))
        self.btnPor = Button(self.frame2, image=self.btnPonImg,
                             command=lambda:self.insert('.'))
        self.btn7.grid(column=0,row=0)
        self.btn8.grid(column=1,row=0)
        self.btn9.grid(column=2,row=0)
        self.btnPor.grid(column=3,row=0)

        #Botões de 4 a divisão
        self.btn4 = Button(self.frame2, image=self.btn4Img,
                           command=lambda:self.insert('4'))
        self.btn5 = Button(self.frame2, image=self.btn5Img,
                           command=lambda:self.insert('5'))
        self.btn6 = Button(self.frame2, image=self.btn6Img,
                           command=lambda:self.insert('6'))
        self.btnDiv = Button(self.frame2, image=self.btnDivImg,
                             command=lambda:self.insert('/'))
        self.btn4.grid(column=0,row=1)
        self.btn5.grid(column=1,row=1)
        self.btn6.grid(column=2,row=1)
        self.btnDiv.grid(column=3,row=1)

        #Botões de 1 a multiplicação
        self.btn1 = Button(self.frame2, image=self.btn1Img,
                           command=lambda:self.insert('1'))
        self.btn2 = Button(self.frame2, image=self.btn2Img,
                           command=lambda:self.insert('2'))
        self.btn3 = Button(self.frame2, image=self.btn3Img,
                           command=lambda:self.insert('3'))
        self.btnMul = Button(self.frame2, image=self.btnMultImg,
                             command=lambda:self.insert('*'))
        self.btn1.grid(column=0,row=2)
        self.btn2.grid(column=1,row=2)
        self.btn3.grid(column=2,row=2)
        self.btnMul.grid(column=3,row=2)

        #Botões de 0 a  soma
        self.btn0 = Button(self.frame2, image=self.btn0Img,
                           command=lambda:self.insert('0'))
        self.btnIg = Button(self.frame2, image=self.btnIgImg,command=self.igual)
        self.btnSub = Button(self.frame2, image=self.btnSubImg,
                             command=lambda:self.insert('-'))
        self.btnSom = Button(self.frame2, image=self.btnSomImg,
                             command=lambda:self.insert('+'))
        self.btn0.grid(column=0,row=3)
        self.btnIg.grid(column=1,row=3)
        self.btnSub.grid(column=2,row=3)
        self.btnSom.grid(column=3,row=3)

        #Botão limpar
        self.btnC = Button(self.frame2,image=self.btnCImg,command=self.limpar)
        self.btnC.grid(column=0,row=4,sticky='we',columnspan=4)

        #Aplicando efeito sem borda em todos os boões
        for child in self.frame2.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == 'Button':
                child.config(borderwidth=0)


    def insert(self,texto):
        '''Função para inserir o texto do botão no entry'''
        self.ent.config(state='normal')
        self.ent.insert(END, texto)
        self.ent.config(state='disable')

    def limpar(self):
        '''Função para limpar o campo entry'''
        self.ent.config(state='normal')
        self.ent.delete(0, END)
        self.ent.config(state='disable')

    def igual(self):
        '''Função que chama o resultado da operação'''
        self.ent.config(state='normal')
        r = self.ent.get()
        rn = round(eval(r),2)
        self.ent.delete(0, END)
        self.ent.insert(END, rn)
        self.ent.config(state='disable')

        
        


master = Tk()
calculadora(master)
master.title('Calc')
master.resizable(False, False)
master.mainloop()
