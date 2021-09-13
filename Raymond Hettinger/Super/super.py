class A:
    pass

class B:
    pass

class Adam(A,B):
    def __init__(self):
        self.name = 'Adam'
        
class Eve(A,B):pass

class Ramon(Adam,Eve):pass
class Gayle(Adam,Eve):pass



class Dannis(Adam,Eve):pass
class Sharon(Adam,Eve):pass

class Rachel(Dannis,Sharon):pass


class Raymond(Ramon,Gayle):pass

class Matthew(Raymond,Rachel):pass

print(Matthew().name)

print(Matthew.mro())