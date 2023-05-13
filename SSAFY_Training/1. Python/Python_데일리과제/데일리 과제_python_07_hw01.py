class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self,name,kinds):
        self.name = name
        self.kinds = kinds
        Doggy.birth_of_dogs += 1
        Doggy.num_of_dogs += 1
    
    def bark(self):
        print(f'{self.name} : 우왈 우왈')
        
    def __del__(self):
        Doggy.num_of_dogs -= 1     
    
    def get_status(self):
        print(f'태어난 강아지 수{Doggy.birth_of_dogs}, 현재 강아지 수{Doggy.num_of_dogs}')
        
d1 = Doggy('하리보','모르티즈')
d2 = Doggy('딸기','허스키')
d3 = Doggy('잭슨','포메')

print(d1.name, d1.kinds)
print(d2.name, d2.kinds)
print(d3.name, d3.kinds)

d1.bark()
d2.bark()
d3.bark()

del d3

d2.get_status()