from market import Market
import character

def main():
    new_character = character.Character.create_character()
    market = Market()

    while True:
        print("\nMenu:")
        print("1. Détails personnage")
        print("2. Inventaire")
        print("3. Market Place")
        print("4. Combat")
        print("5. Quitter")

        try:
            choice = int(input("Choisissez une option : "))
            if choice == 1:
                new_character.view_details()
            elif choice == 2:
                while True:
                    print("\nInventaire:")
                    new_character.view_inventory()
                    print("\nOptions:")
                    print("1. Supprimer un item")
                    print("2. Retour au menu principal")

                    try:
                        inventory_choice = int(input("Choisissez une option de l'inventaire : "))
                        if inventory_choice == 1:
                            item_idx = int(input("Entrez l'indice de l'item à supprimer : ")) - 1
                            new_character.inventory.remove_item_by_index(item_idx)
                        elif inventory_choice == 2:
                            break
                        else:
                            print("Option invalide. Veuillez choisir un numéro entre 1 et 2.")
                    except ValueError:
                        print("Veuillez entrer un numéro valide.")
            elif choice == 3:
                while True:
                    print("\nMarket Place:")
                    print("\nOptions:")
                    print("1. Acheter un item")
                    print("2. Vendre un item")
                    print("3. Retour au menu principal")
                    try:
                        market_choice = int(input("\nChoisissez une option du market place : "))
                        if market_choice == 1:
                            print("\nCatégories disponibles:")
                            for idx, category in enumerate(market.categories.keys(), start=1):
                                print(f"{idx}. {category}")
                            category_idx = int(input("Entrez l'indice de la catégorie : ")) - 1
                            category_keys = list(market.categories.keys())
                            if 0 <= category_idx < len(category_keys):
                                category = category_keys[category_idx]
                                print(f"\nItems disponibles dans {category}:")
                                market.view_items_in_category(category)
                                item_idx = int(input("Entrez le numéro de l'item à acheter : ")) - 1
                                item = market.buy(category_idx, item_idx, new_character.inventory)
                        elif market_choice == 2:
                            print("\nVotre Inventaire:")
                            for idx, category in enumerate(market.categories.keys(), start=1):
                                print(f"{idx}. {category}")
                            category_idx = int(input("Entrez l'indice de la catégorie où vendre l'item : ")) - 1
                            new_character.view_inventory()
                            item_idx = int(input("Entrez l'indice de l'item à vendre : ")) - 1
                            market.sell(category_idx, item_idx, new_character.inventory)
                        elif market_choice == 3:
                            break
                    except ValueError:
                        print("Veuillez entrer un numéro valide.")
            elif choice == 4:
                pass
            elif choice == 5:
                print("Au revoir !")
                break
            else:
                print("Option invalide. Veuillez choisir un numéro entre 1 et 5.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")

if __name__ == "__main__":
    main()
