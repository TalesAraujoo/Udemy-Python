def tag_block(text, classe = 'success', inline=False):
    tag = 'span' if inline else 'div'

    return f'<{tag} class="{classe}">{text}</{tag}>'


def tag_list(*itens):
    list = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{list}</ul'


if __name__ == '__main__':
    #Testes (assertions)
    print(tag_block('bloco'))
    print(tag_block('inline e classe', 'info', True))
    print(tag_block('inline', inline=True))
    print(tag_block('falhou', classe='error'))

    print(tag_block(tag_list('item 1', 'Item 2'), classe = 'info'))