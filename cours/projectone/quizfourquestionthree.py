""" 
####################################################

Initiez-vous à Python pour l'analyse de données

####################################################
"""

""" 
Quiz 4 / Question 3

Considérons l'expérience suivante :
Soit 10.000 lancers d'un dé équilibré classique (à 6 faces). Parmi ces 10.000 lancers, on en prend 1.000 aléatoirement.
On réalise 5 fois cette expérience, et on note m la moyenne des fréquences de 6 obtenus sur les 10.000 lancers et n 
la moyenne des fréquences de 4 obtenus dans le sous-échantillon. Quelles seraient les valeurs de m et n à l'issue de cette expérience ?

L'aléatoire rend les résultats trop variables pour répondre strictement à cette question.

- m  et  n  seront proches de 1/6.
- m  sera proche de 1/6,  n  sera proche de (1/6)/10 = 1/60.
- m  sera proche de 1/6 et il n'est pas possible de savoir pour  n  à cause de l'aléatoire.
"""

import random

print("\n####################################################################################")
print("Initiez-vous à Python pour l'analyse de données - Quiz 4 / Question 3")
print("####################################################################################\n")

m = 0
n = 0

for i in range(5):

    list_launches = []

    for j in range(10000):
        list_launches.append(random.randint(1,6))

    sample_launches = random.sample(list_launches, 1000)

    m += list_launches.count(6)/10000
    n += sample_launches.count(4)/1000

print("m = ", m/5, "\nn = ", n/5, "\n")
#print("m = ", m/5, "\nn = ", n/5, sep="\n") #`\n` will put each word in a new line