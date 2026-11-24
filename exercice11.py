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
if numero_cart_new.isdigit() == True:
    print("Le numéro contient uniquement que des chiffres")
else:
    print("Le numéro ne contient pas uniquement que des chiffres")
    

