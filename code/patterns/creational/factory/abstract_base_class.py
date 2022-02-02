from abc import ABC
from enum import Enum, auto

class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')

class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')

###
class HotDrinkFactory(ABC):
    # prepare = factory meathod, often called make(), create()
    def prepare(self, amount):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()

# Option 1
def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None

# Option 2
class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = [] #stores tuple (name, factoryinstance)
    initialized = False

    def __init__(self) -> None:
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                # evaluates sring as a python expression!
                # string into code
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f[0])
        s = input(f'Please pick drink (0-{len(self.factories)-1})')
        idx = int(s)
        s = input('Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)

if __name__ == '__main__':
    # Option 1
    # entry = input('What kind of drink would you like?')
    # drink = make_drink(entry)
    
    # Option 2
    drink = HotDrinkMachine().make_drink()
    drink.consume()