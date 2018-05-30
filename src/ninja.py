from src.creature import Creature
import random


class Ninja(Creature):
    def __init__(self, name):
        health = random.randint(90, 110)
        super().__init__(name, health)
        self.num_hits = 3

    def attack(self, other):
        if self.health > 0 and other.health > 0:
            print("{} is attacking {}".format(self.name, other.name))
            for _ in range(self.num_hits):
                damage = random.randint(0, 5)
                other.receive_hit(damage)

    def receive_hit(self, damage):
        prob_getting_hit = random.randint(0, 2) / 10
        damage_received = damage * prob_getting_hit
        self.health -= damage_received
        print("{} just received {:.2f} amount of damage and has {:.2f} health".format(self.name, damage_received, self.health))


if __name__ == '__main__':
    n1 = Ninja('gandolf')
