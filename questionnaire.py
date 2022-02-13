
donnees = {
    "de la France": ("Marseille, Nice, Paris, Nantes", "Paris"),
    "de l'Italie": ("Naples, Rome, Venise, Turin", "Rome"),
    "de l'Angleterre": ("Londre, Liverpool, Oxford, Bristol", "Londre"),
    "du Portugal": ("Lisbonne, Porto, Evora, Braga", "Lisbonne")
} 


def poser_question(pays, villes):
    print()
    print(f"QUESTION : Quelle est la capitale {pays}? ")
    print(villes)
    reponse = input("Votre réponse: ")
    return reponse


def afficher_resultat(reponse, bonne_reponse):
    global score
    print()
    if reponse == bonne_reponse:
        score += 1
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")
    print()



score = 0
nb_iteration = 0 

for key, value in donnees.items():
    reponse = poser_question(key, value[0])
    afficher_resultat(reponse, value[-1])
    nb_iteration += 1
    print(f"Votre score est de {score}/{nb_iteration}")
