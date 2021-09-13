class Constant:
    def __init__(self,name):
        self.name = name

    def __setattr__(self,name,value):
        if name == 'pi' and value != 3.14:
            raise AttributeError('pi is a constant can\'t changed')
        super().__setattr__(name,value)


constant = Constant('Shashank')

print(constant.name)

constant.pi = 3.14
print(constant.pi)


class Employee:
    def __init__(self,name):
        self.name = name
    
    def fullName(self):
        return f'{self.name} Jain'

    def __getattr__(self,name):
        print('get attr')
        super().__getattr__(name)

E1 = Employee('Shasank')
print(getattr(E1,'sex','Male'))

E1.first = 24



