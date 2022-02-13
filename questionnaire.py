
# Projet questionnaire : un petit jeu de question 
# objectif : trouver la capitale des pays 


# les données du questionnaire : Le pays, les villes et la bonne réponse
donnees = {
    "de la France": ["Marseille", "Nice", "Paris", "Nantes", "Paris"],
    "de l'Italie": ["Naples", "Rome", "Venise", "Turin", "Rome"],
    "de l'Angleterre": ["Londre", "Liverpool", "Oxford", "Bristol", "Londre"],
    "du Portugal": ["Lisbonne", "Porto", "Evora", "Braga", "Lisbonne"]
} 


# définition de la fonction qui affiche la question et les réponses
def poser_question(pays, villes):
    print()
    print(f"QUESTION {nb_iteration + 1}: Quelle est la capitale {pays}? ")
    print(*villes)
    reponse = input("Votre réponse: ")
    reponse = gestion_erreurs(values[0:4], reponse)
    return reponse
    

def gestion_erreurs(villes, reponse):
    # erreurs possible : 
    #   - l'utilisateur rentre une ville qui n'est pas proposé
    for i in range(len(villes)):
        villes[i] = villes[i].lower()

    if reponse.lower() not in villes:
        print
        print("Erreur: il faut choisir une des villes proposée")
        return poser_question(keys, values[0:4])
    else:
        return reponse


# définition de la fonction qui affiche si c'est une bonne ou mauvaise réponse
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



        
    


score = 0
nb_iteration = 0 

# une boucle sur le dictionnaires 'donnees'
for keys, values in donnees.items():
    reponse = poser_question(keys, values[0:4])
    afficher_resultat(reponse, values[-1])
    nb_iteration += 1
    print(f"Votre score est de {score}/{nb_iteration}")

