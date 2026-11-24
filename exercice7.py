# Programme qui demande une adresse courriel et vérifie 
# qu'elle contient @ et un point (.) après le @ (Exercice 7).
# Torontp, Collège Boréal, 23/11/2026
# D. Minto Dimoune 

# Demande à l'utilisateur de saisir son adresse courriel
email = input("Entrez une adresse courriel: ")

# Vérifions si l'adresse courriel est valide

while True: 
    if email.find("@") == -1:
        print("Erreur, l'adresses corriel ne contient pas @")
        email = input("Entrez une adresse courriel valide: ") 
    elif email[email.find("@"):].find(".") == -1:
        print("Erreur, l'adresses corriel ne contient pas point après @")
        email = input("Entrez une adresse courriel valide: ")
    else:
        print("L'adresse courriel est valide") 
        break
  

# Exemple
# Entrez une adresse courriel: jeanatgmail.com
# Erreur, l'adresses corriel ne contient pas @
# Entrez une adresse courriel valide: jean@gmaildotcom
# Erreur, l'adresses corriel ne contient pas point après @
# Entrez une adresse courriel valide: jeanatgmaildotcom
# Erreur, l'adresses corriel ne contient pas @
# Entrez une adresse courriel valide: jean@gmail.com
# L'adresse courriel est valide