# Programme qui qui demande à l'utilisateur une phrase et 
# affiche le nombre de majuscules et de minuscules
# Torontp, Collège Boréal, 23/11/2026
# D. Minto Dimoune 

# Demande à l'utilisateur de saisir une phrase
phrase = input("Entrez une phrase: ")

# Recherchons le nombre majuscules et de minuscules
phrase_list = phrase.split()

compteur_maj = 0
compteur_min = 0
for mot in phrase_list:
    for i in range(len(mot)):
        if mot[i].isupper() == True:
            compteur_maj += 1
        if mot[i].islower() == True:
            compteur_min += 1

print("Majuscules: ",compteur_maj)
print("Minuscules: ",compteur_min)

# Exemple
# Entrez une phrase: Bonjour Python
# Majuscules:  2
# Minuscules:  11