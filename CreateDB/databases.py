#!/usr/bin/python3
#-*- coding: utf-8 -*-
# import db.config
import json
from pprint import pprint
import mysql.connector

#création de la table installation
#elle contient divers informations sur les installations sportive des Pays de La loire
def newDatabaseInstallation(cursor) :
    cursor.execute("""
    DROP TABLE IF EXISTS Installation;
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Installation (
        installationId int NOT NULL,
        coordId int NOT NULL,
        name varchar(100) DEFAULT NULL,
        noVoie varchar(50) DEFAULT NULL,
        libelleVoie  varchar(100) DEFAULT NULL,
        codePostal varchar(100) DEFAULT NULL,
        commune  varchar(100) DEFAULT NULL,
        PRIMARY KEY(installationId),
        FOREIGN KEY (coordId) REFERENCES Coordonnes(coordId)
    );
    """)

#création de la table Coordonnes
#relative aux cooordonnées (lat et long) des installations sportives
def newDatabaseCoord(cursor) :
    cursor.execute("""
    DROP TABLE IF EXISTS Coordonnes;
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Coordonnes (
        coordId int NOT NULL AUTO_INCREMENT,
        latitude DECIMAL(10,6) NOT NULL,
        longitude DECIMAL(10,6) NOT NULL,
        PRIMARY KEY(coordId),
        UNIQUE(latitude,longitude)
    );
    """)

#suppression de l'ensemble des tables
#permet le nettoyage avant une mise à jour de la bdd
def dropAllTables(cursor) :
    cursor.execute("""
    DROP TABLE IF EXISTS Activite;
    """)

    cursor.execute("""
    DROP TABLE IF EXISTS Equipement;
    """)

    cursor.execute("""
    DROP TABLE IF EXISTS Installation;
    """)

    cursor.execute("""
    DROP TABLE IF EXISTS Coordonnes;
    """)

    cursor.execute("""
    DROP TABLE IF EXISTS EquipementType;
    """)

def insertInstallation(cursor,installation) :
    cursor.execute("""INSERT INTO Installation(installationId,latitude,longitude,name,noVoie,libelleVoie,codePostal,commune) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",installation)

def insertIgnoreCoord(cursor, coordonnes) :
    cursor.execute("""INSERT IGNORE INTO Coordonnes(latitude,longitude) VALUES (%s,%s)""",coordonnes)


def searchInstallation(cursor,latitude,longitude,distance) :
    latitude = str(latitude)
    longitude = str(longitude)
    distance = str(distance)

    sql="SELECT name,noVoie,libelleVoie"+formule+"AS dist FROM Coordonnes c,test t WHERE"+formule+"<="+distance+" and c.coordId=t.coordId ORDER by dist ASC";
    cursor.execute(sql)
    rows = cursor.fetchall()

    return rows
