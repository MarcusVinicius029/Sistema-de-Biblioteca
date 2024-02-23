import os
import sqlite3

class bd_control:
    caminho_bd = "Sistema-de-Biblioteca/SQL/Banco.db"
    if os.path.exists(caminho_bd):
        caminho_bd = os.path.join("Sistema-de-Biblioteca/SQL/Banco.db")
        con = sqlite3.connect(caminho_bd)
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Livros (nome_livro text, autor text, emprestimo boolean, pessoa_emprestimo text)")
        con.commit()
    else:
        os.mkdir("Sistema-de-Biblioteca/SQL/Banco.db")
        caminho_bd = os.path.join("Sistema-de-Biblioteca/SQL/Banco.db")
        con = sqlite3.connect(caminho_bd)
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Livros (nome_livro text, autor text, emprestimo boolean, pessoa_emprestimo text)")
        con.commit
            
    def entrada_de_dados(self, **kargs):
           self.cursor.execute("SELECT nome_livro, autor FROM Livros")
           