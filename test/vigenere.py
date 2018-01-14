#!/usr/bin/python3
# -*- coding: utf-8 -*-

import functions_misc
import functions_cesar
import os
import webbrowser
import urllib2
from lxml import html
import requests

## Vrai code


# Chiffrement de VigenÃ¨re (pour un mot ou une phrase)
# cle est la liste [n_1,n_2,...,n_k]
def vigenere_bis(mot,cle):
    message_code = []
    k = len(cle)                             # longueur de la clÃ©
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


# DÃ©chiffrement de VigenÃ¨re (pour un mot ou une phrase)
def decode_vigenere_bis(mot,cle):
    return vigenere_bis(mot,[-n for n in cle])

# Exemple
mot_clair = "Jadore ecouter la radio toute la journee"
cle = "musique"
cle_liste = []


cle=cle.upper()

for lettre in cle:
    cle_liste.append(ord(lettre))


mot_clair = mot_clair.upper()

mot_code = vigenere_bis(mot_clair,cle_liste)
mot_code = mot_code.upper()
print("mot clair : " + mot_clair)
print("cle : " + cle)
print("mot code : " + mot_code)

mot_decode = decode_vigenere_bis(vigenere_bis(mot_clair,cle_liste), cle_liste)
print mot_decode
