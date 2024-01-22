import random
#import sys

#Permet de vérifier le choix de l'utilisateur
def mauvais_choix(choix, nbmax): 
    liste_reponse = ["Vous avez fait une erreur : ", "Recommencez : ", "Veuillez choisir un chiffre entre 0 et " + str(nbmax) + " : "]
    #Uniquement pour test développement
    # if choix == "stop" : 
    #     sys.exit()
    if choix.isnumeric() and (int(choix) >= 0) and (int(choix) <= nbmax):
        return int(choix)        
    else :
        choix = input(liste_reponse[random.randint(0, len(liste_reponse)-1)])
        choix = mauvais_choix(choix, nbmax)
        return choix

#Permet de vérifier le choix de l'utilisateur        
def mauvais_choix_oui(choix):    
    liste_reponse = ["Vous avez fait une erreur : ", "Recommencez : ", "Veuillez écrire oui ou non : "]
    #Uniquement pour test développement
    # if choix == "stop" :
    #     sys.exit()   
    if choix == "Oui"  or choix == "oui":
        return "Oui"  
    elif choix == "Non" or choix == "non" :
        return "Non"
    else :
        choix = input(liste_reponse[random.randint(0, len(liste_reponse)-1)])
        choix = mauvais_choix_oui(choix)
        return choix




