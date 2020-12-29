
class FirstClass:                     # defines a class object
    def setdata(self, value):         # Define class's mehtod
        self.data = value             # self in instance

    def display(self):
        return (self.data)


class Secondclass(FirstClass):
    def display(self):
        print(f'Current value = {self.data}')


class ThirdClass(Secondclass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
      return 'ThirdClass : %s' % self.data

    def mul(self, other):
        self.data *= other


a = ThirdClass('abc')
b = a + 'xyz'

print(b)
a.display()

a.mul(2)
print(a)

"""
. __init__ is run when a new instance object is created. self is the new ThirdClass object.
. __add__ is run when a ThirdClass instance appears in a+ expression.
. __str__ is run when an object is printed (technically, when it's converted to its print string by the str 
          built-in function or its Python inernals equivalent.


"""
