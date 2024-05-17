class Market:
    def __init__(self):
        self.categories = {
            "Armes": ["Epée", "Arc", "Hache", "Lance", "Masse", "Baguette magique", "Kunai"],
            "Armures": ["Armure légère", "Armure lourde", "Bouclier", "Plastron", "Jambière", "Sac à dos"],
            "Potions": ["Potion de santé", "Potion de force", "Potion de vitesse"]
        }

    def view_categories(self):
        print("Catégories disponibles :")
        for idx, category in enumerate(self.categories.keys(), start=1):
            print(f"{idx}. {category}")

    def view_items_in_category(self, category):
        if category in self.categories:
            print(f"Articles dans la catégorie '{category}' :")
            for idx, item in enumerate(self.categories[category], start=1):
                print(f"{idx}. {item}")
        else:
            print(f"La catégorie '{category}' n'existe pas.")

    def buy(self, category, item_idx, character_inventory):
        if category in self.categories:
            if 0 < item_idx <= len(self.categories[category]):
                item = self.categories[category].pop(item_idx - 1)
                character_inventory.add_item(item)
            else:
                print(f"Indice invalide pour la catégorie '{category}'.")
        else:
            print(f"La catégorie '{category}' n'existe pas.")

    def sell(self, item_name, character_inventory):
        if item_name in character_inventory.items:
            for category in self.categories.values():
                if item_name in category:
                    character_inventory.remove_item_by_name(item_name)
                    category.append(item_name)
                    print(f"{item_name} vendu avec succès !")
                    return
            print(f"Impossible de vendre {item_name}. Catégorie non trouvée.")
        else:
            print(f"{item_name} n'est pas dans votre inventaire.")