from operacoes import Usuarios
# from _tkinter import ttk
from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container = Frame(master)
        self.container["padx"] = 20
        self.container["pady"] = 5
        self.container.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 5
        self.container11.pack()
        self.container12 = Frame(master)
        self.container12["padx"] = 20
        self.container12["pady"] = 5
        self.container12.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        #

        self.lblidusuario = Label(self.container2, text="Busca ID:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscar_usuarios
        self.btnBuscar.pack(side=RIGHT)

        #

        self.lblnome1 = Label(self.container, text="Busca nome:", font=self.fonte, width=10)
        self.lblnome1.pack(side=LEFT)

        self.txtnome1 = Entry(self.container)
        self.txtnome1["width"] = 10
        self.txtnome1["font"] = self.fonte
        self.txtnome1.pack(side=LEFT)

        self.btnBuscar1 = Button(self.container, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar1["command"] = self.buscar_usuarios_nome
        self.btnBuscar1.pack(side=RIGHT)

        #

        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblip = Label(self.container4, text="Ip:", font=self.fonte, width=10)
        self.lblip.pack(side=LEFT)

        self.txtip = Entry(self.container4)
        self.txtip["width"] = 25
        self.txtip["font"] = self.fonte
        self.txtip.pack(side=LEFT)

        self.lblcpf = Label(self.container5, text="CPF:", font=self.fonte, width=10)
        self.lblcpf.pack(side=LEFT)

        self.txtcpf = Entry(self.container5)
        self.txtcpf["width"] = 25
        self.txtcpf["font"] = self.fonte
        self.txtcpf.pack(side=LEFT)

        self.lblemail = Label(self.container6, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container6)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lbltelefone = Label(self.container7, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(self.container7)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        self.lblcidade = Label(self.container8, text="Cidade:", font=self.fonte, width=10)
        self.lblcidade.pack(side=LEFT)

        self.txtcidade = Entry(self.container8)
        self.txtcidade["width"] = 25
        self.txtcidade["font"] = self.fonte
        self.txtcidade.pack(side=LEFT)

        self.lbluf = Label(self.container9, text="UF:", font=self.fonte, width=10)
        self.lbluf.pack(side=LEFT)

        self.txtuf = Entry(self.container9)
        self.txtuf["width"] = 25
        self.txtuf["font"] = self.fonte
        self.txtuf.pack(side=LEFT)

        self.lblcriado_em = Label(self.container10, text="Criado em:", font=self.fonte, width=10)
        self.lblcriado_em.pack(side=LEFT)

        self.txtcriado_em = Entry(self.container10)
        self.txtcriado_em["width"] = 25
        self.txtcriado_em["font"] = self.fonte
        self.txtcriado_em.pack(side=LEFT)

        # Senha e usuário.

        """self.lblusuario = Label(self.container6, text="Usuário:", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)

        self.txtusuario = Entry(self.container6)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.container7, text="Senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)"""

        self.bntInsert = Button(self.container11, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserir_usuario
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container11, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterar_usuario
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container11, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.deletar_usuario
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container12, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserir_usuario(self):
        user = Usuarios()

        user.p_nome = self.txtnome.get()
        user.p_ip = self.txtip.get()
        user.p_cpf = self.txtcpf.get()
        user.p_email = self.txtemail.get()
        user.p_fone = self.txttelefone.get()
        user.p_cidade = self.txtcidade.get()
        user.p_uf = self.txtuf.get()
        user.p_criado_em = self.txtcriado_em.get()

        self.lblmsg["text"] = user.insert_user()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtip.delete(0, END)
        self.txtcpf.delete(0, END)
        self.txtemail.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtcidade.delete(0, END)
        self.txtuf.delete(0, END)
        self.txtcriado_em.delete(0, END)

    def buscar_usuarios(self):
        user = Usuarios()

        idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.select_user(idusuario)

        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.p_nome)

        self.txtip.delete(0, END)
        self.txtip.insert(INSERT, user.p_ip)

        self.txtcpf.delete(0, END)
        self.txtcpf.insert(INSERT, user.p_cpf)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.p_email)

        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT, user.p_fone)

        self.txtcidade.delete(0, END)
        self.txtcidade.insert(INSERT, user.p_cidade)

        self.txtuf.delete(0, END)
        self.txtuf.insert(INSERT, user.p_uf)

        self.txtcriado_em.delete(0, END)
        self.txtcriado_em.insert(INSERT, user.p_criado_em)

    def deletar_usuario(self):
        user = Usuarios()

        idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.delete_user(idusuario)

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtip.delete(0, END)
        self.txtcpf.delete(0, END)
        self.txtemail.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtcidade.delete(0, END)
        self.txtuf.delete(0, END)
        self.txtcriado_em.delete(0, END)

    def alterar_usuario(self):
        user = Usuarios()

        idusuario = self.txtidusuario.get()

        user.p_nome = self.txtnome.get()
        user.p_ip = self.txtip.get()
        user.p_cpf = self.txtcpf.get()
        user.p_email = self.txtemail.get()
        user.p_fone = self.txttelefone.get()
        user.p_cidade = self.txtcidade.get()
        user.p_uf = self.txtuf.get()
        user.p_criado_em = self.txtcriado_em.get()

        self.lblmsg["text"] = user.update_user(idusuario)

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtip.delete(0, END)
        self.txtcpf.delete(0, END)
        self.txtemail.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtcidade.delete(0, END)
        self.txtuf.delete(0, END)
        self.txtcriado_em.delete(0, END)

    def buscar_usuarios_nome(self):
        user = Usuarios()

        p_nome = self.txtnome1.get()

        self.lblmsg["text"] = user.select_user_name(p_nome)

        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.p_nome)

        self.txtip.delete(0, END)
        self.txtip.insert(INSERT, user.p_ip)

        self.txtcpf.delete(0, END)
        self.txtcpf.insert(INSERT, user.p_cpf)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.p_email)

        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT, user.p_fone)

        self.txtcidade.delete(0, END)
        self.txtcidade.insert(INSERT, user.p_cidade)

        self.txtuf.delete(0, END)
        self.txtuf.insert(INSERT, user.p_uf)

        self.txtcriado_em.delete(0, END)
        self.txtcriado_em.insert(INSERT, user.p_criado_em)


# nome, ip, cpf, email, fone, cidade, uf, criado_em
root = Tk()
Application(root)
root.mainloop()
