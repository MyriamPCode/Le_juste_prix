import random
from tkinter import *

nombreADeviner = random.randint(1, 20);

#Création d'une fenêtre d'affichage
fenetre = Tk();
fenetre.title("Le juste prix !");
fenetre.config(bg = "#87CEEB") # Couleur bleue
fenetre.mainloop();

def propositionUne() :
    try:
        premierNombre = int(input("Veuillez entrer une première proposition : "));
        return premierNombre;
    except ValueError :
        print("Erreur : Le prix proposé doit être un nombre entier. ");
        int(input("Veuillez entrer une première proposition : "));
        return propositionUne();

def propositionDeux() :
    try:
        deuxiemeNombre = int(input("Veuillez entrer une deuxième proposition : "));
        return deuxiemeNombre;
    except ValueError :
        print("Erreur : Le prix proposé doit être un nombre entier. ");
        int(input("Veuillez entrer une deuxième proposition : "));
        return propositionDeux();

def propositionTrois() :
    try:
        troisiemeNombre = int(input("Veuillez entrer une troisième proposition : "));
        return troisiemeNombre;
    except ValueError :
        print("Erreur : Le prix proposé doit être un nombre entier. ");
        int(input("Veuillez entrer une troisième proposition : "));
        return propositionTrois();

def propositionQuatre() :
    try:
        quatriemeNombre = int(input("Veuillez entrer une quatrième proposition : "));
        return quatriemeNombre;
    except ValueError :
        print("Erreur : Le prix proposé doit être un nombre entier. ");
        int(input("Veuillez entrer une quatrième proposition : "));
        return propositionQuatre();

def propositionFinale() :
    try:
        dernierNombre = int(input("Veuillez entrer une dernière proposition : "));
        return dernierNombre;
    except ValueError :
        print("Erreur : Le prix proposé doit être un nombre entier. ");
        int(input("Veuillez entrer une dernière proposition : "));
        return propositionFinale();

def evaluationPrix(nombre) :
    if nombre < nombreADeviner :
        print("Le prix proposé est plus bas que le juste prix !");
    elif nombre == nombreADeviner :
        print("Félicitations ! Vous venez de remporter le juste prix !");
        return True;
    else :
        print("Le prix proposé est plus haut que le juste prix ! ");
        return False;

def deroulementJeu() :
    essai = 0;
    maxEssai = 5;

    while essai < maxEssai :
        print(f"Essai {essai +1} sur {maxEssai} :")
        if essai == 0:
            proposition = propositionUne();
        elif essai == 1 :
            proposition = propositionDeux();
        elif essai == 2 :
            proposition = propositionTrois();
        elif essai == 3 :
            proposition = propositionQuatre();
        else :
            proposition = propositionFinale();

        if evaluationPrix(proposition):
            break;

        essai += 1;

        if essai == maxEssai and proposition != nombreADeviner :
            print(f"""Désolé, vous avez perdu. Le juste prix était : {nombreADeviner} !
            Merci d'avoir joué !
            À bientôt !
            """);

if __name__ == "__main__":
    print(""" =======  Bienvenue dans le juste prix !  =======
    Vous avez droit à plusieurs possibilités pour trouver le juste prix.
    Après cinq erreurs, c'est terminé.
    Bonne chance à vous !
    """);
    deroulementJeu();