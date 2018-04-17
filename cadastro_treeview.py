# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import sqlite3
import csv
class App:
    def __init__(self, master):
# ---------------------- CONEXÃO COM BANCO DE DADOS ----------------
        self.conectar = sqlite3.connect('banco.db')
        self.c = self.conectar.cursor()
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS clientes(id integer primary key,
        nome TEXT, rg TEXT, cpf TEXT, endereço TEXT, numero TEXT, telefone TEXT,
        celular TEXT, email TEXT, obs TEXT)
        ''')
        
        #a imagem ao lado
        self.imagem = PhotoImage(file='cadastro.png')
        self.imagem2 = PhotoImage(file='atualizar.png')
        # Cria Notebook
        self.abas = Notebook(master,width=1024,height=390)
        self.abas.grid(row=0,column=0)
        # Cria paineis
        self.painel1 = Frame(self.abas)
        self.painel2 = Frame(self.abas)
        self.painel3 = Frame(self.abas)
        #Declara componentes e insere no painel1 = 'Cadastrar'
        Label(self.painel1, image=self.imagem).grid(row=0,column=9,
                                                   rowspan=4,sticky='ewns')
        Label(self.painel1, text='Nome completo: ').grid(row=0,column=0)
        self.nomeEnt = Entry(self.painel1)
        Label(self.painel1, text='RG: ').grid(row=0,column=4)
        self.rgEnt = Entry(self.painel1)
        Label(self.painel1, text='CPF: ').grid(row=0,column=6)
        self.cpfEnt = Entry(self.painel1)
        Label(self.painel1, text='Endereço: ').grid(row=1,column=0)
        self.endEnt = Entry(self.painel1)
        Label(self.painel1, text='Nº Casa: ').grid(row=1,column=4)
        self.numEnt = Entry(self.painel1)
        Label(self.painel1, text='Telefone: ').grid(row=2,column=0)
        self.telEnt = Entry(self.painel1)
        Label(self.painel1, text='Celular: ').grid(row=2,column=2)
        self.celEnt = Entry(self.painel1)
        Label(self.painel1, text='E-mail: ').grid(row=2,column=4)
        self.emailEnt = Entry(self.painel1)
        self.texto = Text(self.painel1,height=10)
        self.texto.insert(END,'Escreva algo...')
        self.btn1 = Button(self.painel1,text='Cadastrar',command=self.cadastrar)
    
        #layout dos componentes do painel1
        self.nomeEnt.grid(row=0,column=1,columnspan=3,sticky='ew',pady=5)
        self.rgEnt.grid(row=0,column=5,sticky='ew',pady=5)
        self.cpfEnt.grid(row=0,column=7,sticky='ew',pady=5)
        self.endEnt.grid(row=1,column=1,columnspan=3,sticky='ew',pady=5)
        self.numEnt.grid(row=1,column=5,sticky='ew',pady=5)
        self.telEnt.grid(row=2,column=1,sticky='ew',pady=5)
        self.celEnt.grid(row=2,column=3,sticky='ew',pady=5)
        self.emailEnt.grid(row=2,column=5,sticky='ew',pady=5)
        #caixa de texto, scroll e botões
        self.texto.grid(row=3,column=0,columnspan=8,sticky='ew',padx=5)
        self.scroll = Scrollbar(self.painel1, command=self.texto.yview)
        self.scroll.grid(row=3,column=8,sticky='ns')
        self.texto.configure(yscrollcommand=self.scroll.set)
        self.btn1.grid(row=4,column=0,columnspan=8,pady=5)
        #----------------------------------------------------
        #Declara componentes e insere no painel2 = 'Pesquisar'
        Label(self.painel2, text='Digite um nome: ').grid(row=0,column=0,pady=5)
        self.entpes = Entry(self.painel2,width=50)
        self.entpes.grid(row=0,column=1,pady=5)
        self.btn2 = Button(self.painel2,text='Pesquisar',
                           width=20,command=self.pesquisar)
        self.btn2.grid(row=0,column=2,pady=5)
        self.btn3 = Button(self.painel2,text='Apagar selecionado',width=20,
                           command=self.apagar)
        self.btn3.grid(row=3,column=0,columnspan=3,pady=5)
        self.btn4 = Button(self.painel2,text='Exportar BD',width=20,command=self.exporta)
        self.btn4.grid(row=3,column=1,columnspan=3,pady=5)
        #Treeview dos resultados
        self.lista = Treeview(self.painel2,columns=('ID','NOME','RG','CPF',
                                                    'ENDEREÇO','Nº CASA',
                                                    'TELEFONE','CELULAR',
                                                    'E-MAIL', 'OBS'),height=8)
        #tamanho de cada coluna
        self.lista.column('ID',width=50,minwidth=50,stretch=False)
        self.lista.column('NOME',width=100,minwidth=100,stretch=False)
        self.lista.column('RG',width=100,minwidth=100,stretch=False)
        self.lista.column('CPF',width=100,minwidth=100,stretch=False)
        self.lista.column('ENDEREÇO',width=100,minwidth=100,stretch=False)
        self.lista.column('Nº CASA',width=100,minwidth=100,stretch=False)
        self.lista.column('TELEFONE',width=100,minwidth=100,stretch=False)
        self.lista.column('CELULAR',width=100,minwidth=100,stretch=False)
        self.lista.column('E-MAIL',width=100,minwidth=100,stretch=False)
        self.lista.column('OBS',width=140,minwidth=140,stretch=False)
        #exibição de cada coluna
        self.lista['show'] = 'headings'
        self.lista.heading('ID', text='ID')
        self.lista.heading('NOME', text='NOME')
        self.lista.heading('RG', text='RG')
        self.lista.heading('CPF', text='CPF')
        self.lista.heading('ENDEREÇO', text='ENDEREÇO')
        self.lista.heading('Nº CASA', text='Nº CASA')
        self.lista.heading('TELEFONE', text='TELEFONE')
        self.lista.heading('CELULAR', text='CELULAR')
        self.lista.heading('E-MAIL', text='E-MAIL')
        self.lista.heading('OBS', text='OBS')
        
        self.lista.grid(row=1,column=0,columnspan=4,pady=5,padx=5)
        self.scrol2 = Scrollbar(self.painel2,command=self.lista.yview)
        self.scrol2.grid(row=1,column=5,pady=5,sticky='ns')
        self.scrol3 = Scrollbar(self.painel2,command=self.lista.xview,
                                orient='horizontal')
        self.scrol3.grid(row=2,column=0,columnspan=4,pady=5,sticky='we')
        self.lista.configure(xscrollcommand=self.scrol3.set)
        self.lista.configure(yscrollcommand=self.scrol2.set)
       #----------------------------------------------------
       #Declara componentes e insere no painel3 = 'Atualizar'
        self.frame = Frame(self.painel3)
        self.frame2 = Frame(self.painel3)
        Label(self.frame, image=self.imagem2).grid(row=0,column=9,
                                                   rowspan=4,sticky='ewns')
        Label(self.frame2,text='ID:').grid(row=0,column=0,sticky='ew',pady=5)
        self.idAtt = Entry(self.frame2)
        Label(self.frame, text='Nome completo: ').grid(row=0,column=0)
        self.nomeAtt = Entry(self.frame)
        Label(self.frame, text='RG: ').grid(row=0,column=4)
        self.rgAtt = Entry(self.frame)
        Label(self.frame, text='CPF: ').grid(row=0,column=6)
        self.cpfAtt = Entry(self.frame)
        Label(self.frame, text='Endereço: ').grid(row=1,column=0)
        self.endAtt = Entry(self.frame)
        Label(self.frame, text='Nº Casa: ').grid(row=1,column=4)
        self.numAtt = Entry(self.frame)
        Label(self.frame, text='Telefone: ').grid(row=2,column=0)
        self.telAtt = Entry(self.frame)
        Label(self.frame, text='Celular: ').grid(row=2,column=2)
        self.celAtt = Entry(self.frame)
        Label(self.frame, text='E-mail: ').grid(row=2,column=4)
        self.emailAtt = Entry(self.frame)
        self.textoAtt = Text(self.frame,height=8)
        self.btn2 = Button(self.frame,text='Atualizar',command=self.att_id)
        self.btn3 = Button(self.frame2,text='Buscar ID',command=self.pes_id)
    
        #layout dos componentes do painel1
        self.frame.grid(row=1,column=0)
        self.frame2.grid(row=0,column=0)
        self.idAtt.grid(row=0,column=1,pady=5)
        self.nomeAtt.grid(row=0,column=1,columnspan=3,sticky='ew',pady=5)
        self.rgAtt.grid(row=0,column=5,sticky='ew',pady=5)
        self.cpfAtt.grid(row=0,column=7,sticky='ew',pady=5)
        self.endAtt.grid(row=1,column=1,columnspan=3,sticky='ew',pady=5)
        self.numAtt.grid(row=1,column=5,sticky='ew',pady=5)
        self.telAtt.grid(row=2,column=1,sticky='ew',pady=5)
        self.celAtt.grid(row=2,column=3,sticky='ew',pady=5)
        self.emailAtt.grid(row=2,column=5,sticky='ew',pady=5)
        
        #caixa de texto, scroll e botões
        self.textoAtt.grid(row=3,column=0,columnspan=8,sticky='ew',padx=5)
        self.scroll = Scrollbar(self.frame, command=self.textoAtt.yview)
        self.scroll.grid(row=3,column=8,sticky='ns')
        self.texto.configure(yscrollcommand=self.scroll.set)
        self.btn2.grid(row=4,column=0,columnspan=8,pady=5)
        self.btn3.grid(row=0,column=2,pady=5)
        
        #desativando os botões e campos
        for child in self.frame.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == 'Entry':
                child.config(state='disable')
            if widget_class == 'Text':
                child.config(state='disable')
            if widget_class == 'Button':
                child.config(state='disable')


        # Cria abas
        self.abas.add(self.painel1, text='Cadastrar')
        self.abas.add(self.painel2, text='Pesquisar')
        self.abas.add(self.painel3, text='Atualizar')

    #função de exportar o banco de dados
    def exporta(self):
        rows = self.c.execute('SELECT * FROM clientes')
        with open('Banco.csv', 'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Nome', 'RG', 'CPF', 'Endereço', 'NºCasa', 
                             'Telefone', 'Celular', 'E-mail', 'Obsrvação'])
            writer.writerows(rows)
            messagebox.showinfo('Aviso','Exportado com sucesso!')

    #função para pesquisar dados no BD
    def pesquisar(self):
        sql = 'SELECT * FROM  clientes WHERE instr(nome,?)'
        nom = self.entpes.get().lower()
        if nom == '':
            messagebox.showinfo('Aviso','Preencha todos os campos')
        else:
            for i in self.lista.get_children():
                self.lista.delete(i)
            for i in self.c.execute(sql,(nom,)):
                self.lista.insert('','end',values=(i))

    #função para apagar no BD com base na linha selecionada        
    def apagar(self):
        if self.lista.selection():
            select_item = self.lista.selection()
            select_id = self.lista.item(select_item)
            value = select_id['values'][0]
            self.c.execute('DELETE FROM clientes WHERE id=?',(str(value)))
            self.conectar.commit()
            select_del = self.lista.selection()[0]  
            self.lista.delete(select_del)
            messagebox.showinfo('Aviso','Contato apagado!')
        else:
            messagebox.showinfo('Aviso','Escolha um contato a ser apagado')
        
        
    #função de cadastrar e verificar se os campos estão vazios
    def cadastrar(self):
        nome = self.nomeEnt.get().lower()
        ende = self.endEnt.get().lower()
        email = self.emailEnt.get().lower()
        obs = self.texto.get(1.0, END)
        rg, cpf, num, tel, cel = 0,0,0,0,0
        #verifica se tem campo vazio
        if nome == '':
            messagebox.showinfo('Aviso','Preencha todos os campos')
        else:
            #verifica se os campos sao numeros
            if (str(self.rgEnt.get()).isdigit() and str(self.cpfEnt.get()).isdigit()\
                and str(self.numEnt.get()).isdigit()and\
                str(self.telEnt.get()).isdigit() and\
                str(self.celEnt.get()).isdigit()):
                    
                rg = self.rgEnt.get()
                cpf = self.cpfEnt.get() 
                num = self.numEnt.get()
                tel =  self.telEnt.get()
                cel =  self.celEnt.get()
            #insere os dados na tebela e em seguida apaga os campos
                self.c.execute('''
                   INSERT INTO clientes(nome,rg,cpf,endereço,numero,
                   telefone,celular,email,obs) VALUES(?,?,?,?,?,?,?,?,?)''',
                                   (nome,rg,cpf,ende,num,tel,cel,email,obs))
                self.conectar.commit()
                messagebox.showinfo('Aviso','Cadastrado com sucesso!')
                self.nomeEnt.delete(0, 'end')
                self.rgEnt.delete(0, 'end')
                self.cpfEnt.delete(0, 'end')
                self.endEnt.delete(0, 'end')
                self.numEnt.delete(0, 'end')
                self.telEnt.delete(0, 'end')
                self.celEnt.delete(0, 'end')
                self.emailEnt.delete(0, 'end')
                self.texto.delete(1.0, 'end')
            else:
                messagebox.showinfo('Aviso','Os campos RG,CPF,Número,Telefone e Celular usam somente números.')
    #função de verificar se o campo  ID está vazio e se é numero
    def pes_id(self):
        sql = 'SELECT * FROM  clientes WHERE id=?'
        ids = self.idAtt.get()
        #defin
        if ids == '':
            messagebox.showinfo('Aviso','Escolha um ID')
        else:
            if str(ids).isdigit():
                #Reativando os botões e campos
                for child in self.frame.winfo_children():
                    widget_class = child.__class__.__name__
                    if widget_class == 'Entry':
                        child.delete(0, END)
                        child.config(state='normal')
                    if widget_class == 'Text':
                        child.delete(1.0, END)
                        child.config(state='normal')
                    if widget_class == 'Button':
                        child.config(state='normal')
                #recuperando os dados no BD
                for i in self.c.execute(sql,(ids,)):
                   self.nomeAtt.insert('end',i[1])
                   self.rgAtt.insert('end',i[2])
                   self.cpfAtt.insert('end',i[3])
                   self.endAtt.insert('end',i[4])
                   self.numAtt.insert('end',i[5])
                   self.telAtt.insert('end',i[6])
                   self.celAtt.insert('end',i[7])
                   self.emailAtt.insert('end',i[8])
                   self.textoAtt.insert('end',i[9])
        
                    
    #função de atualização
    def att_id(self):
        ids = self.idAtt.get()
        nome = self.nomeAtt.get().lower()
        rg = self.rgAtt.get()
        cpf = self.cpfAtt.get()
        ende = self.endAtt.get().lower()
        num = self.numAtt.get()
        tel =  self.telAtt.get()
        cel =  self.celAtt.get()
        email = self.emailAtt.get().lower()
        obs = self.textoAtt.get(1.0, END)
        self.c.execute('''
        UPDATE clientes SET nome=?,rg=?,cpf=?,endereço=?,numero=?,telefone=?,
        celular=?, email=?, obs=? WHERE id=?''',(nome,rg,cpf,ende,num,tel,cel,
                                                 email,obs,ids))
        self.conectar.commit()
        messagebox.showinfo('Aviso','Atualizao com sucesso!')
        #desativando os botões e campos e limpado os campos
        for child in self.frame.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == 'Entry':
                child.delete(0, END)
                child.config(state='disable')
            if widget_class == 'Text':
                child.delete(0, END)
                child.config(state='disable')
            if widget_class == 'Button':
                child.config(state='disable')
        
        
        
                
               
                

             
master = Tk()
master.title('Cadastro de Clientes')
master.geometry('1024x325+0+0')
master.iconbitmap('icon.ico')
master.resizable(0,0)
App(master)
master.mainloop()

