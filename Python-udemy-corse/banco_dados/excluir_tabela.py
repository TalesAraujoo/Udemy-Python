from utils import nova_conexao
from mysql.connector import ProgrammingError

tabela_excluir = """
    DROP TABLE IF EXISTS emails;
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_excluir)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')