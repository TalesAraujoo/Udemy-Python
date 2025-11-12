from utils import nova_conexao
from mysql.connector import ProgrammingError

sql = """
    SELECT * FROM contatos WHERE nome LIKE %s
"""


with nova_conexao() as conexao:
    try:
        nome = input('Contato a localizar: ')
        args = (f'%{nome}%',) # it has to be a tuple

        cursor = conexao.cursor()
        cursor.execute(sql, args)

        for item in cursor:
            print(item)

    except ProgrammingError as e:
        print(f'Error: {e.msg}')