#!/usr/bin/python3
#-*- coding: utf-8 -*-
import json
from pprint import pprint
import config
import mysql.connector

def createConnection() :
    conn = mysql.connector.connect(host=config.HOST,user=config.USER,password=config.PASSWORD, database=config.BASE)
    cursor = conn.cursor()
    return (conn,cursor)

def closeConnection(conn) :
    conn.commit()
    conn.close()

def newDatabaseActivites(cursor) :
    cursor.execute("""
    DROP TABLE IF EXISTS Activite;
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Activite (
        activiteId int NOT NULL,
        activiteLib varchar(100) DEFAULT NULL,
        equipID int NOT NULL,
        PRIMARY KEY(activiteId,equipID),
        FOREIGN KEY (equipID) REFERENCES Equipement(equipID)
    );
    """)

def newDatabaseEquipementType(cursor) :
    cursor.execute("""
    DROP TABLE IF EXISTS EquipementType;
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS EquipementType (
        equipTypeCode int NOT NULL,
        equipTypeLib varchar(100) DEFAULT NULL,
        PRIMARY KEY(equipTypeCode)
    );
    """)

def newDatabaseEquipement(cursor) :
    cursor.execute("""
    DROP TABLE IF EXISTS Equipement;
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Equipement (
        equipID int NOT NULL,
        equNom varchar(100) DEFAULT NULL,
        equGpsX float NOT NULL,
        equGpsY float NOT NULL,
        equipTypecode int NOT NULL,
        installationId int NOT NULL,

        PRIMARY KEY(equipID),
        FOREIGN KEY (equipTypecode) REFERENCES EquipementType(equipTypeCode),
        FOREIGN KEY (installationId) REFERENCES Installation(installationId)
    );
    """)
#
# def newDatabaseCoord(cursor) :
#     cursor.execute("""
#     DROP TABLE IF EXISTS coordonnes;
#     """)
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS coordonnes (
#         coordId int NOT NULL AUTO_INCREMENT,
#         latitude DECIMAL(10,6) NOT NULL,
#         longitude DECIMAL(10,6) NOT NULL,
#         PRIMARY KEY(coordId),
#         UNIQUE(latitude,longitude)
#     );
#     """)

def insertEquipement(cursor,installation) :
    cursor.execute("""INSERT INTO test(installationId,latitude,longitude,name,noVoie,libelleVoie,codePostal,commune) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",installation)


def insertEquipementType(cursor,equipementType) :
    cursor.execute("""INSERT IGNORE INTO EquipementType(equipTypeCode,equipTypeLib) VALUES(%s,%s)""",equipementType)

def insertEquipement(cursor,equipement) :
    cursor.execute("""INSERT IGNORE INTO Equipement(equipID,equNom,equGpsX,equGpsY,equipTypecode,installationId) VALUES(%s,%s,%s,%s,%s,%s)""",equipement)

def insertActivite(cursor,activite) :
    cursor.execute("""INSERT IGNORE INTO Activite(activiteId,activiteLib,equipId) VALUES(%s,%s,%s)""",activite)






def selectLocationDistance(cursor,distance,latitude,longitude) :
    latitude = str(latitude)
    longitude = str(longitude)
    distance = str(distance)
    formule="(6366*acos(cos(radians("+latitude+"))*cos(radians(`e.equGpsY`))*cos(radians(`equGpsX`)-radians("+longitude+"))+sin(radians("+latitude+"))*sin(radians(`e.equGpsY`))))"
    sql="SELECT e.equipID,"+formule+"AS dist FROM Equipement e WHERE"+formule+"<="+distance+" ORDER by dist ASC";
    cursor.execute(sql)
    rows = cursor.fetchall()

    return rows

def searchInstallation(cursor,latitude,longitude,distance) :
    latitude = str(latitude)
    longitude = str(longitude)
    distance = str(distance)

    sql="SELECT name,noVoie,libelleVoie"+formule+"AS dist FROM Coordonnes c,test t WHERE"+formule+"<="+distance+" and c.coordId=t.coordId ORDER by dist ASC";
    cursor.execute(sql)
    rows = cursor.fetchall()

    return rows
