from utils import nova_conexao
from mysql.connector import ProgrammingError


sql = """
    DELETE FROM contatos WHERE nome = %s
"""

args = ('Lucas',)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()

        cursor.execute('SELECT * FROM contatos')
        for item in cursor:
            print(item)

    except ProgrammingError as e:
        print(f'Error: {e.msg}')