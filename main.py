"cette fonction retourne si un mots ou une phrase est un palindrome"
def ispalindrome(p):
    """definition de la fonction secondaire palindrome
    """
    p=p.lower()
    table=str.maketrans('àéçèôöúùüîïêë','aeceoouuuiiee')
    p=p.replace(' ','')
    p=p.replace(',','')
    p=p.replace('?','')
    p=p.replace(';','')
    p=p.replace('!','')
    p=p.replace("'","")
    p=p.replace('-','')
    p=p.replace(':','')
    p=p.translate(table)
    if p==p[::-1]:
        return True
    return False

#### Fonction principale


def main():
    """
   la fonction principale teste le programme en faisant appel à la fonction sécondaire
   """
    # vos appels à la fonction secondaire ici
for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
    print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
