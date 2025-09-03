FORBIDDEN_WORDS = ('soccer', 'religion', 'politics')

texts = [
    'John likes soccer and politics',
    'It was fun being at the beach'
]
for text in texts:
    for word in text.lower().split():
        if word in FORBIDDEN_WORDS:
            print('The text has at least one forbidden word: ', word)
            break
    else:
        print('Text Authorized: ', text)