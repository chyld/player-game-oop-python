from src.ninja import Ninja
from src.unicorn import Unicorn

zoo = []
with open('data/creatures.csv') as f:
    for line in f:
        ctype, name = line.split(',')
        name = name.strip()
        if ctype == 'Ninja':
            c = Ninja(name)
        elif ctype == 'Unicorn':
            c = Unicorn(name)
        zoo.append(c)

for c in zoo:
    print(c.__dict__)

n1 = zoo[0]
n2 = zoo[1]

while n1.health > 0 and n2.health > 0:
    n1.attack(n2)
    n2.attack(n1)
