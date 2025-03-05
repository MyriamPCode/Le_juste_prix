import random
from tkinter import *
import pygame   # Pour jouer des sons

pygame.mixer.init()

sonVictoire = pygame.mixer.Sound('victoire.wav')
nombreADeviner = random.randint(1, 20);

#Création d'une fenêtre d'affichage
fenetre = Tk();
fenetre.title("Le juste prix !");
fenetre.config(bg = "#87CEEB") # Couleur bleue
fenetre.geometry("640x480");

essai = 0;
maxEssai = 5;
propositions =[];

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

#def evaluationPrix(nombre) :
    #if nombre < nombreADeviner :
        #print("Le prix proposé est plus bas que le juste prix !");
    #elif nombre == nombreADeviner :
        #print("Félicitations ! Vous venez de remporter le juste prix !");
        #return True;
    #else :
        #print("Le prix proposé est plus haut que le juste prix ! ");
        #return False;

def evaluationPrix():
    global essai;
    try:
        proposition = int(saisie.get());
        propositions.append(proposition);

        if proposition < nombreADeviner :
            message["text"] = "Le prix proposé est plus bas que le juste prix.";
        elif proposition == nombreADeviner :
            message["text"] = "Félicitations ! Vous avez trouvé le juste prix !";
            boutonProposer.config(state=DISABLED); #Le bouton Proposer n'est plus désactivé
            sonVictoire.play()
            return
        else :
            message["text"] = "Le prix proposé est plus haut que le juste prix.";

        essai +=1;
        afficherEssai();

        if essai >= maxEssai :
            message["text"] = f"Désolé, vous avez perdu. Le juste prix était {nombreADeviner} : ";
            boutonProposer.config(state=DISABLED);
            essaiMessage["text"]= "";
            essaiMessage.config(bg = "#87CEEB") #Le fond du message est de la même couleur que le background

    except ValueError:
        message["text"] = "Erreur : Veuillez entrer un nombre entier.";

def afficherEssai() :
    essaiMessage["text"] = f"Essai {essai + 1} sur {maxEssai} : "

def resetJeu() :
    global essai, nombreADeviner, propositions;
    essai = 0;
    propositions = [];
    nombreADeviner = random.randint(1, 20);
    message["text"] = "Veuillez entrer une proposition :";
    saisie.delete(0, END);
    boutonProposer.config(state=NORMAL);
    essaiMessage["text"]= f"Essai {essai + 1} sur {maxEssai}";

def defilementTexte(texte, index=0, texteAffiche="") :
    if index< len(texte) :
        texteAffiche += texte[index];
        texteBienvenue.config(text=texteAffiche);
        fenetre.after(100, defilementTexte, texte, index+1, texteAffiche);



"""def deroulementJeu() :
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
"""
        #if essai == maxEssai and proposition != nombreADeviner :
            #print(f"""Désolé, vous avez perdu. Le juste prix était : {nombreADeviner} !
            #Merci d'avoir joué !
            #À bientôt !
            #""");"""



#if __name__ == "__main__":
    #print(""" =======  Bienvenue dans le juste prix !  =======
    #Vous avez droit à plusieurs possibilités pour trouver le juste prix.
    #Après cinq erreurs, c'est terminé.
    #Bonne chance à vous !
    #""");
    #deroulementJeu();


texteBienvenue = Label(fenetre, text ="", font=("Arial",12), justify=CENTER);
texteBienvenue.pack(pady=10);

defilementTexte(""" =======  Bienvenue dans le juste prix !  =======
    Vous avez droit à plusieurs possibilités pour trouver le juste prix.
    Après cinq erreurs, c'est terminé.
    Bonne chance à vous !
    """);

message = Label(fenetre, text="Veuillez entrer une proposition :", font=("Arial", 12));
message.pack(pady=20);

essaiMessage = Label(fenetre, text =f"Essai {essai + 1} sur {maxEssai} :", font=("Arial", 12));
essaiMessage.pack(pady=10);

saisie=Entry(fenetre, font=("Arial", 14))
saisie.pack(pady=10);

boutonProposer = Button(fenetre, text="Proposer", font=("Arial", 12), command=evaluationPrix);
boutonProposer.pack(pady=10);

boutonReset = Button(fenetre , text="Réinitialiser la partie", font=("Arial", 12), command=resetJeu);
boutonReset.pack(pady=10);

fenetre.mainloop();