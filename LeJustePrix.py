import random
from tkinter import *
import pygame   # Pour jouer des sons

pygame.mixer.init()

sonVictoire = pygame.mixer.Sound('victory.wav')
sonJeu = pygame.mixer.Sound('we_remain_united.mp3')
sonDefaite = pygame.mixer.Sound('game_over.wav')

sonJeu.set_volume(0.5)

nombreADeviner = random.randint(1, 20);

#Création d'une fenêtre d'affichage
fenetre = Tk();
fenetre.title("Le juste prix !");
fenetre.config(bg = "#87CEEB") # Couleur bleue
fenetre.geometry("640x480");
sonJeu.play()

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
            sonJeu.stop()
            fenetre.config(bg = "#7adb30")
            return
        else :
            message["text"] = "Le prix proposé est plus haut que le juste prix.";

        essai +=1;
        afficherEssai();

        if essai >= maxEssai :
            message["text"] = f"Désolé, vous avez perdu. Le juste prix était : {nombreADeviner}";
            boutonProposer.config(state=DISABLED);
            essaiMessage["text"]= "";
            essaiMessage.config(bg = "#f44336") #Le fond du message est de la même couleur que le background
            sonJeu.stop()
            sonDefaite.play()
            fenetre.config(bg = "#f44336")

    except ValueError:
        message["text"] = "Erreur : Veuillez entrer un nombre entier.";

def afficherEssai() :
    essaiMessage["text"] = f"Essai {essai + 1} sur {maxEssai} : "

def resetJeu() :
    global essai, nombreADeviner, propositions;
    essai = 0;
    propositions = [];
    nombreADeviner = random.randint(1, 20);
    fenetre.config(bg="#87CEEB")
    essaiMessage.config(bg="white")
    message["text"] = "Veuillez entrer une proposition :";
    saisie.delete(0, END);
    boutonProposer.config(state=NORMAL);
    essaiMessage["text"]= f"Essai {essai + 1} sur {maxEssai}";
    sonJeu.play()
    sonDefaite.stop()
    sonVictoire.stop()

def defilementTexte(texte, index=0, texteAffiche="") :
    if index< len(texte) :
        texteAffiche += texte[index];
        texteBienvenue.config(text=texteAffiche);
        fenetre.after(100, defilementTexte, texte, index+1, texteAffiche);


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