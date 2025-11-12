from abc import ABCMeta, abstractproperty

#turns the class into an abstract class
class Human(metaclass=ABCMeta):
    #class attribute
    species = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name
        self._age = None

    @abstractproperty
    def intelligent(self):
        pass

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError('Age must be a positive number')
        else:
            self._age = age

    def cave_man(self):
        self.specie = 'Homo Neanderthalensis'

    @staticmethod
    def species():
        adjectives = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco', ) + tuple(f'Homo {adj}' for adj in adjectives)

    @classmethod
    def is_evolved(cls):
        return cls.specie == cls.species()[-1]


class Neanderthal(Human):
    specie = Human.species()[-2]

    @property
    def intelligent(self):
        return False


class HomoSapiens(Human):
    specie = Human.species()[-1 ]
    
    @property
    def intelligent(self):
        return True


if __name__ == '__main__':
    anonymous = Human('John Doe')
    
    try:
        print(anonymous.intelligent())
    except NotImplementedError:
        print('Abstract property')


    jose = HomoSapiens('Jose')
    print(f'{jose.name} from class {jose.__class__.__name__}, intelligent: {jose.intelligent}')

    grogn = Neanderthal('Grogn')
    print('{} from class {}, intelligent: {}'
          .format(grogn.name, grogn.__class__.__name__, grogn.intelligent))