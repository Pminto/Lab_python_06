# Programme qui demande à l'utilisateur de saisir un mot, puis affiche 
# le nombre de voyelles qu'il contient (Exercice 1)
# Torontp, Collège Boréal, 23/11/2026
# D. Minto Dimoune 

# Demande à l'utilisateur de saisir un mot
mot = input("Saisir un mot tout en minuscule: ")

# Recherchons le nombre de voyelles
voyelles = ["a", "e", "i", "o", "u", "y"]

compteur = 0
for i in range(len(mot)):
    if mot[i] in voyelles:
        compteur += 1

print("Le nombre de voyelles est: ",compteur)

# Exemple
# Saisir un mot tout en minuscule: programmation
# Le nombre de voyelles est:  5
