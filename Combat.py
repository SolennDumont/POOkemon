from abc import ABC,abstractclassmethod
from mauvais_choix import *

class Combat(ABC):
    
    def __init__(self, Dresseur1):
        self.Dresseur1 = Dresseur1
        
    @abstractclassmethod
    def  gagner_experience(self):
        pass
    @abstractclassmethod
    def jouer(self):
        pass

    def utiliser_competence(self, pokemon, pok_defendant):
        print("Vous avez choisi d'utiliser une competence\t ")
        print("Les competences que vous pouvez utiliser sont :\t ")
        temp = 0 
        #affichage des competences du pokemon actif
        for comp in pokemon._Pokemon__Competences:
            print(str(temp) + "/ ", end="")
            print(comp)
            temp += 1

        #choix du dresseur
        choix = input("Quelle competence voulez-vous utiliser ? (0-" +  str(temp-1) + ") > ")
        choix = mauvais_choix(choix, temp-1)
        print("\n")
        
        #condition ou le pokemon ne peut lancer la competence que s il a l energie necessaire pour la lancer
        if pokemon._Pokemon__Energie<pokemon._Pokemon__Competences[choix]._Cout:
            print("Vous n'avez pas assez d'energie pour lancer cette compétence\t")
        else:
            #Calcul degat ou soin de la competence choisi par le Dresseur
            if pokemon._Pokemon__Competences[choix].who() == 'Defense':
                pokemon.Competences[choix].calcul_competence(pokemon)
            else:
                pokemon._Pokemon__Competences[choix].calcul_competence(pokemon, pok_defendant)

           
    #listePokdispo : liste des pokemons qui n'ont pas encore ete mis KO
    def remplacer_pokemon(self,listePokDispo, pokemonActif):
        
        if listePokDispo != []:
            print("Vous avez choisi de remplacer votre pokemon actif\t \n")
            print("Votre Pokemon actif est:\t \n")
            print(pokemonActif)
            print("Vous pouvez choisir parmis ses Pokemons:\t")
            temp = 0
            for poke in listePokDispo:
                print(str(temp)+"/ ", end='')
                print(poke)
                temp += 1
            choix = input("\nQuel Pokemon voulez-vous utiliser? (0-" + str(temp-1) + ")\t")
            choix = mauvais_choix(choix, temp-1)
            newPokemon = listePokDispo[choix]
            listePokDispo.append(pokemonActif)
            listePokDispo.remove(newPokemon)
            return newPokemon
        else : 
            print("Vous n'avez pas d'autres pokémons dans votre deck")
            return pokemonActif
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    