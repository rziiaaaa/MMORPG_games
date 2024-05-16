import personnage

def main():
    new_character = personnage.Character.create_character()
    while True:
        print("\nMenu:")
        print("1. Détails personnage")
        print("2. Inventaire")
        print("3. Achat items")
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
                    try:
                        market_choice = int(input("\nChoisissez une option du market place"))
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