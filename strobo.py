""" Un nombre est dit strobogrammatique lorsqu'il s'ecrit de la meme maniere apres avoir subi une rotation de 180deg """


def is_strobogrammatic(n: int) -> bool:
    # on definit un dictionnaire avec comme cle le chiffre avant rotation et comme valeur le chiffre apres rotation
    strobo_digits = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    # on transforme en chaine de caractere chaque entree pour eviter les eventuelles erreurs
    n = str(n)

    # left et right representent les indices du nombre a evaluer
    left = 0
    right = len(n)-1

    # on boucle pour parcourir tous les caracteres du nombre
    while right - left >= 0:
        if n[left] and n[right] not in strobo_digits.keys() or n[left] != strobo_digits[n[right]]:
            return False

        left += 1
        right -= 1

        return True

# a titre d'exemple on verifie les nombres strobogrammatiques parmi les 100 premiers entiers
""" for i in range(100):
    if is_strobogrammatic(i):
        print(i) """