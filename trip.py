# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:58:43 2019

@author: dupouyj
"""

from urllib.request import urlopen
import bs4 as BeautifulSoup


html = urlopen("https://www.tripadvisor.fr/Hotel_Review-g187259-d487533-Reviews-Golden_Tulip_Aix_Les_Bains-Aix_les_Bains_Savoie_Auvergne_Rhone_Alpes.html")
soup=BeautifulSoup.BeautifulSoup(html,'html.parser')

class Trip:
    def __init__(self, soup):
        self.soup = soup
    
    def getCom(self):
        return self.soup.findAll("q", {"class" : "hotels-hotel-review-community-content-review-list-parts-ExpandableReview__reviewText--2OVqJ"})
    
    def getProfiles(self):
        ref = self.soup.findAll("div", {"class" : "page"})
        return ref[0].findAll("a", {"class" : "ui_header_link social-member-MemberEventOnObjectBlock__member--23Flv"})
        
        
    def getReviews(self):
        com = []
        for i in range(len(self.getCom())):
            dic = {}
            dic["profile"]=str(self.getProfiles()[i]).split("\"")[-1][1:-4]
            dic["commentaire"]=str(self.getCom()[i]).split(">")[2][:-6]
            com.append(dic)
            #print(dic,"\n\n")
        return com
    
    def getMaxPages(self):
        ref = self.soup.findAll("a", {"class" : "pageNum "})
        return int(str(ref[-1]).split(">")[-2][:3])
    
    def getUrlNextPage(self,n):
        ref = self.soup.findAll("a", {"class" : "pageNum "})
        for i in range(len(ref)):
            if str(ref[i]).split("\"")[-1][1] == str(n):
                nextUrl = str(ref[i]).split("\"")[3]
                return nextUrl


# =============================================================================
# 
# =============================================================================
if __name__ == "__main__" :
    html = urlopen("https://www.tripadvisor.fr/Hotel_Review-g187259-d487533-Reviews-Golden_Tulip_Aix_Les_Bains-Aix_les_Bains_Savoie_Auvergne_Rhone_Alpes.html")
    soup=BeautifulSoup.BeautifulSoup(html,'html.parser')
    
    trip1 = Trip(soup)
    #print(trip1.getMaxPages())
    
#    nextUrl = trip1.getUrlNextPage(2)
#    html2 = urlopen("https://www.tripadvisor.fr/"+str(nextUrl))
#    soup2=BeautifulSoup.BeautifulSoup(html2,'html.parser')
#    trip2 = Trip(soup2)
#    #print(trip2.getReviews())
    
    def getAllReviews():
        reviews = []
        maxPages = trip1.getMaxPages()
        newTrip = trip1
        for i in range(2, 6):
            nextUrl = newTrip.getUrlNextPage(i)
            print(nextUrl,"\n\n")
            nextHtml = urlopen("https://www.tripadvisor.fr/"+str(nextUrl))
            nextSoup = BeautifulSoup.BeautifulSoup(nextHtml,'html.parser')
            nextTrip = Trip(nextSoup)
            reviews.append(nextTrip.getReviews())
            newTrip = nextTrip
        
        return reviews
    
    print(getAllReviews())