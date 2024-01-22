from abc import ABC,abstractmethod
from Competence import Competence
from mauvais_choix import *
import random


class Attaque(Competence) :
    
    def __init__(self, liste_attaque):
        #Recuperation des infos sur la competence (ici attaque)

        #Création des attributs de la compétence
        super().__init__(liste_attaque[0], liste_attaque[1], liste_attaque[2],  int(liste_attaque[5]) )
        #Création des attributs spécifiques à l'attaque
        self.__Puissance = int(liste_attaque[3])
        self.__Precision = int(liste_attaque[4])
        
    @property
    def Puissance(self):
        return self.__Puissance
    
    @property
    def Precision(self):
        return self.__Precision
        
    def who(self):
        return 'Attaque'
    
    def __str__(self) : 
        afficheAttaque = self._Nom + " (Attaque, " + self._Element + ", Cout: " + str(self._Cout) + ") : " + self._Description
        return afficheAttaque
     
    #fonction qui retourne un indice entre 0 et 3 inclu en fonction des elements (du pokemon ou de la competence)
    def indice_elem(self, nomElem):
        if nomElem == "Air":
            return 0
        elif nomElem == "Eau":
            return 1 
        elif nomElem == "Feu":
            return 2
        else:
            return 3     
     
    #calcul des degats de cette attaque 
    def calcul_competence(self, pokemonAssaillant, pokemonAssailli):  # Appelle d'une fonction dans la classe Pokemon pour baisser l'nrj et la vie d'un pokémon
        #Creation tableau b pour calcul degats 
        # b[indices element pokemon][indices element competence]
        b = [[1, 1, 0.5, 1.5],[1.5, 1, 1, 0.5],[0.5, 1.5, 1, 1],[1, 0.5, 1.5, 1]]        
        #determination reussite ou echec de l attaque
        reussite = random.randint(0, 100)
        if reussite>self.Precision:
            print("Echec de l'attaque")
            degats = 0
        else:
            print("Attaque réussi!")
            niv = pokemonAssaillant._Pokemon__Niveau #niveau du pokemon assaillant
            cm = b[self.indice_elem(pokemonAssaillant._Pokemon__Element)] [self.indice_elem(self._Element)]
            degats = cm * ( ((self.Puissance * (4*niv+2)) / pokemonAssailli._Pokemon__Resistance)+2)
            degats = int(degats)
            print("Dégats infligés : " + str(degats))    
            print("\n")
        pokemonAssailli.perte_PV(degats)
        pokemonAssaillant.perte_energie(self._Cout)

        
             