# Programme qui demande une phrase à l'utilisateur et 
# affiche le mot le plus long (Exercice 9).
# Torontp, Collège Boréal, 23/11/2026
# D. Minto Dimoune 

# Demande à l'utilisateur de saisir une phrase
phrase = input("Entrez une phrase: ")

# Cherchons le mot le plus long 
phrase_list = phrase.split()

long_mot = []
for mot in phrase_list:
    long_mot.append(len(mot))

ind_long_mot = long_mot.index(max(long_mot))

print("le mot le plus long est: ",phrase_list[ind_long_mot])

# Exemple
# Entrez une phrase: J'aime apprendre la programmation
# le mot le plus long est:  programmation
# Entrez une phrase: " Bonjour Jean, 2026 "
# le mot le plus long est:  Bonjour