# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:14:09 2019

@author: dupouyj
"""

from urllib.request import urlopen
import bs4 as BeautifulSoup




html = urlopen("https://www.tripadvisor.fr/Hotel_Review-g187259-d487533-Reviews-Golden_Tulip_Aix_Les_Bains-Aix_les_Bains_Savoie_Auvergne_Rhone_Alpes.html")
soup=BeautifulSoup.BeautifulSoup(html,'html.parser')

ref = soup.findAll("a", {"class" : "pageNum "})
maxPages = int(str(ref[-1]).split(">")[-2][:3])
print(maxPages)

n=2
for i in range(len(ref)):
    if str(ref[i]).split("\"")[-1][1] == str(n):
        nextUrl = str(ref[i]).split("\"")[3]
        print(nextUrl)
        



#print(str(ref[0]).split("\"")[-1][1])  #on recupere le numéro du lien de la page
    
url_page2 = str(ref[0]).split("\"")[3]  #on recupere l'url de la page 2, se trouvant dans le code source de la page 1

html_p2 = urlopen("https://www.tripadvisor.fr/"+str(nextUrl))
soup_p2=BeautifulSoup.BeautifulSoup(html_p2,'html.parser')

commentaires=soup_p2.findAll("q", {"class" : "hotels-hotel-review-community-content-review-list-parts-ExpandableReview__reviewText--2OVqJ"})
print(commentaires)

refbis=soup.findAll("div", {"class" : "page"})
profiles=refbis[0].findAll("a", {"class" : "ui_header_link social-member-MemberEventOnObjectBlock__member--23Flv"})

print(profiles)

#com = []
#for i in range(len(commentaires)):
#    dic = {}
#    dic["profile"]=str(profiles[i]).split("\"")[-1][1:-4]
#    dic["commentaire"]=str(commentaires[i]).split(">")[2][:-6]
#    com.append(dic)
#    print(dic,"\n\n")