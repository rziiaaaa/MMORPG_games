class Market:
    def __init__(self):
        self.categories = {
            "Armes": ["Epée", "Arc", "Hache", "Lance"],
            "Armures": ["Armure légère", "Armure lourde", "Bouclier"],
            "Potions": ["Potion de santé", "Potion de force", "Potion de vitesse"]
        }

    def view_categories(self):
        print("Catégories disponibles :")
        for category in self.categories:
            print(f"- {category}")

    def view_items_in_category(self, category):
        if category in self.categories:
            print(f"Articles dans la catégorie '{category}' :")
            for item in self.categories[category]:
                print(item)
        else:
            print(f"La catégorie '{category}' n'existe pas.")

    def buy(self, category, item, character_inventory):
        if category in self.categories:
            if item in self.categories[category]:
                character_inventory.add_item(item)
                print(f"{item} a été ajouté à votre inventaire.")
                self.categories[category].remove(item)
            else:
                print(f"{item} n'est pas disponible dans la catégorie '{category}'.")
        else:
            print(f"La catégorie '{category}' n'existe pas.")

    def sell(self, item, character_inventory):
        pass