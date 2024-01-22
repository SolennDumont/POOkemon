from Combat import Combat
from mauvais_choix import *
from Attaque import Attaque

class JcJ(Combat):
    
    def __init__(self, Dresseur1, Dresseur2):
        super().__init__(Dresseur1)
        self.Dresseur2 = Dresseur2
  
    # fDresseur : dresseur qui a declarer forfait 
    # gDresseur : adverssaire qui a gagne par defaut
    def declarer_forfait(self, fDresseur, gDresseur):
        print(fDresseur._Dresseur__Nom + " a declarer forfait")
        print(gDresseur._Dresseur__Nom + " a gagne le combat!")
    
    #Retourne int exp gagne par un pokemon
    #pDresseur : dresseur vaincu lors du combat 
    #pokemon : le pokemon du dresseur gagnant qui gagne de l'experience
    def gagner_experience(self,pDresseur,pokemon):
        
        #niveau moyen des Pokemons vaincus
        moyPvaincu = (pDresseur._Dresseur__deck[0]._Pokemon__Niveau + pDresseur._Dresseur__deck[1]._Pokemon__Niveau + pDresseur._Dresseur__deck[2]._Pokemon__Niveau)/3
        moyPvaincu = int (moyPvaincu)
        
        #niveau du Pokemon
        niv = pokemon._Pokemon__Niveau
        
        #experiences acquises par le pokemon
        exp = 10 + moyPvaincu - niv
        return exp
        
    def jouer(self):
        condition = True #condition pour jouer; si True on est dans la partie, si False: Partie terminee
        tour = 0 #Compteur nbr de Tour de jeu
        perdant = ""
        gagnant = ""
        
        #reinitialiser Vie et Energie de tous les Pokemons du deck de chaque Dresseur a leur max avant combat
        for pok in self.Dresseur1._Dresseur__deck:
            pok.reinitialisation()
        for pok in self.Dresseur2._Dresseur__deck:
            pok.reinitialisation()
        
        #Chaque Dresseur choisi un pokemon actif parmis son deck
        #Choix du pokemon actif Dresseur1
        
        print(self.Dresseur1)
        choix = input("Quel pokemon voulez vous utiliser? (0-2) > ")
        choix = mauvais_choix(choix, 2)
        D1_PokemonActif = self.Dresseur1._Dresseur__deck[choix] #pokemon actif Dresseur1
        print("\n")
        
        #Choix du pokemon actif Dresseur2
        print(self.Dresseur2)
        choix = input( "Quel pokemon voulez vous utiliser? (0-2) > ")
        choix = mauvais_choix(choix, 2)
        D2_PokemonActif = self.Dresseur2._Dresseur__deck[choix] #Pokemon actif Dresseur2
        print("\n")

        #liste des pokemons qui peuvent encore etre utilisee lors de la partie hormis le pokemon actif
        # si = liste vide, partie terminee*
        D1_Pokemon = []
        D2_Pokemon = []
        for pok in self.Dresseur1._Dresseur__deck:
            D1_Pokemon.append(pok)
        for pok in self.Dresseur2._Dresseur__deck:
            D2_Pokemon.append(pok)
        D1_Pokemon.remove(D1_PokemonActif)
        D2_Pokemon.remove(D2_PokemonActif)
          
        while condition:
            tour += 1
            
            print("-------------\n")
            print("Tour " + str(tour))
            print("\n")
            
            # Au debut de chaque tour, chaque pokemon actif voit son energie regenerer de la valeur regeneration propre a chaque pokemon
            D1_PokemonActif.ajout_energie(D1_PokemonActif._Pokemon__Regeneration)
            D2_PokemonActif.ajout_energie(D2_PokemonActif._Pokemon__Regeneration)
            
            #TOUR DU PREMIER DRESSEUR
            print(self.Dresseur1._Dresseur__Nom +  " c'est a  vous de jouer! \n")
            print("0/ Utiliser une competence")
            print("1/ Remplacer votre Pokemon")
            print("2/ Declarer forfait")
            choix = input("Que voulez-vous faire ? > ")
            choix = mauvais_choix(choix, 2)
            print("\n")
            
            
            if choix == 0: #utiliser competence
                self.utiliser_competence(D1_PokemonActif,D2_PokemonActif)
                print(D1_PokemonActif)
                print("\n")
                print(D2_PokemonActif)
                print("\n")
                #on verifie si le pokemon adverse est mis KO par l attaque
                if D2_PokemonActif._Pokemon__Vie == 0:
                    print(D2_PokemonActif._Pokemon__Nom + " est KO !")
                    if D2_Pokemon!= []: #changement du pokemon actif du Dresseur2 par defaut
                        D2_PokemonActif = D2_Pokemon[0]
                        D2_Pokemon.remove(D2_PokemonActif)
                        print(self.Dresseur2._Dresseur__Nom + ", par defaut votre nouveau Pokemon actif est: ")
                        print(D2_PokemonActif)
                    else: #dresseur 2 a perdu le combat s il n a plus de pokemon dispo
                        print(self.Dresseur2._Dresseur__Nom + ", tous vos Pokemons sont KO.")
                        print(self.Dresseur1._Dresseur__Nom + " a gagne le combat!")
                        condition = False
                        perdant = self.Dresseur2
                        gagnant = self.Dresseur1
                        break
                    
            elif choix == 1: #remplacer pokemon actif
                D1_PokemonActif = self.remplacer_pokemon(D1_Pokemon, D1_PokemonActif)
                print(self.Dresseur1._Dresseur__Nom + ", votre nouveau Pokemon actif est:")
                print(D1_PokemonActif)
            elif choix == 2: #forfait
                self.declarer_forfait(self.Dresseur1, self.Dresseur2)
                condition = False #fin de la partie
                perdant = self.Dresseur1
                gagnant = self.Dresseur2
                break
                
            
            #TOUR DU DEUXIEME DRESSEUR    
            print(self.Dresseur2._Dresseur__Nom +  " c'est a  vous de jouer! \n")
            print("0/ Utiliser une competence")
            print("1/ Remplacer votre Pokemon")
            print("2/ Declarer Forfait")
            choix = input("Que voulez-vous faire? \n")
            choix = mauvais_choix(choix, 2)
            
            if choix == 0:
                self.utiliser_competence(D2_PokemonActif,D1_PokemonActif)
                print(D1_PokemonActif)
                print(D2_PokemonActif)
                #on verifie si le pokemon adverse est mis KO par l attaque
                if D1_PokemonActif._Pokemon__Vie == 0:
                    print(D1_PokemonActif._Pokemon__Nom + " est KO!")
                    if D1_Pokemon!= []: #changement du pokemon actif du Dresseur1 par defaut
                        D1_PokemonActif = D1_Pokemon[0]
                        D1_Pokemon.remove(D1_PokemonActif)
                        print(self.Dresseur1._Dresseur__Nom + ", par defaut votre nouveau Pokemon acitf est: ")
                        print(D1_PokemonActif)
                    else: #dresseur 1 a perdu le combat s il n a plus de pokemon dispo
                        print(self.Dresseur1._Dresseur__Nom + ", tous vos Pokemons sont KO.")
                        print(self.Dresseur2._Dresseur__Nom + " a gagne le combat!")
                        condition = False
                        perdant = self.Dresseur1
                        gagnant = self.Dresseur2
                        break
            elif choix == 1:
                D2_PokemonActif = self.remplacer_pokemon(D2_Pokemon, D2_PokemonActif)
                print(self.Dresseur2._Dresseur__Nom + ", votre nouveau Pokemon actif est:")
                print(D2_PokemonActif)
            elif choix ==2:
                self.declarer_forfait(self.Dresseur2, self.Dresseur1)
                condition = False #fin de la partie
                perdant = self.Dresseur2
                gagnant = self.Dresseur1
                break
        
        print(gagnant._Dresseur__Nom + " chaque Pokemon de votre deck va gagner de l'experience\t" )
        for pok in gagnant._Dresseur__deck:
            exp = self.gagner_experience(perdant,pok)
            print(pok._Pokemon__Nom + " a gagné " + str(exp) + " Exp")
            pok.gagner_experience(exp)

        
        

            