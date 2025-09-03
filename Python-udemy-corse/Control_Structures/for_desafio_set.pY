FORBIDDEN_WORDS = {'soccer', 'religion', 'politics'}

texts = [
    'John likes soccer and politics',
    'It was fun being at the beach'
]

# if 'intersection' means that intersection has something in it, its 'TRUE'
for text in texts:
    intersection = FORBIDDEN_WORDS.intersection(set(text.lower().split()))
    if intersection:
        print('Text has forbidden words: ', intersection)
    else: 
        print('Text allowed: ', text)


