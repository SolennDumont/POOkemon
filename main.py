import random
from Attaque import Attaque
from Defense import Defense
from Pokemon import Pokemon
from Dresseur import Dresseur
from JcJ import JcJ
from JcE import JcE
from Jeu import Jeu

#from mauvais_choix import mauvais_choix

nomfichierPokemon = "pokemon.txt"
nomfichierAttaque = "attaque.txt"
nomfichierDefense = "defense.txt"
fichierSauvAnciennePartie = "Sauvegarde\Sauvegarde.txt"

#Lancer une partie :
Partie = Jeu(nomfichierPokemon,nomfichierAttaque, nomfichierDefense, fichierSauvAnciennePartie)
Partie.Jouer()


