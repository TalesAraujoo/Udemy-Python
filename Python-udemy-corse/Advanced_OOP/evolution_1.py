class Human:
    #class attribute
    species = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name

    def cave_man(self):
        self.species = 'Homo Neanderthalensis'


if __name__ == '__main__':
    jose = Human('Jose')
    grokn = Human('Grokn')
    grokn.cave_man()

    print(f'Jose: {jose.species}')
    print(f'grokn: {grokn.species}')