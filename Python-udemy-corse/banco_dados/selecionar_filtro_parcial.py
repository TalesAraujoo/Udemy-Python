from utils import nova_conexao
from mysql.connector import ProgrammingError


sql = """
    SELECT id, nome, tel FROM contatos WHERE nome LIKE '%a%'
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)

        for x in cursor:
            print(x)
    
    except ProgrammingError as e:
        print(f'Error: {e.msg}')