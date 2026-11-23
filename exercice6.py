# Programme qui demande à l'utilisateur un nom d'utilisateur 
# et vérifie qu'il contient des lettres, des chiffres, et
# possède au moins 5 caractères (Exercice 6).
# Torontp, Collège Boréal, 23/11/2026
# D. Minto Dimoune 

# Demande à l'utilisateur de saisir nom d'utilsateur
nom = input("Entrez un nom d'utilisateur: ")

# Trouvons si le nom contient des lettres, des chiffres, et 
# au moins 5 caractères
while nom.isalpha() == True or nom.isdigit() == True:
    print("Erreur, le nom doit contenir des lettres et des chiffres")
    nom = input("Entrez un nom d'utilisateur: ")

while len(nom) <= 5: 
    print("Erreur, le nom doit contenir au moins 5 caractères")
    nom = input("Entrez un nom d'utilisateur: ")

print("Le nom est valide") 

# Exemple
# Entrez un nom d'utilisateur: 123456
# Erreur, le nom doit contenir des lettres et des chiffres
# Entrez un nom d'utilisateur: joseph
# Erreur, le nom doit contenir des lettres et des chiffres
# Entrez un nom d'utilisateur: joe5
# Erreur, le nom doit contenir au moins 5 caractères
# Entrez un nom d'utilisateur: jean2026
# Le nom est valide