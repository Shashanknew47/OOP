class DoughFactory(object):

    def get_dough(self):
        return 'insectiside treated wheat dough'


class Pizza(DoughFactory):

    def order_pizza(self,*toppings):
        print('getting dough')
        dough = super().get_dough()
        print(f'Making pie with {dough}.')
        for topping in toppings:
            print(f'Addings :  {topping}')


class OrganicDoughFactory(DoughFactory):

    def get_dough(self):
        return 'pure untreated wheat dough'

class OrganicPizza(Pizza,OrganicDoughFactory):
    pass

OrganicPizza().order_pizza('Onion','Mushroom')


print(help(OrganicPizza()))