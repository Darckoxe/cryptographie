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

def decode_vigenere_perso(mot, cle): #cle est une string
    # listes
    mot_liste = []
    cle_liste = []
    lettre_decode_liste = []
    # pré-traitement
    mot = mot.replace(" ","")
    mot = mot.replace("é","e")
    mot = mot.replace("è","e")
    mot = mot.replace("ê","e")
    mot = mot.replace("à","a")
    mot = mot.replace("'","")
    mot = mot.replace(";","")
    mot = mot.replace(".","")
    mot = mot.replace(",","")
    mot = mot.replace("?","")
    mot = mot.replace("!","")
    mot = mot.replace(":","")
    mot = mot.replace("/","")
    mot = mot.replace("\\","")
    mot = mot.strip()
    mot = mot.upper()
    cle = cle.upper()
    # alphabet
    alphabet = {}
    # itérateurs
    i = 0;
    j = 0;
    rang_liste = 0
    # autres
    mot_decode = ""
    id_lettre = 65

    while i < 26:
        alphabet[i] = chr(id_lettre)
        i = i+1;
        id_lettre = id_lettre+1

    for lettre in mot:
        mot_liste.append(ord(lettre))

    for lettre_cle in cle:
        cle_liste.append(ord(lettre_cle))

    for lettre_cour in mot_liste:
        if((lettre_cour - cle_liste[rang_liste]) >= 0):
            lettre_decode = lettre_cour - cle_liste[rang_liste]
            lettre_decode = alphabet[lettre_decode]
            lettre_decode_liste.append(lettre_decode)
        else:
            lettre_decode = lettre_cour - cle_liste[rang_liste] + 26
            lettre_decode = alphabet[lettre_decode]
            lettre_decode_liste.append(lettre_decode)

        if rang_liste == len(cle_liste) - 1:
            rang_liste = 0
        else :
            rang_liste = rang_liste + 1

    mot_decode=mot_decode.join(lettre_decode_liste)
    return mot_decode
