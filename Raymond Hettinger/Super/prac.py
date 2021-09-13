class Cheese:
    def get_cheese(self):
        return 'add cheese'


class VeganCheese(Cheese):
    def get_cheese(self):
        return 'add vegan cheese'


class Pizza(Cheese):
    def __init__(self,*toppings):
        self.toppings = toppings

    def make_pizza(self):
        print('add dough')
        gc = super().get_cheese()
        print(f'cook it and {gc}')
        print('add below topings:')
        for t in self.toppings:
            print(t)
        return '-- Pizza is ready --'


P1 = Pizza('Onion','Mashroom','Olives')

print(P1.make_pizza())

class VeganPizz(Pizza,VeganCheese):
    pass

VeganP1 = VeganPizz('Onion','Mashroom','Olives')
print(VeganP1.make_pizza())