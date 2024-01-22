#Interface de jeu
import random
from mauvais_choix import *
from Pokemon import Pokemon
from Dresseur import Dresseur
from JcJ import JcJ
from JcE import JcE


class Jeu :
    
    def __init__(self, fichierPokemon, fichierDefense, fichierAttaque, fichierSauv):
        self.fichierPokemon = fichierPokemon
        self.fichierAttaque = fichierAttaque
        self.fichierSauv = fichierSauv
        self.fichierDefense = fichierDefense

    def random_pokemon(self): #Return un pokemon aleatoire du fichier nomfichier
    
        f = open(self.fichierPokemon)
        
        lines = f.read()
        nbline = lines.split("\n") #Pour obtenir le nombre de pokemons dans le fichier
        
        condition = True
        while condition :
            nb = random.randint(1, len(nbline)-2) #1 car la premiere ligne n'est pas un pokÃ©mon
            liste_poke = nbline[nb].split("\t")
            if liste_poke[1]=='': #car sinon il s agit d une evolution d un pokemon
                condition = False
        #print(liste_poke)        
        pok = Pokemon(liste_poke) #par defaut on a un pokemon de niveau 1 avec 0 experience
        
        return pok
    
    #methode qui renvoie un pokemon de niveau choisi par le Dresseur
    def choix_pokemon_difficulte(self):
        print("Veuillez choisir la difficulté du Pokemon que vous voulez combattre:\n"
              "0\ Faible (Pokemon entre Niveau 1 et Niveau 3)\n"
              "1\ Moyen (Pokemon entre Niveau 4 et Niveau 6)\n"
              "2\ Fort (Pokemon entre Niveau 7 et Niveau 10)\n"
              "3\ Aléatoire (Pokemon entre Niveau 1 et Niveau 10)")
        
        choix = input("> ")
        choix = mauvais_choix(choix, 3)
        
        pok = self.random_pokemon()
        
        if choix == 0: #Niveau 1 a 3
            niv = random.randint(0,2)
            for i in range(niv):
                pok.monter_niveau(True)
                
        elif choix == 1: #Niveau 4 a 6
            niv = random.randint(3,5)
            for i in range(0,niv):
                pok.monter_niveau(True)
                
        elif choix == 2: #Niveau 7 a 10
            niv = random.randint(6,9)
            for i in range(0,niv):
                pok.monter_niveau(True)
                
        else: #Niveau 1 à 10
            niv = random.randint(1,9)
            for i in range(niv):
                pok.monter_niveau(True)
        
        return pok
        
    #fonction qui renvoie une liste de 3 pok de niv 1 pour un nouveau Dresseur
    def ListePokemonDepart(self):
        listePok = []
        
        while len(listePok) != 3:
            Pok = self.random_pokemon()
            if Pok not in listePok:
                listePok.append(Pok)
        return listePok
    
    def nouveau_dresseur(self, nom):          
        ListePokemon = self.ListePokemonDepart()
        D = Dresseur(nom, ListePokemon)
        return D
        
    def ancien_dresseur(self, nom):
        listePokemons = []          
        fichier_dresseur = "Sauvegarde\Dresseur_" + nom + ".txt"
        with open(fichier_dresseur) as f :
            lines = f.read()
            nbline = lines.split("\n")        
            liste_info_pok = []
            for l in range(0, len(nbline)) :  
                liste_info_pok.append(nbline[l].split("\t"))    
        with  open("pokemon.txt") as f : #self.fichierPokemon       
            lines = f.read()
            nbline = lines.split("\n") 
            for info_pok in liste_info_pok :               
                for l in range(0, len(nbline)) :
                    pokemon = nbline[l].split("\t")
                    if pokemon[0] == info_pok[0] :
                        Pokemon_sauv = Pokemon(pokemon)
                        Pokemon_sauv.addFromSave(info_pok[1], info_pok[2], info_pok[3], info_pok[4], info_pok[5], info_pok[6])
                        listePokemons.append(Pokemon_sauv)
                        break
        return Dresseur(nom, listePokemons)
    
    #fonction qui recupere les infos (pokemon ou competence) a partir du nom
    def Recuperation(nom, nomfichier): 
        #Ouverture du fichier contenant les informations de la competence        
        f = open(nomfichier)       
        lines = f.read()
        nbline = lines.split("\n") 
        #Recherche de la competence dans le fichier texte
        i = 1
        liste = nbline[i].split("\t")
        i+=1    
        while (liste[0] != nom):
            liste = nbline[i].split("\t")
            i += 1 
        return liste

    def sauvegarde(self, dresseur):
        #Vérifier que le dresseur à ce nom n'est pas déjà enregistré
        #Si oui, proposez d'écraser l'ancienne sauvegarde pour mettre la nouvelle
        fichier_sauvegarde_dresseur = "Sauvegarde\Dresseur_" + dresseur._Dresseur__Nom + ".txt"
        with open(self.fichierSauv, 'r') as f :
            lines = f.read()
            nbline = lines.split("\n")
            save = True
            deja_inscrit = False
            for l in nbline:
                #Dresseur déjà sauvegardé
                if dresseur._Dresseur__Nom == l : 
                    print(dresseur._Dresseur__Nom,end='')
                    print(", un dresseur est déjà enregistré sous ce nom. Nous ne pouvons pas enregistrer votre dresseur. Voulez vous écraser sa sauvegarde ?\n")
                    choix = input("Veuillez répondre par oui ou non. > ")
                    choix = mauvais_choix_oui(choix)
                    deja_inscrit = True
                    if choix == "Non":
                        print("Dans ce cas, nous ne pouvons pas enregistrer votre dresseur.\n")
                        save = False
                    break
        with open(self.fichierSauv, 'a') as f :
            if save and not(deja_inscrit): 
                f.write('\n' + dresseur._Dresseur__Nom)      
        if save :
            with open(fichier_sauvegarde_dresseur, 'w') as f :    
                for pok in dresseur._Dresseur__listePokemons :
                    info_pok = pok._Pokemon__Nom + "\t" + str(pok._Pokemon__Niveau) + "\t" + str(pok._Pokemon__Exp)  + "\t" + str(pok._Pokemon__VieMax)  + "\t" + str(pok._Pokemon__EnergieMax)  + "\t" + str(pok._Pokemon__Regeneration)  + "\t" + str(pok._Pokemon__Resistance) 
                    f.write(info_pok + "\n")          
            print(dresseur._Dresseur__Nom + ", votre dresseur a bien été enregistré")
          
    def initialisation(self, nom):  
        # Vérifier si le dresseur est enregistré
        dresseur_trouvee = False
        with open(self.fichierSauv, 'r') as f :
            lines = f.read()
            nbline = lines.split("\n")  
        for n in range(0, len(nbline)) : 
            if nom == nbline[n]:
                print("Nous avons trouvé un dresseur déjà enregistré à ce nom :\n")
                dresseur = self.ancien_dresseur(nom)
                print(dresseur)
                choix = input("Est-ce bien vous ? Veuillez répondre par oui ou non. > ")
                choix = mauvais_choix_oui(choix)
                if (choix == "Oui") :
                    dresseur_trouvee = True
                    break
                       
        #Si non enregistré : proposition de récupérer une ancienne sauvegarde ou creer un nouveau dresseur
        if not(dresseur_trouvee):
            print("\nVoici la liste des dresseurs enregistrés : \n")
            #Options : 
            for n in range(0, len(nbline)) : 
                print(str(n) + "\ " + nbline[n])
            print(str(len(nbline)) + "\ Créer un nouveau dresseur" )
            #Ajouter une option de retour
            #Choix du joueur :
            choix = input("Avec quel dresseur voulez-vous jouer ? > ")
            choix = mauvais_choix(choix, len(nbline))
            print("\n")
            #Application du choix :
            if choix == len(nbline) :
                #Il existe déjà un dresseur à ce nom, vous risquez d'écraser sa sauvegarde, voulez vous continuer ?
                dresseur = self.nouveau_dresseur(nom)
                print(dresseur)
            else :  
                dresseur = self.ancien_dresseur(nbline[choix])
                print(dresseur) 
                
        return dresseur
        
    def Jouer (self) :
        
        #Message d'accueil
        print("----------------------------------\n")
        print("     Bienvenue dans POOkemon !    \n")
        print("----------------------------------")
        
        #INITIALISATION
        nom = input("Quel est votre nom ? > ")
        print("Bonjour, " + nom + ",")
        liste_dresseur = []
        
        Dresseur1 = self.initialisation(nom)

        #CHOIX ACTIVITE
        envie_jouer = True
        while envie_jouer :

            #Options :
            print("\n\nQue voulez vous faire ?\n"
                  "0\ Mode multijoueur local : Combat contre un autre dresseur\n" #Combat JcJ
                  "1\ Combatte/Capturer des pokemons\n"
                  "2\ Changer de deck\n"
                  "3\ Changer de dresseur\n"
                  "4\ Quitter le jeu") #Combat JcE
            
            #Choix du joueur :
            choix = input("Veuillez faire un choix : > ")
            choix = mauvais_choix(choix, 4)
            print("\n")
            
            #Application du choix :
            if (choix==0) : #Combat contre un autre dresseur
                # #Choix du deuxième joueur
                print("Deuxième joueur, à vous de faire votre choix :")
                if liste_dresseur == []:
                    print("Vous n'avez pas d'autres dresseurs disponibles !")
                    Nom = input("Quel est le nom du dresseur que vous voulez combattre ? > ")
                    Dresseur2 = self.initialisation(Nom)
                    liste_dresseur.append(Dresseur2)
                    print("\n")
                else : 
                    for d in range(len(liste_dresseur)):
                        print(str(d) + '\ ' + liste_dresseur[d]._Dresseur__Nom)
                    print(str(len(liste_dresseur)) + '\ ' + 'Créer un nouveau dresseur' )
                    choix = input("Quel dresseur voulez vous jouer ? > ")
                    choix = mauvais_choix(choix, len(liste_dresseur))
                    print('\n')
                    if choix == len(liste_dresseur):
                        nom = input("Très bien. Créons un nouveau dresseur. Quel sera son nom ? > ")
                        Dresseur2 = self.nouveau_dresseur(nom)
                        liste_dresseur.append(Dresseur2)
                    else :
                        Dresseur2 = liste_dresseur[choix]
                    
                print(Dresseur2._Dresseur__Nom + " VS " + Dresseur1._Dresseur__Nom)
                print("Que le combat commence\n")
                combat = JcJ(Dresseur1, Dresseur2)
                combat.jouer() 

            elif (choix == 1) : #Combatte/Capturer des pokemons   
                print("Nous allons partir à la chasse aux pokémons !\n")                           
                pokemon_IA = self.choix_pokemon_difficulte()
                print("Vous allez vous battre contre " + pokemon_IA._Pokemon__Nom)
                print(pokemon_IA)
                print("\nBonne chance à vous\n")
                combat = JcE(Dresseur1, pokemon_IA)
                combat.jouer()  
                
            elif (choix == 2) : #Changer de deck           
                Dresseur1.changer_deck()
                
                
            elif (choix == 3) : #Changer de dresseur
                                
                if liste_dresseur != []: 
                    print("\nVoici les dresseurs actuellement disponibles en jeu :\n")
                    for d in range(len(liste_dresseur)) :
                        print(str(d) + "\ " + liste_dresseur[d]._Dresseur__Nom)
                    print(str(len(liste_dresseur)) + "\ " + "Initialiser un nouveau dresseur")
                    choix = input("Que choississez vous ? > ")
                    choix = mauvais_choix(choix, (len(liste_dresseur)-1))
                    
                    if (choix == len(liste_dresseur)):
                        #variable booleenne qui sert à verifier si on veut initialiser un nouveau dresseur ou pas
                        initialisation = True 
                    else :
                        print("\nVous avez choisi : ")
                        print(liste_dresseur[choix])
                        dresseur = liste_dresseur[choix]
                        liste_dresseur.remove(liste_dresseur[choix])
                        if Dresseur1 not in liste_dresseur :
                            liste_dresseur.append(Dresseur1)  
                        Dresseur1 = dresseur
                        initialisation = False
                else :
                    initialisation = True
                    
                if initialisation == True :
                    nom = input("Quel est le nom de votre nouveau dresseur ? > ")
                    dresseur = self.initialisation(nom)
                    liste_dresseur.append(Dresseur1)
                    if dresseur in liste_dresseur :
                        liste_dresseur.remove(dresseur)
                    Dresseur1 = dresseur
                
            elif (choix == 4) : #Quitter le jeu
                print("\nVoulez vous sauvegarder tous les dresseurs avant de quitter ?")
                choix = input("Veuillez répondre par oui ou non > ")
                choix = mauvais_choix_oui(choix)
                if choix == "Oui":
                    for dresseur in liste_dresseur :
                        self.sauvegarde(dresseur)
                    self.sauvegarde(Dresseur1)
                        
                print("\nMerci d'avoir joué !")
                print("A une prochaine fois !")
                envie_jouer = False
                       
         