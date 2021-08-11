from banco import Banco


class Usuarios(object):
    def __init__(self, idusuario=0, p_nome="", p_ip="", p_cpf="", p_email="", p_fone="", p_cidade="", p_uf="",
                 p_criado_em=""):
        self.info = {}
        self.idusuario = idusuario
        self.p_nome = p_nome
        self.p_ip = p_ip
        self.p_cpf = p_cpf
        self.p_email = p_email
        self.p_fone = p_fone
        self.p_cidade = p_cidade
        self.p_uf = p_uf
        self.p_criado_em = p_criado_em

    def insert_user(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute(
                " INSERT INTO usuarios (nome, ip, cpf, email, fone, cidade, uf, criado_em) VALUES ('" + self.p_nome + "','" + self.p_ip + "','" + self.p_cpf + "','" + self.p_email + "','" + self.p_fone + "', '" + self.p_cidade + "', '" + self.p_uf + "', '" + self.p_criado_em + "' )")

            banco.conexao.commit()
            c.close()

            return ("Usuário cadastrado com sucesso.")
        except:
            return ("Ocorreu um erro na inserção do usuário.")

    def update_user(self, idusuario):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute(
                " update usuarios set nome = '" + self.p_nome + "', ip = '"
                + self.p_ip + "', cpf = '" + self.p_cpf + "', email = '" + self.p_email + "', fone = '"
                + self.p_fone + "' where idusuario = " +
                idusuario + "")

            banco.conexao.commit()
            c.close()

            return ("Usuário atualizado com sucesso!")
        except:
            return ("Ocorreu um erro na alteração do usuário.")

    def delete_user(self, idusuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where idusuario = " + idusuario + " ")

            banco.conexao.commit()
            c.close()

            return ("Usuário excluído com sucesso!")
        except:
            return ("Ocorreu um erro na exclusão do usuário.")

    def select_user(self, idusuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where idusuario = " + idusuario + "")

            for linha in c:
                self.idusuario = linha[0]
                self.p_nome = linha[1]
                self.p_ip = linha[2]
                self.p_cpf = linha[3]
                self.p_email = linha[4]
                self.p_fone = linha[5]
                self.p_cip = linha[6]
                self.p_uf = linha[7]
                self.p_criado_em = linha[8]
            # idusuario, nome, ip, cpf, email, fone, cidade, uf, criado_em
            c.close()

            return ("Busca feita com sucesso!")
        except:
            return ("Ocorreu um erro na busca do usuário.")

    def select_user_name(self, p_nome):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute('select * from usuarios where nome = "{}"'.format(p_nome))

            for linha in c:
                self.idusuario = linha[0]
                self.p_nome = linha[1]
                self.p_ip = linha[2]
                self.p_cpf = linha[3]
                self.p_email = linha[4]
                self.p_fone = linha[5]
                self.p_cidade = linha[6]
                self.p_uf = linha[7]
                self.p_criado_em = linha[8]
            # idusuario, nome, ip, cpf, email, fone, cidade, uf, criado_em
            c.close()
            return("Busca feita com sucesso!")
        except:
            return ("Ocorreu um erro na busca do usuário.")
