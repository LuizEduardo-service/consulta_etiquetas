import os
import sqlite3 as sq
from tkinter import messagebox

class DataBase:

    def __init__(self) -> None:

        self.parentDirectory = os.path.dirname(os.getcwd())
        dir_data = os.path.join(self.parentDirectory, 'data\\')
        self.dbLocal =dir_data + 'dataBase.db'
        

    def connect_bd(self):
        self.conn = sq.connect(self.dbLocal)
        self.cursor = self.conn.cursor()

    def criar_tabelas(self):
        try:
            self.connect_bd()
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS tb_usuario(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                usuario VARCHAR(100),
                                senha VARCHAR(50)                               

                                )""")

            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS tb_config(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                diretorio VARCHAR(300),
                                nome_arq VARCHAR(100),
                                dir_saida VARCHAR(300),
                                nome_arq_saida VARCHAR(100)
                                )""")
            
            self.conn.commit()
        except:
            messagebox.showerror('Erro Tabela', 'Não foi possivel criar as tabelas!\nVerifique a conexão e tente novamente')
        finally:
            self.conn.close()

    def mostra_dados(self, tabela):
        try:
            self.connect_bd()
            sql= f"""SELECT * FROM {tabela}"""
            self.cursor.execute(sql)
            dados = self.cursor.fetchall()
            return dados
        except:
            messagebox.showerror('Erro Consulta', 'Não foi possivel acessar o banco de dados!\nVerifique a conexão e tente novamente')
        finally:
            self.conn.close()

    def update(self, stringSQL):
        try:
            self.connect_bd()
            self.cursor.execute(stringSQL)
            self.conn.commit()
            messagebox.showinfo('Atualização ', 'Atualização realizada com Sucesso!')
        except:
            messagebox.showerror('Erro Atualização', 'Não foi possivel alterar os dados!\nVerifique a conexão e tente novamente')
        finally:
            self.conn.close()

    def delete(self, stringSQL):
        try:
            self.connect_bd()
            self.cursor.execute(stringSQL)
            self.conn.commit()
            messagebox.showinfo('Exclusão', 'Exclusão realizada com Sucesso!')
        except:
            messagebox.showerror('Erro Exclusão', 'Não foi possivel alterar os dados!\nVerifique a conexão e tente novamente')
        finally:
            self.conn.close()

if __name__ == '__main__':
    bd = DataBase()
    bd.criar_tabelas()