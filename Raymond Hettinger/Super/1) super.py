class Adam:
    def __init__(self):
        self.name = 'Adam'
        
class Eve:pass

class Ramon(Adam,Eve):pass
class Gayle(Adam,Eve):pass

class Raymond(Ramon,Gayle):pass


class Dannis(Adam,Eve):pass
class Sharon(Adam,Eve):pass

class Rachel(Dannis,Sharon):pass



class Matthew(Raymond,Rachel):pass

print(Matthew().name)
