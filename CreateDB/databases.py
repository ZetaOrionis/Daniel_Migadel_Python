#!/usr/bin/python3
#-*- coding: utf-8 -*-
import json
from pprint import pprint
import mysql.connector

def createConnection() :
    conn = mysql.connector.connect(host="localhost",user="root",password="", database="installations_sportives")
    cursor = conn.cursor()
    return (conn,cursor)

def closeConnection(conn) :
    conn.commit()
    conn.close()

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
        codePostal int DEFAULT NULL,
        commune  varchar(100) DEFAULT NULL,
        PRIMARY KEY(installationId),
        FOREIGN KEY (coordId) REFERENCES Coordonnes(coordId)
    );
    """)

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

def insertInstallation(cursor,installation) :
    cursor.execute("""INSERT INTO test(installationId,latitude,longitude,name,noVoie,libelleVoie,codePostal,commune) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",installation)

def insertIgnoreCoord(cursor, coord) :
    cursor.execute("""INSERT IGNORE INTO coordonnes (latitude,longitude) VALUES (%s,%s)""",coord)


def selectLocationDistance(cursor,distance,latitude,longitude) :
    latitude = str(latitude)
    longitude = str(longitude)
    distance = str(distance)
    formule="(6366*acos(cos(radians("+latitude+"))*cos(radians(`latitude`))*cos(radians(`longitude`)-radians("+longitude+"))+sin(radians("+latitude+"))*sin(radians(`latitude`))))"
    sql="SELECT coordId,"+formule+"AS dist FROM coordonnes WHERE"+formule+"<="+distance+" ORDER by dist ASC";
    cursor.execute(sql)
    rows = cursor.fetchall()

    return rows

def searchInstallation(cursor,latitude,longitude,distance) :
    latitude = str(latitude)
    longitude = str(longitude)
    distance = str(distance)

    sql="SELECT name,noVoie,libelleVoie"+formule+"AS dist FROM coordonnes c,test t WHERE"+formule+"<="+distance+" and c.coordId=t.coordId ORDER by dist ASC";
    cursor.execute(sql)
    rows = cursor.fetchall()

    return rows
