def tag_block(text, classe = 'success'):
    return f'<div class="{classe}">{text}</div>'

if __name__ == '__main__':
    #Testes (assertions)
    assert tag_block('Incluído com sucesso!') == \
           '<div class="success">Incluído com sucesso!</div>'

    assert tag_block('Impossível excluir!', 'error') == \
           '<div class="error">Impossível excluir!</div>'
    
print(tag_block('bloco'))