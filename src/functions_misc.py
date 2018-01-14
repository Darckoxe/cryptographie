#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import string

def compterLettres(nomFichier):
    fichier = open("a_analyser/"+nomFichier, 'r')
    contenu = fichier.read()
    cpt=0
    for i in contenu:
        if i=="u":
            cpt=cpt+1
        else:
            pass
    print cpt

def analyseFreq():
    alphabet = string.ascii_letters
    print alphabet
    liste = [1,1,1]
    print liste

def frequences(chaine) :
    freq = [0] * 26
    for c in chaine:
        if c in string.ascii_uppercase:
            freq[ord(c) - ord('A')] += 1
    somme=sum(freq)
    freq=[v / somme * 1000.0 for v in freq]
    return freq

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    # print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True
