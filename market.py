class Market:
    def __init__(self):
        self.categories = {
            "Armes": ["Epée", "Arc", "Hache", "Lance", "Masse", "Baguette magique", "Kunai"],
            "Armures": ["Armure légère", "Armure lourde", "Bouclier", "Plastron", "Jambière", "Sac à dos"],
            "Potions": ["Potion de santé", "Potion de force", "Potion de vitesse"]
        }

    def view_stock(self):
        for category in self.categories:
            print(f"\n{category}:")
            for idx, item in enumerate(self.categories[category], start=1):
                print(f"{idx}. {item}")

    def view_items_in_category(self, category):
        if category in self.categories:
            for idx, item in enumerate(self.categories[category], start=1):
                print(f"{idx}. {item}")
        else:
            print(f"La catégorie '{category}' n'existe pas.")

    def buy(self, category_idx, item_idx, character_inventory):
        category_keys = list(self.categories.keys())
        if 0 <= category_idx < len(category_keys):
            category = category_keys[category_idx]
            if 0 <= item_idx < len(self.categories[category]):
                item = self.categories[category].pop(item_idx)
                character_inventory.add_item(item)
                print(f"{item} acheté avec succès !")
                return item
            else:
                print("Indice d'item invalide.")
        else:
            print("Indice de catégorie invalide.")
        return None

    def sell(self, category_idx, item_idx, character_inventory):
        if 0 <= item_idx < len(character_inventory.items):
            item = character_inventory.items[item_idx]
            category_keys = list(self.categories.keys())
            if 0 <= category_idx < len(category_keys):
                category = category_keys[category_idx]
                character_inventory.remove_item_by_index(item_idx)
                self.categories[category].append(item)
            else:
                print(f"Indice de catégorie invalide.")
        else:
            print(f"Indice invalide dans votre inventaire.")