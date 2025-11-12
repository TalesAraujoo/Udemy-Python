from utils import nova_conexao
from mysql.connector import ProgrammingError


sql = """
    SELECT nome FROM contatos ORDER BY nome ASC
"""

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for item in cursor:
        print(item)
        # print('\n'.join(registro[0]) for registro in cursor)