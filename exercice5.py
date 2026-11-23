# Programme qui demande à l'utilisateur une phrase et 
# affiche le nombre de mots qu'elle contient (Exercice 5).
# Torontp, Collège Boréal, 23/11/2026
# D. Minto Dimoune 

# Demande à l'utilisateur de saisir une phrase
phrase = input("Entrez une phrase: ")

# Trouvons le nombre de mots
mots = phrase.split()

print("Le nombre de mots dans la phrase est:",len(mots))

# Exemple
# Entrez une phrase: J'aime apprendre Python
# Le nombre de mots dans la phrase est: 3