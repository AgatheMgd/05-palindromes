"""
Module pour vérifier si une chaîne de caractères est un palindrome.
La fonction ispalindrome() ignore les majuscules, les accents et les caractères spéciaux 
pour effectuer la vérification du palindrome.
"""
import re
import unidecode

def ispalindrome(p):

    """ 
    Vérifie si la chaîne de caractère passé en paramètre est un palindrome.
    
    La fonction ignore tout ce qui est accent et ponctuation, pour cela on utilise
    des méthodes importés pour faciliter la conversion.
    
    Exemple d'utilisation :
    
    >>> ispalindrome("trousse")
    False
    >>> ispalindrome("ressasser")
    True
    >>> ispalindrome("été")
    True
    >>> ispalindrome("table")
    False

    """
    p = p.lower()
    p = unidecode.unidecode(p)  #Converti les caractères spéciaux
    p = re.sub(r'[^a-zA-Z0-9]', '', p) #Supprimer les caractères non "alphanumériques"

    return p == p[::-1]

#### Fonction principale

def main():

    """ 
    Fonction qui teste le fonctionnement de ispalindrome()
    """
    # Appel de la fonction ispalindrome pour différents exemples
    ispalindrome("trousse")
    ispalindrome("ressasser")
    ispalindrome("été")
    ispalindrome("table")

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
