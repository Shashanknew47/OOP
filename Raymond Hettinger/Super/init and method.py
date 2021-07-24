class GFather:
    def __init__(self):
        print('Gf')
        self.G = 'G'

    def getvalue(self):
        print('gf')

class Father(GFather):
    Hair_color = 'Brown_hair'
    def __init__(self):
        self.F = 'Father'
        print('Father')
        super().__init__()

    def getvalue(self):
        print('getfather')
        super().getvalue()
    

class Mother(GFather):
    Mo = 'Mom'
    def __init__(self):
        print('Mother')
        self.M = 'Mother'
        super().__init__()
    
    def getvalue(self):
        print('getmother')
        super().getvalue()

class Child(Mother,Father):
    def __init__(self):
        print('Child')
        self.B = 'Baby'
        super().__init__()

    def getvalue(self):
        print('getchild')
        super().getvalue()


C1 = Child()

print(C1.Mo)
print(Child.__mro__)
(C1.getvalue())
