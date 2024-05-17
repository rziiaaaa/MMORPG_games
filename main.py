from market import Market

import personnage


def main():
    new_character = personnage.Character.create_character()
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
                            new_character.remove_item_from_inventory()
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
                            market.view_categories()
                            try:
                                category_idx = int(input("Choisissez une catégorie par son numéro : "))
                                category = list(market.categories.keys())[category_idx - 1]
                                market.view_items_in_category(category)
                                item_idx = int(input("Entrez le numéro de l'item à acheter : "))
                                market.buy(category, item_idx, new_character.inventory)
                            except ValueError:
                                print("Veuillez entrer un numéro valide.")
                        elif market_choice == 2:
                            print("\nVotre Inventaire:")
                            new_character.view_inventory()
                            item_name = input("Entrez le numéro de l'item à vendre : ")
                            market.sell(item_name, new_character.inventory)
                        elif market_choice == 3:
                            break
                        else:
                            print("Option invalide. Veuillez choisir un chiffre entre 1 et 3.")
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
