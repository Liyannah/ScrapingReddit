# coding: utf-8

import geocoder
import json
import en_core_web_sm
nlp = en_core_web_sm.load()

f = open('scraping.json')
scraping_data = json.load(f)
f.close()

title = scraping_data["title"]
url = scraping_data["url"]
ind = scraping_data["id"]
coord = {}
i = 0

for index in title:
    descrpt = title[index]
    url_img = url[index]
    id_post = ind[index]
    sentence = nlp(descrpt)
    sent = ([(X.text, X.label_) for X in sentence.ents])
    coord["coord"+index] = []

    for association in sent:
#        if association[1] == 'GPE':
        g = geocoder.geonames(association[0], key="liyanna")
        if g.geonames_id != None:
            place = geocoder.geonames(g.geonames_id, method="details", key="liyanna")
            coord["coord"+index].append({})
            coord["coord"+index][-1]["lieu"] = association[0]
            coord["coord"+index][-1]["lat"] = place.lat
            coord["coord"+index][-1]["lon"] = place.lng
            coord["coord"+index][-1]["des"] = descrpt
            coord["coord"+index][-1]["url"] = url_img
            coord["coord"+index][-1]["id"] = id_post
            
    
final_file = json.dumps(coord, indent = 2)
f = open("coord.json","w")
f.write(final_file)
f.close()   