from utils import nova_conexao
from mysql.connector import ProgrammingError

sql = """
    INSERT INTO contatos
        (nome, tel)
    VALUES 
        (%s, %s)
"""

args = (
    ('Ana', '98645-1234'),
    ('Bia', '78541-4567'),
    ('Roberto', '78541-4567'),
    ('Flavia', '78541-4577'),
    ('Otaviorio', '78541-4467'),
    ('João', '78541-4117'),
)


with nova_conexao() as conexao:
    try: 
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()

    except ProgrammingError as e:
        print(f'Error: {e.msg}')

    else:
        print('Row count: ', cursor._rowcount)
     