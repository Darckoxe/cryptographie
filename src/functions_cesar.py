#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import string

def cesar_bis(mot,n):
    message_code = []
    # Pour chaque lettre
    for lettre in mot:
        if lettre == " ":                    # On ne touche pas aux espaces
            lettre_code = " "
        else:
            nomb = ord(lettre)-65            # Lettre devient nombre de 0 Ã  25
            nomb_code = (nomb+n) % 26        # Chiffrement de CÃ©sar : on ajoute n
            lettre_code = chr(nomb_code+65)  # On repasse aux lettres
        message_code.append(lettre_code)     # On ajoute la lettre codÃ©e au message

    message_code = "".join(message_code)     # On revient Ã  une chaine de caractÃ¨re
    return(message_code)


def decode_cesar_bis(mot,n):
    return cesar_bis(mot,-n)

def attaque_cesar_bis(mot):
    for n in range(26):
        print(decode_cesar_bis(mot,n) + "\n")
    return None
