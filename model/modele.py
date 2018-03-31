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

    cursor.execute("""SELECT * from installation where commune = %s""",ville)

    rows = cursor.fetchall()
    return rows
    
    cursor.close()
    conn.close()

""" Selection d'une activitée précise dans une ville donnée """
def recherche(activite,ville) :

    """ Connection à la base de données """

    conn = mysql.connector.connect(host="localhost",user="root",password="",database="installations_sportives")
    cursor = conn.cursor()

    query = ("SELECT * FROM PaysdelaLoire where activite LIKE \""+ activite +"\" and ville LIKE \""+ ville +"\" ")

    cursor.execute(query)

    """ Afficher sous forme de tableau """
    row = cursor.fetchall()
    return row


    cursor.close()
    conn.close()
