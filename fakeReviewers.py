# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:17:06 2019

@author: dupouyj
"""

from urllib.request import urlopen
import bs4 as BeautifulSoup
from similarity.normalized_levenshtein import NormalizedLevenshtein


bad_char=[",",";",".",":",'!']
def remove_bad_chars(string,bad_char):
    for char in bad_char:
        string=string.replace(char,"")
    return string

def cleaned_reviews(listOfReviews):
    for reviewer in listOfReviews:
        reviewer["commentaire"]=remove_bad_chars(reviewer["commentaire"],bad_char)
    return listOfReviews
           
chaine = [{'profile': 'Nielpi', 'commentaire': 'Chambre supérieure calme  avec acces spa. Spa complet et inégalable.  Attends avec impatience  la fin des travaux pour profiter  pleinement du bar et du restaurant. Réception cordiale. Idéalement  situé, près  de la gare.'} ,{'profile': 'nadia', 'commentaire': "Nous avons séjourné le week end dernier et vraiment une belle experience la dame de l'accueil vraiment super,  La chambre très propre grande et le plateau de bienvenue fait plaisir,  Nous avons pu profiter du spa durant 3h30 l'après midi très bien il est grand et nous avons pu"},{'profile': 'Passport15213414595', 'commentaire': "Nous avons séjourné le week end dernier et vraiment une belle experience la dame de l'accueil vraiment super,  La chambre très propre grande et le plateau de bienvenue fait plaisir,  Nous avons pu profiter du spa durant 3h30 l'après midi très bien il est grand et nous avons pu"} ]


normalized_levenshtein = NormalizedLevenshtein()
def same_comment(cleanedReviews):
    fakeReviews=[]
    for review in cleanedReviews:
        nb_similarity = 0
        testReviews=[i for i in cleanedReviews if i != 'review']
        if(len(testReviews)>1):
            for test in testReviews:
                if(normalized_levenshtein.distance(review["profile"], test["profile"])>0.5):
                    nb_similarity+=1
        if nb_similarity>20 :
            fakeReviews.append(review)
    return fakeReviews
    
        
        #test

fakeReviews=[]
cleanedReviews=cleaned_reviews(chaine)
fakeReviews=same_comment(cleanedReviews)
print(fakeReviews)

    #une personne avec différents commentaires
    
