import mysql.connector

""" Recherche par ville """
def rechercheVille(ville) :

    """ Connection à la base de données """

    conn = mysql.connector.connect(host='localhost',user='root',password='',database='installations_sportives')
    cursor = conn.cursor()

    query = ("SELECT activiteLib, equNom, equipTypeLib, name, noVoie, libelleVoie, commune, latitude, longitude FROM installation i, activite a, equipement e, coordonnes c, equipementtype et where c.coordID = i.coordID and i.commune = \""+ville+"\" and i.installationId = e.installationId and a.equipID = e.equipID and e.equipTypecode = et.equipTypeCode")
    cursor.execute(query)

    """ Afficher sous forme de tableau """
    rows = cursor.fetchall()
    return rows

    cursor.close()
    conn.close()

""" Selection d'une activitée précise dans une ville donnée """
def rechercheVilleActivite(activite,ville) :

    """ Connection à la base de données """

    conn = mysql.connector.connect(host="localhost",user="root",password="",database="installations_sportives")
    cursor = conn.cursor()

    query = ("SELECT activiteLib, equNom, equipTypeLib, name, noVoie, libelleVoie, commune, latitude, longitude FROM installation i, activite a, equipement e, coordonnes c, equipementtype et where c.coordID = i.coordID and i.commune = \""+ville+"\" and a.equipID = e.equipID and a.activiteLib = \""+activite+"\" and e.equipTypecode = et.equipTypeCode and i.installationId=e.installationId")

    cursor.execute(query)

    """ Afficher sous forme de tableau """
    row = cursor.fetchall()
    return row


    cursor.close()
    conn.close()

""" Recherche par activitée """
def rechercheActivite(activite) :

    """ Connection à la base de données """

    conn = mysql.connector.connect(host="localhost",user="root",password="",database="installations_sportives")
    cursor = conn.cursor()

    query = ("SELECT activiteLib, equNom, equipTypeLib, name, noVoie, libelleVoie, commune, latitude, longitude FROM installation i, activite a, equipement e, coordonnes c, equipementtype et where c.coordID = i.coordID and a.equipID = e.equipID and a.activiteLib = \""+activite+"\" and e.equipTypecode = et.equipTypeCode and i.installationId=e.installationId")

    cursor.execute(query)

    """ Afficher sous forme de tableau """
    row = cursor.fetchall()
    return row


    cursor.close()
    conn.close()

""" Cette fonction permet l'autocompletion du champs ville """
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

""" Cette fonction permet l'autocompletion du champs activite """
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
