# Programme qui demande à l'utilisateur de saisir 
# un numéro de carte de crédit, puis l'affiche de nouveau 
# en masquant tous les caractères par des astérisques (*), 
# à l'exception des quatre derniers caractères (Exercice 10).
# Torontp, Collège Boréal, 23/11/2026
# D. Minto Dimoune 

# Demande à l'utilisateur de saisir un numéro de carte
numero_cart = input("Entrez votre numéro de carte de crédit: ")

nbre_chiffre = len(numero_cart)

numero_masque = numero_cart.replace(numero_cart[:len(numero_cart) - 4],"*"*12)

print("Numéro masqué: ",numero_masque)

# Exemple:
# Entrez votre numéro de carte de crédit: 1234567812345678
# Numéro masqué:  ************5678


