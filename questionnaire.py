# Projet questionnaire : un petit jeu de question 
# objectif : trouver la capitale des pays 


# ============ données du questionnaire =============
donnees = {
    "de la France": ["Marseille", "Nice", "Paris", "Nantes", "Paris"],
    "de l'Italie": ["Naples", "Rome", "Venise", "Turin", "Rome"],
    "de l'Angleterre": ["Londre", "Liverpool", "Oxford", "Bristol", "Londre"],
    "du Portugal": ["Lisbonne", "Porto", "Evora", "Braga", "Lisbonne"]
} 


# =========== affiche la question et les réponses ===========
def poser_question(pays, villes):
    print()
    print(f"QUESTION: Quelle est la capitale {pays}? ")
    print(*villes)
    reponse = input("Votre réponse: ")
    reponse = gestion_erreurs(villes, reponse)
    return reponse
    

# =========== fonction pour la gestion des erreurs ===========
def gestion_erreurs(villes, reponse):
    # erreurs possible : 
    #   - l'utilisateur rentre une ville qui n'est pas proposé
    #   - l'utilisateur rentre un nombre
    for i in range(len(villes)):
        villes[i] = villes[i].lower()
    print()
    if reponse.lower() not in villes:
        print("Erreur: il faut choisir une des villes proposée")
        return poser_question(keys, values[0:4])
    else:
        return reponse


# =========== affiche bonne ou mauvaise réponse =============
# elle gère également le l'itération du score
def afficher_resultat(reponse, bonne_reponse):
    global score
    print()
    if reponse.lower() == bonne_reponse.lower():
        score += 1
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")
    print()

    
score = 0 # variable qui alimentera 'score'
nb_iteration = 0 # variable qui alimentera 'nb_iteration'

# ======== boucle sur le dictionnaires 'donnees' ========
# ========== appel des différentes fonctions ============
for keys, values in donnees.items():
    reponse = poser_question(keys, values[0:4])
    afficher_resultat(reponse, values[-1])
    nb_iteration += 1
    print(f"Votre score est de {score}/{nb_iteration}")

