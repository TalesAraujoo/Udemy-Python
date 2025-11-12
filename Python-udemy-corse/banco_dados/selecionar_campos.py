from utils import nova_conexao
from mysql.connector import ProgrammingError

sql = """
    SELECT tel, nome from contatos
"""


with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    contatos = cursor.fetchall()

    for contato in contatos:
        print('\t'.join(str(campo) for campo in contato))
    

