class Employee:

    raise_amt = 1.03
    
    def __init__(self,First,Last,Pay):
        self.first = First
        self.last = Last
        self.pay = Pay
        self.email = self.first + self.last + '@gmail.com'

    def apply_raise(self):
        self.rai = int(self.raise_amt * self.pay)
        return self.rai
    
    def __repr__(self):
        return f'{self.first} {self.last}'
    
class Developer(Employee):
    
    raise_amt = 1.10
    
    def __init__(self,First,Last,Pay,Prog_lang):
        super().__init__(First,Last,Pay)
        self.Prog_lang = Prog_lang   

    def apply_raise(self):
        return 'ok'


        
       
D1 = Developer('Shashank','Jain',100,'Pythonh')
D2 = Developer('Corey','Shafer',200,'Java')
        
print(vars(D1))
print(vars(D2))
print('----------------')
print(vars(Developer))
print('--------------------------')
print(vars(Employee))


D2.apply_raise()

D1.Prog_lang 
D1.apply_raise()

