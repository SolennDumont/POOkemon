from mauvais_choix import *
from Competence import Competence
from Defense import Defense
from Attaque import Attaque
from abc import ABC,abstractmethod
import random

class Pokemon :
   
    def __init__(self, Pokemon):
        
        self.__Nom = Pokemon[0]
        self.__Avant = Pokemon[1]
        self.__Apres = Pokemon[2]
        self.__Element = Pokemon[3]

        
        #Niveau du pokemon
        Max = Pokemon[4].split('-')
        self.__Niveau = int(Max[0]) 
        self.__NiveauMax = int(Max[1]) #pour le level up
        
        #Experience du pokemon
        self.__Exp = 0
        
        #Vie du pokemon
        Max = Pokemon[5].split('-')
        self.__VieMax = int(Max[0])
        self.__Vie = int(Max[0])
        self.__VieMaxUp = int(Max[1]) # Vie Max que peut avoir le pokemon pour le level up
        

        #Energie d'un pokemon
        Max = Pokemon[6].split('-')
        self.__Energie = int(Max[0])
        self.__EnergieMax = int(Max[0]) 
        self.__EnergieMaxUp = int(Max[1]) # Energie Max que peut avoir le pokemon pour le level up
        
        #Regeneration d'un pokemon        
        Max = Pokemon[7].split('-')
        self.__Regeneration = int(Max[0])
        self.__RegenerationMax = int(Max[1]) 
        
        #Resistance d'un pokemon
        Max = Pokemon[8].split('-')
        self.__Resistance = int(Max[0])
        self.__ResistanceMax = int(Max[1])       
        
        #Récupère les competences correspondant au pokémon sous forme de liste :        
        #Liste des competences en str:  
        competences = Pokemon[9][1:len(Pokemon[9])-1].split(", ")
        self.__Competences = [] #attribut Comptences
        #Transformation de cette liste de str en liste de Competences(Attaque ou Defense)
        for comp in competences:
            #On vérifie la nature de la competence pour savoir dans quel fichier chercher les informations
            #Ouverture du fichier contenant les informations de la competence 
                       
            #On veut créer une liste de compétence
            nat = 1
            with open("defense.txt") as f :
                lines = f.read()
                nbline = lines.split("\n")
                #Recherche de la competence dans le fichier texte  
                i = 1
                liste_defense = nbline[i].split("\t")
                while i<len(nbline):
                    if liste_defense[0] == comp : #La compétence est une défense
                        nat = 0
                        self.__Competences.append(Defense(liste_defense))
                        break
                    liste_defense = nbline[i].split("\t")
                    i += 1
                  
            if nat == 1 : #Pas trouvee dans defense.txt
                with open("attaque.txt") as f:
                    lines = f.read()
                    nbline = lines.split("\n")
                    #Recherche de la competence dans le fichier texte  
                    i = 1
                    liste_attaque = nbline[i].split("\t")
                    nat = 1
                    while i<len(nbline):
                        if liste_attaque[0] == comp : #La compétence est une défense
                            nat = 0
                            self.__Competences.append(Attaque(liste_attaque))
                            break
                        liste_attaque = nbline[i].split("\t")
                        i += 1
            
                        
                
    def addFromSave(self, Niveau, Experience, VieMax, EnergieMax, Regeneration, Resistance):
        
        #Permet de créer des pokémons de la sauvegarde
        
        self.__Niveau = int(Niveau)
    
        #Experience du pokemon
        self.__Exp = int(Experience)
        
        #Vie du pokemon
        self.__VieMax = int(VieMax)
        self.__Vie = int(VieMax)
        
        #Energie d'un pokemon
        self.__Energie = int(EnergieMax)
        self.__EnergieMax = int(EnergieMax)
        
        #Regeneration d'un pokemon        
        self.__Regeneration = int(Regeneration)
        
        #Resistance d'un pokemon
        self.__Resistance = int(Resistance)


    # Attribut Nom et Element en privee
    @property
    def Nom(self):
        return self.__Nom
    
    @property
    def Avant(self):
        return self.__Avant
    
    @property
    def Apres(self):
        return self.__Apres
    
    @property
    def Element(self):
        return self.__Element
    
    # Attribut Niveau et NiveauMax en privee
    @property
    def Niveau(self):
        return self.__Niveau
    
    @property
    def NiveauMax(self):
        return self.__NiveauMax
    
    @Niveau.setter
    def Niveau(self, value):
        if value < 0 :
            self.__Niveau = self.__Niveau
        elif value  > self.__NiveauMax :
            self.__Niveau = self.__NiveauMax
        else:
            self.__Niveau = value
    

    # Attribut VieMax,Vie et VieMaxUp en privee :    
    @property
    def VieMaxUp(self):
        return self.__VieMaxUp
    
    @property 
    def VieMax(self):
        return self.__VieMax
    
    @VieMax.setter
    def VieMax(self,value):
        if value > self.__VieMaxUp:
            self.__VieMax = self.__VieMaxUp
        elif value < self.__VieMax:
            self.__VieMax = self.__VieMax
        else:
            self.__VieMax = value
    
    @property
    def Vie(self):
        return self.__Vie
    
    @Vie.setter
    def Vie(self, value):
        if (value < 0):
            self.__Vie =0
        elif value > self.__VieMax:
            self.__Vie = self.__VieMax
        else:
            self.__Vie = value
    
    #Attribut EnergieMax, Energie et EnergieMaxUp en privee:
    @property
    def EnergieMaxUp(self):
        return self.__EnergieMaxUp
    
    @property
    def EnergieMax(self):
        return self.__EnergieMax
    
    @EnergieMax.setter
    def EnergieMax(self,value):
        if (value > self.__EnergieMaxUp):
            self.__EnergieMax = self.__EnergieMaxUp
        elif (value < self.__EnergieMax):
            self.__EnergieMax = self.__EnergieMax
        else:
            self.__EnergieMax = value
            
    @property
    def Energie(self):
        return self.__Energie
    
    @Energie.setter
    def Energie(self, value):
        if (value < 0):
            self.Energie = 0
        elif (value > self.__EnergieMax):
            self.__Energie = self.__EnergieMax
        else:
            self.__Energie = value
    
    #Attribut Exp en privee
    @property
    def Exp(self):
        return self.__Exp
    
    @Exp.setter
    def Exp(self,value):
        if (value< 0):
            self.__Exp = 0
        else:
            self.__Exp = value
        
    #Attribut Regeneration, RegenerationMax et RegenerationMaxUp en privee:
    @property
    def RegenerationMax(self):
        return self.__RegenerationMax
    
    @property
    def Regeneration(self):
        return self.__Regeneration
    
    @Regeneration.setter
    def Regeneration(self,value):
        if (value > self.__RegenerationMax):
            self.__Regeneration = self.__RegenerationMax
        elif (value < self.__Regeneration):
            self.__Regeneration = self.__Regeneration
        else:
            self.__Regeneration = value
            

    #Attribut Resistance, ResistanceMax et ResistanceMaxUp mis en privee:
    @property
    def ResistanceMax(self):
        return self.__ResistanceMax
    
    @property
    def Resistance(self):
        return self.__Resistance

    @Resistance.setter
    def Resistance(self,value):
        if (value > self.__ResistanceMax):
            self.__Resistance = self.__ResistanceMax
        elif (value < self.__Resistance):
            self.__Resistance = self.__Resistance
        else:
            self.__Resistance = value
            
    @property
    def Competences(self):
        return self.__Competences

    def __str__(self):
        afficheGenerale = self.Nom + " (Lvl " + str(self.Niveau) + " " + self.Element + " exp:"+ str(self.Exp) + "/100) : "
        afficheVie = "Vie " + str(self.Vie) + "/" + str(self.VieMax) + " "
        afficheEnergie = "Energie " + str(self.Energie) + "/" + str(self.EnergieMax) + " (+" + str(self.Regeneration) + ") "
        afficheResistance = "Resistance " + str(self.Resistance) + " "
        afficheCompetence = self.Competences[0].Nom       
        for comp in range (1,len(self.Competences)) :
            afficheCompetence += ", " + self.Competences[comp].Nom
        return afficheGenerale + afficheVie + afficheEnergie + afficheResistance + "\n" + afficheCompetence

    def __eq__(self, other): #Retourne vrai si les deux pokémons sont identiques
        if self.Nom != other.Nom : #Il suffit de comparer les noms pour savoir si c'est le même pokémon
            return False
        else:
            return True
  
    #reinitialise vie et energie du pokemon a son max
    #methode utile avant un combat
    def reinitialisation(self):
        self.Energie = self.EnergieMax
        self.Vie = self.VieMax

    #methode pour ajouter de l experience au pokemon
    def gagner_experience(self, exp): 
        self.Exp = self.Exp + exp
        print(self)
        if self.Exp == 100:
            self.Exp = 0
            self.monter_niveau()

    #methode pour retirer "valeur" Vie 
    def perte_PV(self, valeur):
        self.Vie = self.Vie - valeur
        
    #methode pour ajouter "valeur" Vie 
    def ajout_PV(self, valeur):
        self.Vie = self.Vie + valeur
    
    #methode pour retirer "valeur" Energie
    def perte_energie(self,valeur):
        self.Energie = self.Energie - valeur

    #methode pour ajouter "valeur" Energie
    def ajout_energie(self,valeur):
        self.Energie = self.Energie + valeur
    
    
    def monter_niveau(self, ia_pok = False):
        if not ia_pok:
            print(self.Nom + " a accumulé assez d'expérience pour monter de niveau!")
            
        if self.Niveau<self.NiveauMax:
            # Niveau du pokemon augmente
            self.Niveau = self.Niveau + 1
            # Les statistiques du pokemon augmentent d'une valeur aleatoire entre 1 et 5
            # Vie
            up = random.randint(1, 5)
            self.VieMax = self.VieMax + up
            # Energie
            up = random.randint(1, 5)
            self.EnergieMax = self.EnergieMax + up
            # Resistance
            up = random.randint(1, 5)
            self.Resistance = self.Resistance + up
            # Regeneration
            up = random.randint(1, 5)
            self.Regeneration = self.Regeneration + up
            self.reinitialisation()
            if (not ia_pok):
                print(self)
               
        elif self.Niveau==self.NiveauMax and self.Apres!="":
            if (not ia_pok):
                print("Votre pokemon va évoluer vers une nouvelle forme!")
            self.evolution() #evolution du Pokemon
            if (not ia_pok):
                self.reinitialisation()
                print(self.__str__())
            
        elif self.Niveau==self.NiveauMax and self.Apres=="" and not ia_pok:
            print("Votre pokemon a atteint son niveau max et est dans sa forme la plus évoluée.")
            print(self)
            
    # methode qui gere l evolution du pokemon vers une nouvelle forme
    # avant de lancer cette methode, on s'est deja assure que self.Apres!=""
    def evolution(self):        
        #Ouverture du fichier contenant les informations de la competence        
        with open("pokemon.txt") as f :     
            lines = f.read()
            nbline = lines.split("\n") 
            #Recherche de la competence dans le fichier texte
            i = 1
            liste = nbline[i].split("\t")
            i+=1    
            while (liste[0] != self.Apres):
                liste = nbline[i].split("\t")
                i += 1 

        self.__init__(liste)
        
        
        

























