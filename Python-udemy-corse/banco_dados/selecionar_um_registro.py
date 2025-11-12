from utils import nova_conexao

sql = """
    SELECT tel, nome from contatos
"""

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    print(cursor.fetchone())