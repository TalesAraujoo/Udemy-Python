class Animal:
    @property
    def capacities(self):
        return ('sleep', 'eat', 'drink')


class Human(Animal):
    @property
    def capacities(self):
        return super().capacities + ('love', 'speak', 'study')
    

class Spider(Animal):
    @property
    def capacities(self):
        return super().capacities + ('create web', 'Walk on walls')
    

class SpiderMan(Human, Spider):
    @property
    def capacities(self):
        return super().capacities + \
            ('hit on bad guys', 'throw web around')
    
if __name__ == '__main__':

    john = Human()
    print(f'John: {john.capacities}')

    spider = Spider()
    print(f'Spider: {spider.capacities}')

    peter = SpiderMan()
    print(f'Peter Parker: {peter.capacities}')