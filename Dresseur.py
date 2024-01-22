from mauvais_choix import *

class Dresseur :
    
    def __init__(self, Nom, listePokemons):
        self.__Nom = Nom
        self.__listePokemons = listePokemons #Liste des pokémons possedes par le dresseur
        self.__deck = [] 
        #par defaut, le deck est remplie par les trois premiers pokemon posseder par le dresseur
        for pok in range(len(self.listePokemons)):
            if pok<3:
                self.__deck.append(self.listePokemons[pok])
    
    @property
    def Nom(self):
        return self.__Nom
    
    @property
    def listePokemons(self):
        return self.__listePokemons
    
    @listePokemons.setter
    def listePokemons(self,pokemon): #Empêcher l'utilisateur de mettre le même pokemon 2 fois dans sa liste
        if pokemon not in self.__listePokemons:
            self.__listePokemons.append(pokemon)
    
    @property
    def deck(self):
        return self.__deck
    
    @deck.setter          
    def deck(self,pokemon): #Empêcher l'utilisateur de mettre plus de 3 pokémons dans son deck !
        if len(self.__deck)<3:
            self.__deck.append(pokemon)

    def affiche_deck(self): #Affichage du deck du dresseur
        print("Votre deck est :\n ")
        for poke in range (len(self.deck)) :
            print(str(poke)+'/ ',end='')
            print(self.deck[poke])
                  
    def __str__(self): #Affichage de toutes les informations du dresseur        
        affiche_general = "Voilà votre dresseur : " + self.Nom + ": " + str(len(self.listePokemons)) + " pokémons. Le deck est :"
        affichage_deck = "\n"
        option = 0
        for pok in self.deck :
            affichage_deck += str(option) + "\ " + pok.__str__() + "\n"
            option += 1
        return affiche_general + affichage_deck
        
        
    def changer_deck(self): #Permet à un joueur de changer son deck     
        print("Changement de deck : \n")
        condition = True # Tant que True, le dresseur est en train de changer les pokemons de son deck
        while condition:
            self.affiche_deck()
            choix = input("Quel pokémon voulez vous changer ? (0-2) \n")
            choix = mauvais_choix(choix, len(self.deck))
            self.deck.remove(self.deck[choix]) #retire le pokemon du deck
            #affiche les pokemons que le dresseur peut ajouter à son deck
            print("Voici les pokemons que vous pouvez ajouter à votre deck:\n")
            verification = [] #variable pour stocker les vrai indices des pokemon qu on peut ajouter de self.listesPokemons
            affichage = 0
            for poke in range(len(self.listePokemons)):
                if self.listePokemons[poke] not in self.deck:
                    print(str(affichage)+'/ ',end='')
                    print(self.listePokemons[poke])
                    affichage += 1
                    verification.append(poke)       
            choix = input("Par quel pokemon voulez-vous changer ? > ")
            choix = mauvais_choix(choix, affichage-1)
            self.deck = self.listePokemons[verification[choix]]
            print("Votre changement de deck a ete pris en compte: \t")
            self.affiche_deck()
            choix = input("Avez-vous fini de changer votre deck ? Veuillez répondre par oui ou par non. > ")
            choix = mauvais_choix_oui(choix)
            if choix == "Oui":
                condition = False
              
    def capturer_Pokemon(self, pokemon): #Ajoute un pokemon capture à la liste de pokemons
        self.listePokemons = pokemon
        

         
         
        

      

    
