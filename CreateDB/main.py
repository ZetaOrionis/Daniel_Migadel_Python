#!/usr/bin/python3
#-*- coding: utf-8 -*-
import math
import json
import csv
import urllib.request
import dbEquip
import databases

print("Téléchargement en cours ...\n")


#on extrait les fichiers via les url sous format csv
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


connection, cursor = dbEquip.createConnection()

print("Connexion réussie ...\n")
print("Installation des tables ...\n")

#Initalisation de toutes les tables que nous allons les
databases.dropAllTables(cursor)
databases.newDatabaseCoord(cursor)
databases.newDatabaseInstallation(cursor)

dbEquip.newDatabaseEquipementType(cursor)
dbEquip.newDatabaseEquipement(cursor)

dbEquip.newDatabaseActivites(cursor)


#on lit le fichier instaalation
f = open("../res/installations.csv")
reader = csv.DictReader(f)
data = [row for row in reader]

for row in data :

    coordonnes = (row["Latitude"],row["Longitude"])
    databases.insertIgnoreCoord(cursor,coordonnes)
    cursor.execute("""SELECT coordId FROM Coordonnes where latitude=%s AND longitude=%s""",coordonnes)
    id = cursor.lastrowid
    result = cursor.fetchone()
    #on retient l'id des coordonnées pour ensuite l'insérer dans la table installation
    print(row["Numéro de l'installation"])
    print(row["Nom usuel de l'installation"])

    installation = (row["Numéro de l'installation"],result[0],row["Nom usuel de l'installation"],
    row["Numero de la voie"],row["Nom de la voie"],row["Code postal"],row["Nom de la commune"])
    cursor.execute("""INSERT INTO Installation(installationId,coordId,name,noVoie,libelleVoie,codePostal,commune) VALUES(%s,%s,%s,%s,%s,%s,%s)""",installation)


#on lit le fichier equipements
#on fixe le délimiteur ;
f = open("../res/equipements.csv")
reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_NONE)
data = [row for row in reader]

for row in data:
    equipementType = [row["EquipementTypeCode"],row["EquipementTypeLib"]]
    equipement = [row["EquipementId"],row["EquNom"],row["EquGpsX"],row["EquGpsY"],row["EquipementTypeCode"],row["InsNumeroInstall"]]

    #on insère les typles dans EquipementType et Equipemet
    print(str(equipementType))
    dbEquip.insertEquipementType(cursor,equipementType)
    print(str(equipement))
    dbEquip.insertEquipement(cursor,equipement)


#on lit le fichier activites et on le réécrit dans un autre (remplacement des guillemets)
#on fixe le délimiteur ;
with open('../res/activites.csv', 'r') as f, open('../res/activites1.csv', 'w') as fo:
    for line in f:
        fo.write(line.replace('"', ''))

f = open("../res/activites1.csv")
reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_NONE)
data = [row for row in reader]
for row in data:
    activite = [row["ActCode"],row["ActLib"],row["EquipementId"]]
    print(str(activite))
    dbEquip.insertActivite(cursor,activite)


#on supprimer les tuples ayant activitID = 0 car le fichier csv a des données inutiles
dbEquip.deleteActiviteVide(cursor)

#oon ferme la connexion
dbEquip.closeConnection(connection)
