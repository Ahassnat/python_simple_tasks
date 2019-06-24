from Pharm.Custmer import Px
from Pharm.cal import space,vol

x=Px('ahmed',28,'male',8)
x_space=space(x.age,x.type)
x_vol=vol(x.type,x.age)
print(f'the volum is :: {x_vol}, the space{x_space}')
print(f'the name is{x.name} sex is :: {x.sex}')
