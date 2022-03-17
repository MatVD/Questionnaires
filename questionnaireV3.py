# Questionnaire version 3 - orientée objet

class Questionnaire:
    def __init__(self, questions):
        self.questions = questions
        
    def lancer_questionnaire(self):
        for question in self.questions:
            question.affichage()


class Question:

    NB_QUESTIONS = 0
    SCORE = 0

    def __init__(self, titre_question, choix_de_reponse, bonne_reponse):
        Question.NB_QUESTIONS += 1
        self.titre_question = titre_question
        self.choix_de_reponse = choix_de_reponse
        self.bonne_reponse = bonne_reponse

    def affichage(self):
        print()
        print(f"Question {Question.SCORE + 1}: {self.titre_question}")
        print(f"{', '.join(self.choix_de_reponse)}")
        self.reponse = input("Votre réponse: ")
        self.gestion_score()

    def gestion_score(self):
        print()
        if self.reponse.lower() == self.bonne_reponse.lower():
            Question.SCORE +=1
            print("Bonne réponse !")
        else: 
            print("Mauvaise réponse !")
        print(f"Votre score est de {Question.SCORE}/{Question.NB_QUESTIONS}")
        print()


liste_questions = [
    Question("Quelle est la capitale de la France? ", ("Nantes", "Lyon", "Paris", "Marseille"), "Paris"),
    Question("Quelle est la capitale de l'Italie? ", ("Turin", "Naples", "Rome", "Venise"), "Rome"),
    Question("Quelle est la capitale de l'Espagne? ", ("Barcelone", "Madrid", "Salou", "Seville"), "Madrid"),
]

questionnaire1 = Questionnaire(liste_questions)
questionnaire1.lancer_questionnaire()


