
""" 
Quiz 4 / Question 4

On considère deux jeux de hasard :

Le jeu A est un jeu de pile ou face avec une pièce biaisée (pile avec une probabilité de p=0.49). 
On lance la pièce. Si l'on obtient pile, on gagne un euro, sinon on perd un euro.

Le jeu B est un jeu avec deux pièces biaisées. La pièce 1 donne pile avec une probabilité p1 = 0.09 et 
la pièce 2 donne pile avec une probabilité p2 = 0.74. 
Si la somme en jeu de K euros est un multiple de 3, 
on lance la pièce 1, sinon on lance la pièce 2. Comme dans le jeu A, si l'on obtient pile, on gagne un euro, sinon on perd un euro.

Le jeu A est clairement perdant. Le jeu B l'est aussi (vous pourrez le vérifier). 

À présent, on va mixer les deux ! En effet, à chaque tour, on lance une pièce (cette fois-ci...) équilibrée ! Si l'on a pile, on joue au jeu A, sinon on joue au jeu B.

On suppose que le joueur a 0 euros comme capital de départ.
Après avoir joué 1.000.000 de parties, quel est le statut du jeu, du point de vue du joueur ?

Je vous conseille fortement d'organiser votre code en plusieurs fonctions, pour pouvoir en simplifier l'organisation et la relecture.

- Jeu gagnant
- Jeu perdant
- Jeu neutre (les gains sont proches de 0 en fin de compte)
"""

import random

print("\n####################################################################################")
print("Initiez-vous à Python pour l'analyse de données - Quiz 4 / Question 4")
print("####################################################################################\n")

def game_A():
    if random.uniform(0,1) <= 0.49:
        return 1
    else:
        return -1

def game_B1():
    if random.uniform(0,1) <= 0.09:
        return 1
    else:
        return -1

def game_B2():
    if random.uniform(0,1) <= 0.74:
        return 1
    else:
        return -1

def balanced_piece():
    if random.uniform(0,1) <= 0.5:
        return 1
    else:
        return -1

avg = 0

for i in range(10):
    n = 1000000
    gain = 0

    for i in range(n):
        result_game = balanced_piece()
        if result_game == 1:
            gain += game_A()
        else:
            if gain % 3 == 0:
                gain += game_B1()
            else:
                gain += game_B2()
    
    avg += gain

print("The net gain is: ", avg/10, "€")