class Person:
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percentage):
        self.pay = int(self.pay * (1+percentage)) + 100
    def __repr__(self):
        return f'[Person : {self.name}; {self.pay}]'

class Manager:
    def __init__(self,name,pay):
        self.person = Person(name,'mgr',pay)
    def giveRaise(self,percent,bonus=.1):
        self.person.giveRaise(percent + bonus)
    def __getattr__(self,attr):
        print(f'get attar : {attr=}')
        return getattr(self.person,attr)
    def __repr__(self):
        return f'[Manager : {self.name}; {self.pay}]'

if __name__=='__main__':
    Bob = Person('Bob Smith')
    Sue = Person('Sue Jones',job='dev',pay=1_00_000)
    print(Bob)
    print(Sue)
    Sue.giveRaise(.1)
    Tom = Manager('Tom Jones',50000)
    Tom.giveRaise(.1)
    print(Tom.pay)
    print(Tom)
