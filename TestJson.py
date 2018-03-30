import json
#https://pastebin.com/0EBRAtB7
#https://pastebin.com/2fNdVsEk
data_installation = json.load(open('res/data.fiche.installation.paysdelaloire.fr.json'))
data_activite = json.load(open('res/data.fiche.activite.paysdelaloire.fr.json'))
data_equipement = json.load(open('res/data.fiche.equipement.paysdelaloire.fr.json'))

bd_install = []
bd_ville = []
bd = []


for i in range(1, data_installation["nb_results"]) :
    bd_install.append(data_installation["data"][i]["geo"]["name"])
bd.append(bd_install)

for i in range(1, data_installation['nb_results']) :
    bd_ville.append(data_installation["data"][i]["ComLib"])
bd.append(bd_install)

print(bd)
