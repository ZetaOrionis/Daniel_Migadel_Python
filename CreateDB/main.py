#!/usr/bin/python3
#-*- coding: utf-8 -*-
from databases import *
from dbEquip import *
#from parseData import *
import math

print("Allo le monde\n")
#url = "http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-installations"
#url = str(input())

data = json.load(open('../res/install.data.paysdelaloire.fr.json'))
data_1 = json.load(open('../res/equip.data.paysdelaloire.fr.json'))
data_2 = json.load(open('../res/equi_activites_tabledata.paysdelaloire.fr.json'))
#pprint(data)

connection, cursor = createConnection()
#cursor.execute("""
#CREATE TABLE IF NOT EXISTS installations (
#    id int(6) NOT NULL AUTO_INCREMENT,
#    num int(5) DEFAULT NULL,
#    libelleVoie  varchar(50) DEFAULT NULL,
#    num2 int(5) DEFAULT NULL,
#    PRIMARY KEY(id)
#);
#""")

#data
newDatabaseInstallation(cursor)
newDatabaseCoord(cursor)

#data_1
newDatabaseEquipementType(cursor)
newDatabaseEquipement(cursor)

#data_2
newDatabaseActivites(cursor)

for i in data["data"]:
    coordonnees = [i["Latitude"],i["Longitude"]]

    #cursor.execute("""INSERT INTO Coordonnes(latitude,longitude) VALUES(%s,%s)""",coordonnees)
    insertIgnoreCoord(cursor,coordonnees)
    cursor.execute("""SELECT coordId FROM coordonnes where latitude=%s AND longitude=%s""",coordonnees)
    id = cursor.lastrowid
    row = cursor.fetchone()
    print(row[0])
    installation = [i["InsNumeroInstall"],row[0],i["geo"]["name"],
    i["InsNoVoie"],i["InsLibelleVoie"],i["InsCodePostal"],i["ComLib"]]
    cursor.execute("""INSERT INTO Installation(installationId,coordId,name,noVoie,libelleVoie,codePostal,commune) VALUES(%s,%s,%s,%s,%s,%s,%s)""",installation)

for a in data_1["data"]:
    equipementType = [a["EquipementTypeCode"],a["EquipementTypeLib"]]
    equipement = [a["EquipementId"],a["EquNom"],a["EquipementTypeCode"],a["InsNumeroInstall"]]
    print(str(equipementType))
    insertEquipementType(cursor,equipementType)
    print(str(equipement))
    insertEquipement(cursor,equipement)

for b in data_2["data"]:
    activite = [b["ActCode"],b["ActLib"],b["EquipementId"]]
    print(str(activite))
    insertActivite(cursor,activite)

# latitude = math.radians(47.075698)
# longitude = math.radians(-1.400693)
# lat = math.radians(46.333078)
# long = math.radians(-1.304158)
#
# a = math.cos(latitude)*math.cos(latitude)*math.cos(longitude-longitude)
# b = math.sin(latitude)*math.sin(latitude)
# c = math.acos(a+b)
# d = 6366*c
# print(str(a))
# print(str(b))
# print(str(c))
# print(str(d))
#
# print(str(latitude))
# print(str(longitude))
# f = 6366*math.acos(math.cos(latitude)*math.cos(lat)*math.cos(long-longitude)+math.sin(latitude)*math.sin(lat))

#print("Formule calculée -- >"+str(f))
rows = selectLocationDistance(cursor,20,47.075698,-1.40069)
print(rows)

#    print(i["InsNoVoie"])
#    print(i["InsLibelleVoie"])
#    print(i["InsCodePostal"])
closeConnection(connection)
#print("url"+url+"\n")
#print("data[InsLibelleVoie] = "+str(data["data"][0]["InsLibelleVoie"]))

#http://apprendre-python.com/page-database-data-base-donnees-query-sql-mysql-postgre-sqlite
