import random

class Monster:
    def __init__(self, name="Zorg", hp=150, attack_power=40):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, character):
        damage = self.attack_power
        character.suffer_damage(damage)

    def is_alive(self):
        return self.hp > 0

    def suffer_damage(self, damage):
        self.hp -= damage
        if self.hp >= 0:
            print(f"{self.name} subit {damage} dégâts. PV restants : {self.hp}")

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Attaque: {self.attack_power})"

    @staticmethod
    def random_monster():
        monsters = [
            Monster(name="Goblin", hp=100, attack_power=20),
            Monster(name="Orc", hp=200, attack_power=30),
            Monster(name="Dragon", hp=500, attack_power=50)
        ]
        return random.choice(monsters)
