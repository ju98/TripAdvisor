# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:17:06 2019

@author: dupouyj
"""

from urllib.request import urlopen
import bs4 as BeautifulSoup




html = urlopen("https://www.tripadvisor.fr/Hotel_Review-g187259-d487533-Reviews-Golden_Tulip_Aix_Les_Bains-Aix_les_Bains_Savoie_Auvergne_Rhone_Alpes.html")
soup=BeautifulSoup.BeautifulSoup(html,'html.parser')

commentaires=soup.findAll("q", {"class" : "hotels-hotel-review-community-content-review-list-parts-ExpandableReview__reviewText--2OVqJ"})
#ref2=soup.findAll("a", {"class" : "ui_header_link social-member-MemberEventOnObjectBlock__member--23Flv"})
ref=soup.findAll("div", {"class" : "page"})
#commentaires_bis=ref3[0].findAll("q", {"class" : "hotels-hotel-review-community-content-review-list-parts-ExpandableReview__reviewText--2OVqJ"})
profiles=ref[0].findAll("a", {"class" : "ui_header_link social-member-MemberEventOnObjectBlock__member--23Flv"})


#print(str(profiles[4]).split("\"")[-1][1:-4])
#♠print(str(commentaires[0]).split(">")[2][:-6])


com = []
for i in range(len(commentaires)):
    dic = {}
    dic["profile"]=str(profiles[i]).split("\"")[-1][1:-4]
    dic["commentaire"]=str(commentaires[i]).split(">")[2][:-6]
    com.append(dic)
    print(dic,"\n\n")

#print(com)
