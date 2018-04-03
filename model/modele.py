import mysql.connector

""" Selection d'une installation précise dans une ville donnée """
""" Connection à la base de données """
"""query ="SELECT latitude,longitude FROM coordonnes c, installation i where c.CoordID = i.CoordID and i.commune = \""+ville+"\"";
"""
""" Afficher sous forme de tableau """
"""query = ("SELECT * from installation where commune LIKE \""+ville+"\"")"""
def rechercheInstallation(ville) :

    conn = mysql.connector.connect(host='localhost',user='root',password='',database='installations_sportives')
    cursor = conn.cursor()

    query = ("SELECT activiteLib, equNom, equipTypeLib, name, noVoie, libelleVoie, commune, latitude, longitude FROM installation i, activite a, equipement e, coordonnes c, equipementtype et where c.coordID = i.coordID and i.commune = \""+ville+"\" and a.equipID = e.equipID and e.equipTypecode = et.equipTypeCode and i.installationId = e.installationId")
    cursor.execute(query)

    rows = cursor.fetchall()
    return rows

    cursor.close()
    conn.close()

""" Selection d'une activitée précise dans une ville donnée """
def recherche(activite,ville) :

    """ Connection à la base de données """

    conn = mysql.connector.connect(host="localhost",user="root",password="",database="installations_sportives")
    cursor = conn.cursor()

    query = ("SELECT activiteLib, equNom, equipTypeLib, name, noVoie, libelleVoie, commune, latitude, longitude FROM installation i, activite a, equipement e, coordonnes c, equipementtype et where c.coordID = i.coordID and i.commune = \""+ville+"\" and a.equipID = e.equipID and activiteLib = \""+activite+"\" and e.equipTypecode = et.equipTypeCode and i.installationId=e.installationId")

    cursor.execute(query)

    """ Afficher sous forme de tableau """
    row = cursor.fetchall()
    return row


    cursor.close()
    conn.close()

""" Retourne toutes les activitées """
def rechercheActivites() :

    """ Connection à la base de données """

    conn = mysql.connector.connect(host="localhost",user="root",password="",database="installations_sportives")
    cursor = conn.cursor()

    query = ("SELECT * FROM activite")

    cursor.execute(query)

    """ Afficher sous forme de tableau """
    row = cursor.fetchall()
    return row


    cursor.close()
    conn.close()

def autocompletionville(ville) :
    conn = mysql.connector.connect(host="localhost",user="root",password="",database="installations_sportives")
    cursor = conn.cursor()

    commune = '%'+ville+'%'

    query = ("SELECT DISTINCT commune FROM installation where commune LIKE \'"+commune+"\'")

    cursor.execute(query)

    """ Afficher sous forme de tableau """
    row = cursor.fetchall()
    return row


    cursor.close()
    conn.close()

def autocompletionactivite(activite) :
    conn = mysql.connector.connect(host="localhost",user="root",password="",database="installations_sportives")
    cursor = conn.cursor()

    act = '%'+activite+'%'

    query = ("SELECT DISTINCT activiteLib FROM activite where activiteLib LIKE \'"+act+"\'")

    cursor.execute(query)

    """ Afficher sous forme de tableau """
    row = cursor.fetchall()
    return row


    cursor.close()
    conn.close()
