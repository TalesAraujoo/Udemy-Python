FORBIDDEN_WORDS = ('soccer', 'religion', 'politics')

texts = [
    'John likes soccer and politics',
    'It was fun being at the beach'
]
for text in texts:
    found = False
    for word in text.lower().split():
        if word in FORBIDDEN_WORDS:
            print('The text has at least one forbidden word: ', word)
            found = True
            break
    
    if not found:
        print('Text Authorized: ', text)