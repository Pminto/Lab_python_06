# Programme qui demande une chaîne de caractères puis affiche
# le nombre de lettres, le nombre de chiffres et le nombre
# d'espace (Exercice 8).
# Aussi valable par pour la vérification d'une phrase
# Torontp, Collège Boréal, 23/11/2026
# D. Minto Dimoune 

# Demande à l'utilisateur de saisir une chaine de caractère
chaine = input("Entrez une chaine de caractère: ")

# Vérifions la chaine de caractère
longueur = len(chaine)

chaine_list = chaine.split()

compteur_lettre = 0 
compteur_chiffre = 0 
for mot in chaine_list:
    for i in range(len(mot)):
        if mot[i].isalpha() == True:
            compteur_lettre += 1 
        elif mot[i].isdigit() == True:
            compteur_chiffre += 1 
        else:
            print("C'est un autre type de caractère")

compteur_space = longueur - (compteur_lettre + compteur_chiffre)

print("Le nombre de lettres est: ",compteur_lettre)
print("Le nombre de chiffres est: ",compteur_chiffre)
print("Le nombre d'espace est: ",compteur_space)

# Exemple
# Entrez une chaine de caractère:  Bonjour Jean 2026 
# Le nombre de lettres est:  11
# Le nombre de chiffres est:  4
# Le nombre d'espace est:  4