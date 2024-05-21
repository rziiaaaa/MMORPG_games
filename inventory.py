import character


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
            for idx, item in enumerate(self.items, start=1):
                print(f"{idx}. {item}")
        else:
            print("L'inventaire est vide.")

    def remove_item_by_index(self, index):
        if 0 <= index < len(self.items):
            item = self.items.pop(index)
            print(f"{item} a été retiré de l'inventaire.")
        else:
            print("Indice invalide pour l'inventaire.")