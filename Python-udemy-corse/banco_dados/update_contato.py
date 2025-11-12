from utils import nova_conexao
from mysql.connector import ProgrammingError


sql = """
    UPDATE contatos 
    SET nome = %s
    WHERE id = %s
"""

args = ('Ana Flavia', 16)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args    )
        conexao.commit()

        # cursor.execute('SELECT * FROM contatos')
        # for item in cursor:
        #     print('\t'.join(str(tmp) for tmp in item))

    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    
    else:
        print(f'{cursor.rowcount} alterado(s)')