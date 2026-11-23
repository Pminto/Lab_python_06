# Programme qui vérifie si un mot est un palindrome (Exercice 4).
# Torontp, Collège Boréal, 23/11/2026
# D. Minto Dimoune 

# Demande à l'utilisateur de saisir une chaîne de caractères
mot = input("Entrez un mot: ")

# Trouvons l'inverse du mot
mot_inv = mot[::-1]

compteur = 0
for i in range(len(mot)):
    if mot[i] == mot_inv[i]:
        compteur += 1

if compteur == len(mot):
    print("Le mot est un palindrome.")
else:
    print("Le mot n'est pas un palindrome.")

# Exemple
# Entrez une mot: radar
# Le mot est un palindrome.
# Entrez une mot: Bonjour
# Le mot n'est pas un palindrome.