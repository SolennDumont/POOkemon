### POOkemon : le jeu orienté objet

Le projet présente un jeu de combat entre pokémons.
.
## Démarrage

Run le fichier "main.py"

## Explication diagramme UML

Lien entre classe : \
Le jeu est la classe la plus haute de la hiérarchie. Elle instancie tous les objets. Sans elle, rien n'existe : Composition \
Une compétence appartient et ne peut pas exister sans un pokémon : Composition \
Un pokémon appartient à un dresseur mais peut exister sans lui : Agrégation \
Les classes JcJ et JcE possède et utilise des dresseurs et des pokémons mais ceux là peuvent aussi exister en dehors : Agrégation \
Certains méthodes de Combat utilise des objets de la classe Pokémon. 

Encapsulation : \
Tous les attributs qui ont été mis en privé ne doivent pas être modifié extérieurement à leur classe. Certains attributs ont aussi des valeurs qu'on fixe à l'aide de setters. \
Les attributs protégés (uniquement dans Competence) doivent pouvoir être modifié uniquement dans Attaque et Defense.

## Fabriqué avec

Python 3.7.9 64-bit | Spyder IDE 5.2.1

## Auteurs

Koloina Randrianavony \
Solenn Dumont Le Brazidec

Master 1 SPI ISI 2023
