'''
BLOCO DE NOTAS BEM SIMPLES, AINDA FALTA REVISÃO
'''
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as ScrolledText
from tkinter import font
from tkinter import messagebox
import os

class Main:
    def __init__(self, master):
        #----------- INTERFACE TKINTER ----------

        #----- NOVA JANELA -----
        def create_window():
            window = Toplevel(master)
            window.title('Tipos de fontes')
            window.geometry('500x230')
            window.resizable(0, 0)

            # -----  PEGAR A FONTE SELECIONADA -----
            def selectFont():
                fonte = lista.get(ANCHOR)
                tamanho = int(lista2.get())
                if lista.get(ANCHOR) or lista2.get():
                    self.texto.config(font=(fonte, tamanho))

                window.destroy()

            #----- LISTA DAS FONTES -----
            btn = Button(window, text='Aplicar', command=selectFont)
            btn.grid(column=0, row=2)
            Label(window, text=' Tipos de fonte').grid(column=0, row=0)
            lista = Listbox(window, exportselection=0)
            scrollbar = Scrollbar(window)
            lista.grid(column=0, row=1)
            lista.config(width=50)
            lista.config(yscrollcommand=scrollbar.set)
            scrollbar.grid(column=1, row=1,sticky='ns')
            scrollbar.config(command=lista.yview)

            # ----- TAMANHO DA FONTE -----
            Label(window, text='Tamanho da fonte:').grid(column=2, row=0, rowspan=2)
            lista2 = Entry(window, width=5)
            lista2.grid(column=3, row=0, rowspan=2)
            lista2.insert('end', 10)

            #----- FONTES -----
            fonts = list(font.families())
            fonts.sort()
            for f in fonts:
                lista.insert(END, f)




        #----- MENU -----
        self.frame = Frame(master)
        self.frame.pack()
        self.menu = Menu(master)
        self.formatar = Menu(self.menu, fg='#FF8C00', font=('verdana', '10'), tearoff=0, activebackground='#ff00ff', activeforeground='#fff')
        self.formatar.add_command(label='Fontes', command=create_window)
        self.menuControle = Menu(self.menu, fg='#FF8C00', font=('verdana', '10'), tearoff=0, activebackground='#ff00ff', activeforeground='#fff')
        self.menuControle.add_command(label='Abrir', command=self.abrir)
        self.menuControle.add_command(label='Salvar', command=self.salvar)
        self.menuControle.add_command(label='Sobre', command=self.sobre)
        self.menu.add_cascade(label='Painel', menu=self.menuControle)
        self.menu.add_cascade(label='Opções', menu=self.formatar)
        master.config(menu=self.menu)

        #----- AREA DE TEXTO -----

        self.texto = ScrolledText.ScrolledText(master, state='normal', font=('verdana', 10))
        self.texto.pack(fill=BOTH, expand=1)
        self.texto.focus_set()

        #----- FUNÇÕES -----

    def salvar(self):
        t = self.texto.get(1.0,'end-1c')
        filename = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        filename.write(t)
        filename2 = str(filename)
        filename3 = filename2.split()
        filename.close()
        root.title('Bloco - ' + filename3[1].split('/')[-1])

    def abrir(self):
        filename = filedialog.askopenfilename(defaultextension='.txt')
        f = open(filename, 'r')
        f2 = f.read()
        self.texto.delete(1.0,'end-1c')
        self.texto.insert(1.0, f2)
        filename2 = str(filename)
        filename3 = filename2.split('/')
        f.close()
        root.title('Bloco - ' + filename3[-1])
        
    def sobre(self):
        messagebox.showinfo('Sobre',
        '''Bloco de texto bem simples feito em python para estudos.
        Autor: Jonathan
        Versão: 1.0
        Versão Python: 3.6''')
        
        
            




root = Tk()
root.title('Bloco')
Main(root)
root.mainloop()
