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

def evaluationPrix(essaiMessage, message,saisie, boutonProposer):
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
            fenetre.config(bg = "#7adb30") #Couleur verte
            return
        else :
            message["text"] = "Le prix proposé est plus haut que le juste prix.";

        essai +=1;
        afficherEssai(essaiMessage);

        if essai >= maxEssai :
            message["text"] = f"Désolé, vous avez perdu. Le juste prix était : {nombreADeviner}";
            boutonProposer.config(state=DISABLED);
            essaiMessage["text"]= "";
            essaiMessage.config(bg = "#f44336") #Le fond du message est de la même couleur que le background
            sonJeu.stop()
            sonDefaite.play()
            fenetre.config(bg = "#f44336") #Couleur rouge

    except ValueError:
        message["text"] = "Erreur : Veuillez entrer un nombre entier.";

def afficherEssai(essaiMessage) :
    essaiMessage["text"] = f"Essai {essai + 1} sur {maxEssai} : "

def resetJeu(essaiMessage,message,saisie,boutonProposer) :
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

texteBienvenue = Label(fenetre, text="", font=("Arial", 12), justify=CENTER);
texteBienvenue.pack_forget()

def defilementTexte(texte, index=0, texteAffiche="") :
    if index< len(texte) :
        texteAffiche += texte[index];
        texteBienvenue.config(text=texteAffiche);
        fenetre.after(40, defilementTexte, texte, index+1, texteAffiche);
    else:
        texteBienvenue.config(text=texte)


def cacherBouton() :
    boutonFacile.pack_forget()
    boutonNormal.pack_forget()

def modeFacile() :
    global nombreADeviner
    texteTitre.pack_forget()
    cacherBouton()
    nombreADeviner = random.randint(1, 20)
    texteBienvenue.pack(pady=10)
    defilementTexte(""" =======  Bienvenue dans le juste prix !  =======
    Vous avez droit à plusieurs possibilités pour trouver le juste prix.
    Le juste prix est compris entre 1 et 20$
    Après cinq erreurs, c'est terminé.
    Bonne chance à vous !
    """)

    message = Label(fenetre, text="Veuillez entrer une proposition :", font=("Arial", 12));
    message.pack(pady=20);

    essaiMessage = Label(fenetre, text=f"Essai {essai + 1} sur {maxEssai} :", font=("Arial", 12));
    essaiMessage.pack(pady=10);

    saisie = Entry(fenetre, font=("Arial", 14))
    saisie.pack(pady=10);

    boutonProposer = Button(fenetre, text="Proposer", font=("Arial", 12), command=lambda:evaluationPrix(essaiMessage, message, saisie, boutonProposer));
    boutonProposer.pack(pady=10);

    boutonReset = Button(fenetre, text="Réinitialiser la partie", font=("Arial", 12), command=lambda:resetJeu(essaiMessage,message,saisie,boutonProposer));
    boutonReset.pack(pady=10);


texteTitre = Label(fenetre, text= "Le juste prix", font=("Arial", 20))
texteTitre.pack(pady=20)

boutonFacile = Button(fenetre, text="Facile", font=("Arial", 12), command=modeFacile)
boutonFacile.pack(pady=10)

boutonNormal = Button(fenetre, text="Normal", font=("Arial", 12))
boutonNormal.pack(pady=10)



fenetre.mainloop();