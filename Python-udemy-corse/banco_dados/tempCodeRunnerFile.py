from utils import nova_conexao
from mysql.connector import ProgrammingError

sql = """
    ALTER TABLE contatos
        ADD COLUMN IF NOT EXISTS
            id INT AUTO_INCREMENT PRIMARY KEY
"""

with nova_conexao() as conexao:
    try: 
        cursor = conexao.cursor()
        cursor.execute(sql)
        cursor.execute('DESCRIBE contatos')

        for i, table in enumerate(cursor, start = 1):
            print(table)
    except ProgrammingError as e:
        print(f'Error: {e.msg}')