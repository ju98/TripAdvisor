# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:44:50 2019

@author: dupouyj
"""

from urllib.request import urlopen
import bs4 as BeautifulSoup



class Trip:
    def __init__(self, url):
        self.url = url
    
    
    def getSoup(self):
        '''
            Récupère le code source d'une page web
        '''
        html = urlopen(self.url)
        return BeautifulSoup.BeautifulSoup(html,'html.parser')
    
    
    
    def getCom(self):
        '''
            Retourne la liste des commentaires sur une page
        '''
        commentaires = []
        com = self.getSoup().findAll("q", {"class" : "hotels-review-list-parts-ExpandableReview__reviewText--3oMkH"})  # on recupère les commentaires dans le code source
        
        for i in range(5): # 5 commentaires par page
            #print(str(com[i]).split(">")[2][:-6],"\n")
            commentaires.append(str(str(com[i]).split(">")[2][:-6]))
        
        return commentaires
    
    
    
    def getProfiles(self):
        '''
            Retourne la liste des profils qui ont fait un commentaire sur une page
        '''
        profiles = []
        prof = self.getSoup().findAll("a", {"class" : "ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC"}) # on recupère les profils dans le code source
        for i in range(5): # 5 commentaires par page
            #◘print(str(str(prof[i]).split("\"")[-1][1:-4]));
            profiles.append(str(str(prof[i]).split("\"")[-1][1:-4]))
            
        return profiles
        
    
        
    def getReviews(self):
        '''
            Retourne une liste de dictionnaires contenant le profil de celui qui a commenté et son commentaire
        '''
        com = []
        for i in range(5):  # 5 commentaires par page
            dic = {}
            dic["profile"]=self.getProfiles()[i]
            dic["commentaire"]=self.getCom()[i]
            com.append(dic)
            #print(dic,"\n\n")
        return com
    
    
    
    def getMaxPages(self):
        '''
            Retourne le nombre maximum de pages
        '''
        ref = self.getSoup().findAll("a", {"class" : "pageNum "}) # on récupère le nombre de pages dans le code source
        return int(str(ref[-1]).split(">")[-2][:3])
    
    
    
    def getUrlNextPage(self,n):
        '''
            Retourne l'url de la page de commentaires numéro n
            /!\ sur une page, on a que l'url de certaines pages. Exemple pour la page 1 : url des pages 1-2-3-4-255.
        '''
        ref = self.getSoup().findAll("a", {"class" : "pageNum "})
        
        for i in range(len(ref)):
            if str(ref[i]).split("\"")[-1][1] == str(n):
                nextUrl = str(ref[i]).split("\"")[3]
                return str(nextUrl)
    
    
    def getUrl(self, n):
        '''
            Retourne l'url de la page numero n 
        '''
        url_page2 = str(self.getUrlNextPage(2)) # url de la page 2, en supposant qu'in est sur la page 1
        
        url_part1 = "https://www.tripadvisor.fr" + str(url_page2)[:40] # 1ere partie de l'url
        url_part2 = str(url_page2)[-74:] # 2eme partie de l'url
        
        return str(url_part1) + str(n*5) + str(url_part2)


# =============================================================================
# 
# =============================================================================
if __name__ == "__main__" :
    
    filename = "reviews.txt"
    file = open(filename, "a")      # ouverture du fichier en mode "append"


    trip1 = Trip("https://www.tripadvisor.fr/Hotel_Review-g187259-d487533-Reviews-Golden_Tulip_Aix_Les_Bains-Aix_les_Bains_Savoie_Auvergne_Rhone_Alpes.html")
    
    
    # ecriture des commentaires de la premiere page
    for i in trip1.getReviews():
        file.write(str(i) + "\n")



    for j in range(2, trip1.getMaxPages()):  #on parcourre toutes les pages
        url = trip1.getUrl(j)
        trip = Trip(url) # creation de l'objet Trip
        for i in trip.getReviews():  # on parcourre les commentaires sur la page et les écrit dans un fichier texte
            file = open(filename, "a")
            file.write(str(i) + "\n")      
        print(j, " ok\n")
    

    file.close()

    print("tout est ok!!\n")