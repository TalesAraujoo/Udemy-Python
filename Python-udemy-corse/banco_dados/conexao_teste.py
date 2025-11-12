from utils import nova_conexao

with nova_conexao() as conexao: 
    if conexao.is_connected():
        print('Conectado')
    else:
        print('Sem conexão')