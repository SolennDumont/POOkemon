from mauvais_choix import *

from abc import ABC,abstractmethod

class Competence(ABC): #Classe mère d'Attaque et de Defense
    
    def __init__(self, nom, description, element, cout):
        self._Nom = nom
        self._Description = description
        self._Element = element
        self._Cout = cout
        
    #Getters 
    #Protected : permet aux classes filles d'avoir accès à ses attributs
    @property
    def Nom(self):
        return self._Nom

    @property
    def Description(self):
        return self._Description
    
    @property
    def Element(self):
        return self._Element
    
    @property
    def Cout(self):
        return self._Cout
    
    #Méthodes abstraites 
    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def calcul_competence(self):
        pass
    
    @abstractmethod
    def who(self):
        pass


    
            



 