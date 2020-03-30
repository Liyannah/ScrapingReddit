# coding: utf-8

import geocoder
import json
import en_core_web_sm
nlp = en_core_web_sm.load()

#open the reddit data
with open("scraping.json") as input_file:
          scraping_data = json.load(input_file)

#var initialization
title = scraping_data["title"]
url = scraping_data["url"]
ind = scraping_data["id"]
coord = {}
i = 0

#treatment of every title
for index in title:
    descrpt = title[index]
    url_img = url[index]
    id_post = ind[index]
    sentence = nlp(descrpt)
#selection of the named entities
    sent = ([(X.text, X.label_) for X in sentence.ents])
    if len(sent) != 0:
        coord["coord"+index] = []

#geolocalisation of the named entities found
        for association in sent:
            if association[1] not in ('DATE', 'TIME', 'PERCENT', 'MONEY', 'QUANTITY', 'ORDINAL', 'CARDINAL') :
                g = geocoder.geonames(association[0], key="liyanna")
                if g.geonames_id is not None:
                    place = geocoder.geonames(g.geonames_id, method="details", key="liyanna")
                    coord["coord"+index].append({})
                    coord["coord"+index][-1]["lieu"] = association[0]
                    coord["coord"+index][-1]["lat"] = place.lat
                    coord["coord"+index][-1]["lon"] = place.lng
                    coord["coord"+index][-1]["des"] = descrpt
                    coord["coord"+index][-1]["url"] = url_img
                    coord["coord"+index][-1]["id"] = id_post
            
    
final_file = json.dumps(coord, indent = 2)
with open("coord.json","w") as output_file:
    output_file.write(final_file)
