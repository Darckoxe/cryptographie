#!/usr/bin/python3
# -*- coding: utf-8 -*-

def vigenere_bis(mot,cle):
    message_code = []
    k = len(cle)                             # longueur de la cle
    i = 0                                    # rang dans le bloc
    # Pour chaque lettre
    for lettre in mot:
        if lettre == " ":                    # On ne touche pas aux espaces
            lettre_code = " "
        else:
            nomb = ord(lettre)-65            # Lettre devient nombre de 0 Ã  25
            nomb_code = (nomb+cle[i]) % 26   # Chiffrement de VigenÃ¨re : on ajoute n_i
            lettre_code = chr(nomb_code+65)  # On repasse aux lettres
            i=(i+1) % k                      # On passe au rang suivant
        message_code.append(lettre_code)     # On ajoute la lettre codÃ©e au message
    message_code = "".join(message_code)     # On revient Ã  une chaine de caractÃ¨re
    return(message_code)


def decode_vigenere_bis(mot,cle):
    return vigenere_bis(mot,[-n for n in cle])
