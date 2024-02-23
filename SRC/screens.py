from SQL.controle_banco import conection
class telainicial:
    def cria_tela(self):
        print("""Olá, seja bem vindo! O que você deseja fazer?
              0 - Sair
              1 - Cadastrar livro
              2 - Pesquisar livro
              3 - Excluir livro
              4 - Atualizar informações sobre o livro
              5 - Emprestar livro
              6 - Verificar empréstimo""")
    
    def captura_dados(self):
        i = int(input(": "))
        if i == 0:
            return False
        elif i == 1:
            return 1
        elif i == 2:
            return 2
        elif i == 3:
            return 3
        elif i == 4:
            return 4
        elif i == 5:
            return 5
        elif i == 6:
            return 6
        

class cadastar_livro:
    def get_dados(self):
        