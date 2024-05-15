class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} a été ajouté à l'inventaire.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} a été retiré de l'inventaire.")
        else:
            print(f"L'objet {item} n'est pas dans l'inventaire.")

    def view_items(self):
        if self.items:
            print("Inventaire:")
            for item in self.items:
                print(item)
        else:
            print("L'inventaire est vide.")

class Character:
    def __init__(self, name, health, attack, weapon):
        self.name = name
        self.health = health
        self.attack = attack
        self.weapon = weapon
        self.inventory = Inventory()
        if weapon:
            self.inventory.add_item(weapon)

    def attacking(self, target):
        target.health -= self.attack
        print(f"{self.name} attaque {target.name}")

    def alive(self):
        return self.health > 0

    def view_inventory(self):
        self.inventory.view_items()


    def view_details(self):
        character_class_name = type(self).__name__
        print(f"Classe: {character_class_name}")
        print(f"Pseudo: {self.name}")
        print(f"PV : {self.health}")
        print(f"Attaque : {self.attack}")
        print(f"Arme : {self.weapon}")

    def suffer_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} a été vaincu !")
        else:
            print(f"{self.name} subit {damage} dégâts. PV restants : {self.health}")

    @staticmethod
    def create_character():
        while True:
            try:
                name = input("Entrez le nom du personnage (entre 3 et 25 caractères): ")
                if len(name) < 3 or len(name) > 25:
                    raise ValueError("Le pseudo doit avoir entre 3 et 25 caractères.")
                break
            except ValueError as e:
                print(e)

        classes = ["Warrior", "Knight", "Wizard", "Troll", "Assassin"]
        print("Choisissez une classe:")
        for i, class_name in enumerate(classes, start=1):
            print(f"{i}. {class_name}")

        while True:
            try:
                class_index = int(input("Entrez le numéro de la classe: "))
                if class_index < 1 or class_index > len(classes):
                    raise ValueError("Numéro de classe invalide.")
                break  # Sort de la boucle si le numéro de classe est valide
            except ValueError as e:
                print(e)

        character_class = classes[class_index - 1]

        weapon = input("Entrez l'arme du personnage: ")


        if character_class == "Warrior":
            return Warrior(name, weapon=weapon)
        elif character_class == "Knight":
            return Knight(name, weapon=weapon)
        elif character_class == "Wizard":
            return Wizard(name, weapon=weapon)
        elif character_class == "Troll":
            return Troll(name, weapon=weapon)
        elif character_class == "Assassin":
            return Assassin(name, weapon=weapon)
        else:
            print("Classe de personnage invalide.")
            return None

class Warrior(Character):
    def __init__(self, name, health=100, attack=25, weapon="Epée"):
        super().__init__(name, health, attack, weapon)

    def melee_attack(self, target):
        damage = self.attack * 2
        target.suffer_damage(damage)
        print(f"{self.name} attaque en mêlée {target.name} et inflige {damage} dégâts !")


class Knight(Character):
    def __init__(self, name, health=120, attack=20,weapon="Epee", armor="Shield"):
        super().__init__(name, health, attack, weapon)
        self.armor = armor

    def take_damage(self, damage):
        reduce_damage = damage - self.armor  # Les dégâts subis sont réduits par l'armure
        if reduce_damage < 0:
            reduce_damage = 0
        self.health -= reduce_damage
        print(f"{self.name} encaisse {reduce_damage} points de dégâts grâce à son armure !")


class Wizard(Character):
    def __init__(self, name, health=80, attack=20, weapon="Bâton magique"):
        super().__init__(name, health, attack, weapon)

    def cast_spell(self, target):
        damage = self.attack * 3  # Les magiciens infligent des dégâts triples avec leurs sorts
        target.suffer_damage(damage)
        print(f"{self.name} lance un sort sur {target.name} et lui inflige {damage} dégâts !")


class Troll(Character):
    def __init__(self, name, health=100, attack=50, resistance=15, weapon="Massue"):
        super().__init__(name, health, attack, weapon)
        self.resistance = resistance

    def reduce_damage(self, damage):
        reduce_degat = damage - self.resistance
        if reduce_degat < 0:
            reduce_degat = 0
        self.health -= reduce_degat
        print(f"{self.name} subit {reduce_degat} points de dégâts !")


class Assassin(Character):
    def __init__(self, name, health=75, attack=35, speed=50, weapon="Dague"):
        super().__init__(name, health, attack,weapon)
        self.speed = speed

    def quick_attack(self, target):
        target.health -= self.attack
        print(f"{self.name} attack rapidement {target.name} !")

    def dodge(self):
        print(f"{self.name} esquive habilement l'attaque !")
