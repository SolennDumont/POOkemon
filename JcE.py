from Combat import Combat
from mauvais_choix import *
from Attaque import Attaque
from random import randint


class JcE(Combat): # Combat entre un dresseur et un pokémon
    
    def __init__(self, Dresseur1, pokemon):
        super().__init__(Dresseur1)
        self.pokemon = pokemon

    def gagner_experience(self):
    
        print(self.Dresseur1._Dresseur__Nom + " chaque Pokemon de votre deck va gagner de l'experience\t" )
        
        for pok in self.Dresseur1._Dresseur__deck:
            
            exp = 10 + self.pokemon._Pokemon__Niveau - pok._Pokemon__Niveau
            print(pok._Pokemon__Nom + " a gagné " + str(exp) + " Exp")
            pok.gagner_experience(exp)

    def capturer_pokemon(self):
        
            reussite = random.randint(0, 100)
            proba = 4*(0.2 - self.pokemon._Pokemon__Vie / self.pokemon._Pokemon__VieMax)
            if reussite < proba*100 :
                print("Vous avez capturé " + self.pokemon._Pokemon__Nom)
                print("Le pokémon rejoint votre liste pokémon jouable définitivement sauf si vous possédez déja ce pokemon\n")
                self.Dresseur1.capturer_Pokemon(self.pokemon)
                #self.Dresseur1._Dresseur__listePokemons.append(self.pokemon)
                capture = True
            else :
                print("\nEchec de la capture\n")
                capture = False
            return capture
   
    
    def utiliser_competence_IA(self, pok_actif): #Competence utilisee aleatoirement #IA à améliorer
        c = randint(0, len(self.pokemon._Pokemon__Competences)-1)        
        print(self.pokemon._Pokemon__Nom + " a choisi d'utiliser " + self.pokemon._Pokemon__Competences[c]._Nom)
        #Condition ou le pokemon ne peut lancer la competence que s il a l'energie necessaire pour la lancer
        if self.pokemon._Pokemon__Energie < self.pokemon._Pokemon__Competences[c]._Cout :
            print("Vous n'avez pas assez d'energie pour lancer cette compétence\t")
        else:
            #Calcul degat ou soin de la competence choisi par le pokémon
            if self.pokemon._Pokemon__Competences[c].who() == 'Defense':
                self.pokemon.Competences[c].calcul_competence(self.pokemon)
            else:
                self.pokemon._Pokemon__Competences[c].calcul_competence(self.pokemon, pok_actif)
        
    def jouer(self):
        
        tour = 0 #Compteur nbr de Tour de jeu
        perdant = ""
        gagnant = ""
        #reinitialiser Vie et Energie de tous les Pokemons du deck de Dresseur a leur max avant combat
        for pok in self.Dresseur1._Dresseur__deck:
            pok.reinitialisation()
        
        #Choix du pokemon actif Dresseur
        print(self.Dresseur1)        
        choix = input("Quel pokemon voulez vous utiliser? (0-2) > ")
        choix = mauvais_choix(choix, 2)
        D_PokemonActif = self.Dresseur1._Dresseur__deck[choix] #pokemon actif Dresseur
        print("\n")
        #liste des pokemons qui peuvent encore etre utilisee lors de la partie hormis le pokemon actif
        # si = liste vide, partie terminee
        D_Pokemon = []
        for pok in self.Dresseur1._Dresseur__deck:
            D_Pokemon.append(pok)
        D_Pokemon.remove(D_PokemonActif)
        
        capturer_dispo = False
        
        while True:
            
            tour += 1
            
            
            print("\n-------------\n")
            print("Tour " + str(tour))
            print("\n")
            
            # Au debut de chaque tour, chaque pokemon actif voit son energie regenerer de la valeur regeneration propre a chaque pokemon
            D_PokemonActif.ajout_energie(D_PokemonActif._Pokemon__Regeneration)
            self.pokemon.ajout_energie(self.pokemon._Pokemon__Regeneration)
            
            #TOUR DU DRESSEUR
            print(self.Dresseur1._Dresseur__Nom +  " c'est a  vous de jouer! \n")
            print("0/ Utiliser une competence")
            print("1/ Remplacer votre Pokemon")
            print("2/ Declarer Forfait")
            
            if capturer_dispo :
                print("3/ Capturer le pokémon")
                choix = input("Que voulez-vous faire? > ")
                choix = mauvais_choix(choix, 3)
            else :                              
                choix = input("Que voulez-vous faire? > ")
                choix = mauvais_choix(choix, 2)
            
            print("\n")
            if choix == 3 :
                self.capturer_pokemon()
                break

            elif choix == 0: #utiliser competence
            
                self.utiliser_competence(D_PokemonActif, self.pokemon)
                print(D_PokemonActif)
                print(self.pokemon)
                
                #on verifie si le pokemon adverse est mis KO par l attaque
                if self.pokemon._Pokemon__Vie == 0:
                    print(self.pokemon._Pokemon__Nom + " est KO!")
                    print(self.Dresseur1._Dresseur__Nom + " a gagne le combat !")
                    self.gagner_experience()
                    break
                
                elif self.pokemon._Pokemon__Vie < (self.pokemon._Pokemon__VieMax/100) * 20 and not(capturer_dispo):
                    capturer_dispo = True
                    print("Vous avez affaibli le pokémon")
                    print("Vous pouvez dès à présent tenter de le capturer ou continuer de l'affaiblir pour avoir plus de chance de le capturer\n")
                
                #Cas où le pokémon se soigne et/ou message déjà indiqué
                elif self.pokemon._Pokemon__Vie > (self.pokemon._Pokemon__VieMax/100) * 20 and (capturer_dispo):  
                    capturer_dispo = False 
                             
            elif choix == 1: #remplacer pokemon actif
                D_PokemonActif = self.remplacer_pokemon(D_Pokemon, D_PokemonActif)
                print(self.Dresseur1._Dresseur__Nom + ", votre nouveau pokemon actif est:")
                print(D_PokemonActif)
                
                
            elif choix == 2: #forfait du dresseur
                
                print("Vous avez déclaré forfait")
                print(self.pokemon._Pokemon__Nom + " est déclaré vainqueur ! Vive lui")
                break
            
                    
            #TOUR DE L'IA
            print("\n\nTour de " + self.pokemon._Pokemon__Nom)
            self.utiliser_competence_IA(D_PokemonActif)
            
            #on verifie si le pokemon du dresseur est mis KO par l attaque
            if D_PokemonActif._Pokemon__Vie == 0:
                print(D_PokemonActif._Pokemon__Nom + " est KO!")
                
                if D_Pokemon != []: #changement du pokemon actif du dresseur par defaut
                    D_PokemonActif = D_Pokemon[0]
                    D_Pokemon.remove(D_PokemonActif)
                    print(self.Dresseur1._Dresseur__Nom + ", par défaut votre nouveau pokemon actif est: ")
                    print(D_PokemonActif)
                    
                else: #dresseur a perdu le combat s il n a plus de pokemon dispo
                    print(self.pokemon._Pokemon__Nom + " a gagné !\n")
                    print("Vous avez perdu tous ses pokemons !")
                    break
        
        
        print("Le combat s'achève ici. Vous êtes libres de rejoindre un autre combat.\n")
            
            
            
            