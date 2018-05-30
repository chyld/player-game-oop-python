from src.creature import Creature
import random


class Unicorn(Creature):
    def __init__(self, name):
        health = random.randint(500, 800)
        super().__init__(name, health)


if __name__ == '__main__':
    n1 = Unicorn('jazzmine')
