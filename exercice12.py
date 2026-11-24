# Programme qui demande à l’utilisateur un mot de passe 
# et vérifie certaines conditions (Exercice 12).
# Torontp, Collège Boréal, 24/11/2026
# D. Minto Dimoune 

# Demande à l'utilisateur de saisir un mot de passe
mot_de_passe= input("Entrez un mot de passe : ")
# Vérifions que le mot de passe contient au moins 8 caractères
if len(mot_de_passe) < 8: 
    print("le mot de passe ne contient pas au moins 8 caractères")
else:
    print("le mot de passe contient au moins 8 caractères")

# Vérifions que le mot de passe contient une lettre majuscule
compteur_maj = 0
for i in range(len(mot_de_passe)):
    if mot_de_passe[i].isupper() == True:
        compteur_maj += 1
if compteur_maj == 0:
    print("Le mot de passe ne contient pas de majuscule")
elif compteur_maj == 1:
    print("Le mot de passe ontient une majuscule")
else:
    print("Le mot de passe contient au moins une majuscule")





