#!/usr/bin/python3
#-*- coding: utf-8 -*-
from databases import *
from dbEquip import *
import math
import json
import csv
import urllib.request

print("Allo le monde\n")
#url = "http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-installations"
#url = str(input())

csvInstallation = urllib.request.urlopen("http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=csv")
csvInstallationOld = open("../res/installations.csv","w")
csvInstallationOld.write(csvInstallation.read().decode("utf-8"))
csvInstallation.close()
csvInstallationOld.close()

csvEquipement = urllib.request.urlopen("http://data.paysdelaloire.fr/fileadmin/data/datastore/rpdl/sport/23440003400026_J336/equipements.csv")
csvEquipementOld = open("../res/equipements.csv","w")
csvEquipementOld.write(csvEquipement.read().decode("iso8859_1").encode('utf8').decode('utf-8'))
csvEquipement.close()
csvEquipementOld.close()

csvActivite = urllib.request.urlopen("http://data.paysdelaloire.fr/fileadmin/data/datastore/pdl/PLUS15000/J334_equipements_activites.csv")
csvActiviteOld = open("../res/activites.csv","w")
csvActiviteOld.write(csvActivite.read().decode("utf-8"))
csvActivite.close()
csvActiviteOld.close()

#
# data = json.load(open('../res/installations.json'))
# data_1 = json.load(open('../res/equipements.json'))
# data_2 = json.load(open('../res/activites.json'))




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
dropAllTables(cursor)

newDatabaseCoord(cursor)
newDatabaseInstallation(cursor)

#data_1
newDatabaseEquipementType(cursor)
newDatabaseEquipement(cursor)

#data_2
newDatabaseActivites(cursor)

# with open('../res/installations.csv') as f:
#     reader = csv.DictReader(f, delimiter=';')
#     for row in reader:
#         # latitude = row["Nom de la voie"]
#         # longitude = row["Longitude"]
#         print(row)
#         print(row[0])

f = open("../res/installations.csv")
reader = csv.DictReader(f)
data = [row for row in reader]

for row in data :
    print(row["Latitude"])
    print(row['Longitude'])
    coordonnes = (row["Latitude"],row["Longitude"])
    insertIgnoreCoord(cursor,coordonnes)
    cursor.execute("""SELECT coordId FROM Coordonnes where latitude=%s AND longitude=%s""",coordonnes)
    id = cursor.lastrowid
    result = cursor.fetchone()

    print(row["Numéro de l'installation"])
    print(row["Nom usuel de l'installation"])

    installation = (row["Numéro de l'installation"],result[0],row["Nom usuel de l'installation"],
    row["Numero de la voie"],row["Nom de la voie"],row["Code postal"],row["Nom de la commune"])
    cursor.execute("""INSERT INTO Installation(installationId,coordId,name,noVoie,libelleVoie,codePostal,commune) VALUES(%s,%s,%s,%s,%s,%s,%s)""",installation)


# f = open("../res/equipements.csv")
f = open("../res/equipements.csv")
reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_NONE)
data = [row for row in reader]

for row in data:
    equipementType = [row["EquipementTypeCode"],row["EquipementTypeLib"]]
    equipement = [row["EquipementId"],row["EquNom"],row["EquGpsX"],row["EquGpsY"],row["EquipementTypeCode"],row["InsNumeroInstall"]]

    print(str(equipementType))
    insertEquipementType(cursor,equipementType)
    print(str(equipement))
    insertEquipement(cursor,equipement)

with open('../res/activites.csv', 'r') as f, open('../res/activites1.csv', 'w') as fo:
    for line in f:
        fo.write(line.replace('"', ''))

f = open("../res/activites1.csv")
reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_NONE)
data = [row for row in reader]
for row in data:
    activite = [row["ActCode"],row["ActLib"],row["EquipementId"]]
    print(str(activite))
    insertActivite(cursor,activite)
