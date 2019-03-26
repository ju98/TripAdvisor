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
        html = urlopen(self.url)
        return BeautifulSoup.BeautifulSoup(html,'html.parser')
    
    
    def getCom(self):
        commentaires = []
        com = self.getSoup().findAll("q", {"class" : "hotels-hotel-review-community-content-review-list-parts-ExpandableReview__reviewText--2OVqJ"})
        for i in range(5):
            #print(str(com[i]).split(">")[2][:-6],"\n")
            commentaires.append(str(str(com[i]).split(">")[2][:-6]))
        return commentaires
    
    
    
    def getProfiles(self):
        profiles = []
        ref = self.getSoup().findAll("div", {"class" : "page"})
        prof = ref[0].findAll("a", {"class" : "ui_header_link social-member-MemberEventOnObjectBlock__member--23Flv"})
        for i in range(5):
            profiles.append(str(str(prof[i]).split("\"")[-1][1:-4]))
        return profiles
        
        
    def getReviews(self):
        com = []
        for i in range(5):  # 5 commentaires par page
            dic = {}
            dic["profile"]=self.getProfiles()[i]
            dic["commentaire"]=self.getCom()[i]
            com.append(dic)
            #print(dic,"\n\n")
        return com
    
    def getMaxPages(self):
        ref = self.getSoup().findAll("a", {"class" : "pageNum "})
        return int(str(ref[-1]).split(">")[-2][:3])
    
    def getUrlNextPage(self,n):
        ref = self.getSoup().findAll("a", {"class" : "pageNum "})
        for i in range(len(ref)):
            if str(ref[i]).split("\"")[-1][1] == str(n):
                nextUrl = str(ref[i]).split("\"")[3]
                return str(nextUrl)
    
    def getUrl(page):
        pass


# =============================================================================
# 
# =============================================================================
if __name__ == "__main__" :
    
    filename = "reviews.txt"
    file = open(filename, "a")      # ouverture du fichier en mode "append"


    trip1 = Trip("https://www.tripadvisor.fr/Hotel_Review-g187259-d487533-Reviews-Golden_Tulip_Aix_Les_Bains-Aix_les_Bains_Savoie_Auvergne_Rhone_Alpes.html")
    
#    for i in trip1.getReviews():
#        file.write(str(i) + "\n")



    url_page2 = str(trip1.getUrlNextPage(2))
    url_part1 = "https://www.tripadvisor.fr" + str(url_page2)[:40]
    url_part2 = str(url_page2)[-74:]
    
    trip2 = Trip("https://www.tripadvisor.fr" + url_page2)
    
#    for i in trip2.getReviews():
#        file.write(str(i) + "\n")


    for j in range(28, 100):
        url = str(url_part1) + str(j*5) + str(url_part2)
        trip = Trip(url)
        for i in trip.getReviews():
            file = open(filename, "a")
            file.write(str(i) + "\n")
            file.close()
        print(j, " ok\n")
    



    print("ok\n")