from mauvais_choix import *
from Competence import Competence

class Defense(Competence) :
    
    def __init__(self,liste_defense):
        
        #liste_defense = Recuperation(nomCompetence,"defense.txt") 
        nom = liste_defense[0]
        description = liste_defense[1]
        element = liste_defense[2]
        soin = liste_defense[3]
        energie = liste_defense[4] 
        cout = int(liste_defense[5])
        
        if soin =='':
            soin = 0
        else:
            soin = soin.split('-')
            soin[0] = int(soin[0])
            soin[1] = int(soin[1])

        if energie =='':
            energie = 0
        else:
            energie = energie.split('-')
            energie[0] = int(energie[0])
            energie[1] = int(energie[1])

      
        #Creation des attributs de la competence
        
        super().__init__(nom,description,element,cout) 
        self.__Soin = soin
        self.__Energie = energie
    
    
    @property
    def Soin(self):
        return self.__Soin
    
    @property
    def Energie(self):
        return self.__Energie
    

    def who(self):
        return "Defense"
     
    def __str__(self) : 
        afficheDefense = self._Nom + " (Defense, " + self._Element + ", Cout: " + str(self._Cout) + ") : " + self._Description
        return afficheDefense

                
    #calcul des soins apportes par la competence
    #IMPACT SUR ENERGIE OU VIE DU pokemon
    def calcul_competence(self,pokemon):
        #si la competence restaure des points de vie
        if self.Soin !=0:
            soin = random.randint(self.Soin[0],self.Soin[1])
            #pokemon._Pokemon__Vie += soin
            pokemon.ajout_PV(soin)
        else:
        #si la competence restaure de l energie
            energie = random.randint(self.Energie[0],self.Energie[1])
            #pokemon._Pokemon__Energie += energie
            pokemon.ajout_energie(energie)
        pokemon.perte_energie(self._Cout)