# reader = csv.DictReader(f)
# data = [row for row in reader]
#
# for row in data :
#
# writer = csv.writer(open("../res/activites.csv", "wb"), quoting=csv.QUOTE_NONE)
# reader = csv.reader(open("../res/activites1.csv", "rb"), skipinitialspace=True)
# writer.writerows(reader)





print(["Latitude"])
print(["Longitude"])


# for i in data :
#     coordonnees = [i["Latitude"],i["Longitude"]]
#     print(i["Latitude"])
#     print(i["Longitude"])
#
#
#     #cursor.execute("""INSERT INTO Coordonnes(latitude,longitude) VALUES(%s,%s)""",coordonnees)
#     insertIgnoreCoord(cursor,coordonnees)
#     cursor.execute("""SELECT coordId FROM Coordonnes where latitude=%s AND longitude=%s""",coordonnees)
#     id = cursor.lastrowid
#     row = cursor.fetchone()
#     # print(row[0])
#
#     installation = [i["Numéro de l'installation"],row[0],i["Nom usuel de l'installation"],
#     i["Numero de la voie"],i["Nom de la voie"],i["Code postal"],i["Nom de la commune"]]
#     cursor.execute("""INSERT INTO Installation(installationId,coordId,name,noVoie,libelleVoie,codePostal,commune) VALUES(%s,%s,%s,%s,%s,%s,%s)""",installation)

# for a in data_1:
#     equipementType = [a[EquipementTypeCode],a["EquipementTypeLib"]]
#     equipement = [a["EquipementId"],a["EquNom"],a["EquGpsX"],a["EquGpsY"],a["EquipementTypeCode"],a["InsNumeroInstall"]]
#
#     # print(str(equipementType))
#     insertEquipementType(cursor,equipementType)
#     # print(str(equipement))
#     insertEquipement(cursor,equipement)
#
# for b in data_2["data"]:
#     activite = [b["ActCode"],b["ActLib"],b["EquipementId"]]
#     print(str(activite))
#     insertActivite(cursor,activite)

deleteActiviteVide(cursor)
# reader = csv.DictReader(f)
# data = [row for row in reader]
#
# for row in data :
#
# writer = csv.writer(open("../res/activites.csv", "wb"), quoting=csv.QUOTE_NONE)
# reader = csv.reader(open("../res/activites1.csv", "rb"), skipinitialspace=True)
# writer.writerows(reader)





print(["Latitude"])
print(["Longitude"])


# for i in data :
#     coordonnees = [i["Latitude"],i["Longitude"]]
#     print(i["Latitude"])
#     print(i["Longitude"])
#
#
#     #cursor.execute("""INSERT INTO Coordonnes(latitude,longitude) VALUES(%s,%s)""",coordonnees)
#     insertIgnoreCoord(cursor,coordonnees)
#     cursor.execute("""SELECT coordId FROM Coordonnes where latitude=%s AND longitude=%s""",coordonnees)
#     id = cursor.lastrowid
#     row = cursor.fetchone()
#     # print(row[0])
#
#     installation = [i["Numéro de l'installation"],row[0],i["Nom usuel de l'installation"],
#     i["Numero de la voie"],i["Nom de la voie"],i["Code postal"],i["Nom de la commune"]]
#     cursor.execute("""INSERT INTO Installation(installationId,coordId,name,noVoie,libelleVoie,codePostal,commune) VALUES(%s,%s,%s,%s,%s,%s,%s)""",installation)

# for a in data_1:
#     equipementType = [a[EquipementTypeCode],a["EquipementTypeLib"]]
#     equipement = [a["EquipementId"],a["EquNom"],a["EquGpsX"],a["EquGpsY"],a["EquipementTypeCode"],a["InsNumeroInstall"]]
#
#     # print(str(equipementType))
#     insertEquipementType(cursor,equipementType)
#     # print(str(equipement))
#     insertEquipement(cursor,equipement)
#
# for b in data_2["data"]:
#     activite = [b["ActCode"],b["ActLib"],b["EquipementId"]]
#     print(str(activite))
#     insertActivite(cursor,activite)

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
