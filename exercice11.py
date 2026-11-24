# Programme qui améliore le promme de l'exercice 10 en
# ajoutant certaines validations (Exercice 11).
# Torontp, Collège Boréal, 23/11/2026
# D. Minto Dimoune 

# Demande à l'utilisateur de saisir une phrase
numero_cart = input("Entrez votre numéro de carte de crédit contenant des espaces et des - : ")

#@ Supprimons les espace et les tirets puis affichons
# Retirons les espaces et rassemblons les caractères sans espaces
numero_cart_list = numero_cart.split()
numero_cart_list1 = "".join(numero_cart_list)
# Retirons ensuite les tirets
numero_cart_list2 = numero_cart_list1.split("-")
numero_cart_new = "".join(numero_cart_list2)

## Verifions que le numéro de carte obtenu contient uniquement des chiffres
if numero_cart_new.isdigit() != True:
    print("Le numéro ne contient pas uniquement que des chiffres")
    
## Vérifions que le numéro comporte exactement 16 chiffres
if len(numero_cart_new) != 16:
    print("Erreur! Assurez-vous que le nombre de chiffres soit 16")

##Masquage du numéro si tout est bon
nbre_chiffre = len(numero_cart_new)

numero_masque = numero_cart_new.replace(numero_cart_new[:len(numero_cart_new) - 4],"*"*12)

print("Numéro masqué: ",numero_masque)

# Exemple:
# Entrez votre numéro de carte de crédit contenant des espaces et des - : 1234-5678- 1234-5678-
# Numéro masqué:  ************5678