import sqlite3


class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('db/banco.db')
        self.create_table()

    def create_table(self):
        c = self.conexao.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
                idusuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                ip TEXT,
                cpf     VARCHAR(11) NOT NULL,
                email TEXT NOT NULL,
                fone TEXT,
                cidade TEXT,
                uf VARCHAR(2) NOT NULL,
                criado_em DATE NOT NULL
        );""")

        self.conexao.commit()

        c.close()
