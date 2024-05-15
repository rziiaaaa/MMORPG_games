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
            choix = int(input("Choisissez une option : "))
            if choix == 1:
                new_character.view_details()
            elif choix == 2:
                # Boucle pour le menu de l'inventaire
                while True:
                    print("\nInventaire:")
                    new_character.view_inventory()
                    print("\nOptions:")
                    print("1. Supprimer un item")
                    print("2. Retour au menu principal")

                    try:
                        choix_inventaire = int(input("Choisissez une option de l'inventaire : "))
                        if choix_inventaire == 1:
                            # Ajouter la logique pour supprimer un item
                            pass
                        elif choix_inventaire == 2:
                            break  # Sort de la boucle et retourne au menu principal
                        else:
                            print("Option invalide. Veuillez choisir un numéro entre 1 et 2.")
                    except ValueError:
                        print("Veuillez entrer un numéro valide.")
            elif choix == 3:
                # Ajouter la logique pour l'achat d'items
                pass
            elif choix == 4:
                # Ajouter la logique pour le combat
                pass
            elif choix == 5:
                print("Au revoir !")
                break  # Quitte la boucle et termine le programme
            else:
                print("Option invalide. Veuillez choisir un numéro entre 1 et 5.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")
if __name__ == "__main__":
    main()