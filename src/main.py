#!/usr/bin/python3
# -*- coding: utf-8 -*-

import functions_misc
import functions_cesar
import functions_vigenere
import signal
import urllib2
import sys

def lireFichier(nom_fichier):
    try:
        fichier = open("../a_analyser/"+nom_fichier,'r')
        contenu = fichier.read()
        print contenu
        fichier.close()
    except Exception as e:
        print("Ce fichier n'existe pas..")
        exit()

try:
    while True :
        est_html = False
        est_txt = False
        est_premier = False

        print("\n\n----- .: DECODER 3000 :. -----\n")
        print("Vous souhaitez :")
        print("1. Decoder un fichier html")
        print("2. Decoder un fichier texte stocké sur votre disque dur")

        reponse = raw_input("\nFaites un choix : ")
        if reponse == '1':
            url = raw_input("Indiquez l'url complete du fichier html à analyser : \n")
            est_html = True
        if reponse == '2':
            est_txt = True
            print("Avant de continuer, déplacez le fichier que vous souhaitez analyser dans le dossier 'a_analyser'")
            nom_fichier = raw_input("Indiquez le nom du fichier et son extension : ")
            print("\nVous avez décidé d'analyser le contenu suivant : \n")
            lireFichier(nom_fichier)


        if est_html == True:
            try:
                print(urllib2.urlopen(url).read())
            except Exception as e:
                print("Ce n'est pas une url valide !")

        if est_txt == True:
            print("--- FONCTIONS DISPONIBLES ---")
            print("1. Décoder avec Cesar")
            print("2. Décoder avec Vigenere")
            print("3. Décoder selon l'encodage du texte")
            print("4. Décoder selon les nombres")


            reponse = raw_input("Faites un choix : ")
            if reponse == "1":
                print("\nVous avez choisi le décodage par Cesar")
                reponse = raw_input("Connaissez-vous le décalage ? O/N : ")
                if reponse == 'O':
                    decalage = raw_input("Donnez la valeur du décalage : ")
                    decalage = int(decalage)
                    fichier = open("../a_analyser/"+nom_fichier,'r')
                    contenu = fichier.read().replace(" ","")
                    contenu = contenu.strip().upper()
                    print("Le message décodé est : ")
                    print(functions_cesar.decode_cesar_bis(contenu, decalage))
                    fichier.close()

                else :
                    print("Le programme va effectuer une analyse brute pour tenter de déchiffrer le code\n\n")
                    fichier = open("../a_analyser/"+nom_fichier,'r')
                    contenu = fichier.read().replace(" ","")
                    contenu = contenu.strip()
                    functions_cesar.attaque_cesar_bis(contenu)
                    fichier.close()
                    print("\n")

            if reponse == "2":
                print("\nVous avez choisi le décodage par Vigenere")
                fichier = open("../a_analyser/"+nom_fichier,'r')
                contenu = fichier.read()
                contenu = contenu.upper()
                print(contenu)
                cle = raw_input("Donnez la cle du message codé : ")
                cle_liste = []
                for lettre in cle:
                    cle_liste.append(ord(lettre))
                print cle_liste
                mot_decode = functions_vigenere.decode_vigenere_bis(contenu, cle_liste)
                print("\n"+mot_decode)
                fichier.close()

            if reponse == "3":
                print("\nVous avez choisi le decodage selon l'encodage")

                fichier = open("../a_analyser/"+nom_fichier,'r')
                contenu = fichier.read()
                contenu = contenu.strip()
                carac_concatener = ""
                est_latin1 = False

                try:
                    for carac in contenu:
                        if carac != " ":
                            carac_concatener = carac_concatener + carac
                        if carac == " ":
                            if (int(carac_concatener) >= 0) and (int(carac_concatener) <= 255):
                                est_latin1 = True
                            carac_concatener = ""
                except Exception as e:
                    est_latin1 = False
                fichier.close()

                if est_latin1 == True:
                        print("Votre chaine est encodée en Latin-1")
                        print("Voici le message décodé\n\n")
                        fichier = open("../a_analyser/"+nom_fichier,'r')
                        contenu = fichier.read()
                        contenu = contenu.strip()

                        carac_concatener = ""
                        message = ""
                        for carac in contenu:
                            if carac != " ":
                                carac_concatener = carac_concatener + carac
                            if carac == " ":
                                try:
                                    carac_concatener = int(carac_concatener)
                                    message = message + unichr(carac_concatener)
                                    carac_concatener = ""
                                except Exception as e:
                                    pass

                        print(message)
                        fichier.close()
                else :
                    print("Votre message est encodé en Unicode")
                    print("Voici le message décodé\n\n")
                    fichier = open("../a_analyser/"+nom_fichier,'r')
                    contenu = fichier.read()
                    contenu = contenu.strip()
                    print(contenu.replace(" ", "")).decode('hex')

            if reponse == '4':
                print("Vous avez choisi le décodage par les nombres\n")
                fichier = open("../a_analyser/"+nom_fichier,'r')
                contenu = fichier.read()
                contenu = contenu.strip()
                carac_concatener = ""
                for carac in contenu:
                    if carac != " ":
                        carac_concatener = carac_concatener + carac
                    if carac == " ":
                        try:
                            carac_concatener = int(carac_concatener)
                            if functions_misc.is_prime(carac_concatener):
                                est_premier = True
                            else:
                                est_premier = False
                            carac_concatener = ""
                        except Exception as e:
                            pass

                if est_premier == True:
                    print("Votre message est encodé selon les chiffres premiers")
                    message_decode = ""
                    rel_nombre_lettre = {} #Dictionnaire qui associe le nombre premier à la lettre
                    id_lettre_maj = 65 #On commence par la lettre A de la table ascii
                    prime_number = 0
                    nb_lettre_associe = 0 #Compteur d'association des lettres
                    carac_concatener = ""

                    #On va associer à chaque lettre, un nombre premier
                    while nb_lettre_associe < 26:
                        if functions_misc.is_prime(prime_number):
                            rel_nombre_lettre[prime_number] = chr(id_lettre_maj)
                            nb_lettre_associe = nb_lettre_associe + 1
                            id_lettre_maj = id_lettre_maj + 1
                        prime_number = prime_number + 1

                    #On va lire le texte de nombre premier et récupérer dans le dictionnaire la lettre associé au dictionnaire
                    for carac in contenu:
                        if carac != " ":
                            carac_concatener = carac_concatener + carac
                        if carac == " ":
                            carac_concatener = int(carac_concatener)
                            message_decode = message_decode + rel_nombre_lettre[carac_concatener] + " "
                            carac_concatener = ""
                    print("Voici le message décodé\n" + message_decode)
                    fichier.close()

                else:

                    # Cet algo sans nom décrypte la chaine codé de la façon suivante:
                    # message en clair : Alexandre
                    # message codé : A1 l2 e3 x4 a5 n6 d7 r8 e9
                    # message décodé : A l e x a n d r e
                    # On a juste à retirer les nombres
                    fichier = open("../a_analyser/"+nom_fichier,'r')
                    contenu = fichier.read()
                    contenu = contenu.strip()
                    message_decode = ""
                    est_chiffre = False

                    for carac in contenu:
                        try:
                            carac = int(carac)
                            est_chiffre = True
                        except Exception as e:
                            est_chiffre = False

                        if est_chiffre == False:
                            message_decode = message_decode + carac
                    print("Voici le message décodé\n" + message_decode)



except KeyboardInterrupt as e:
    print("\nA bientôt !")
