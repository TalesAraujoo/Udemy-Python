def tag_block(text, classe = 'success', inline=False):
    tag = 'span' if inline else 'div'

    return f'<{tag} class="{classe}">{text}</{tag}>'

if __name__ == '__main__':
    #Testes (assertions)
    print(tag_block('bloco'))
    print(tag_block('inline e classe', 'info', True))
    print(tag_block('inline', inline=True))
    print(tag_block('falhou', classe='error'))