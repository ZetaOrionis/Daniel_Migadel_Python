import mysql.connector

""" Selection d'une installation précise dans une ville donnée """
def rechercheInstallation(ville) :

    """ Connection à la base de données """

    conn = mysql.connector.connect(host="infoweb",user="E165106N",password="E165106N",database="E165106N")
    cursor = conn.cursor()

    query = ("SELECT * FROM test where commune LIKE \""+ ville +"\" ")

    cursor.execute(query)

    """ Afficher sous forme de tableau """
    row = cursor.fetchall()
    return row

    cursor.close()
    conn.close()

""" Selection d'une activitée précise dans une ville donnée """
def recherche(activite,ville) :

    """ Connection à la base de données """

    conn = mysql.connector.connect(host="infoweb",user="E165106N",password="E165106N",database="E165106N")
    cursor = conn.cursor()

    query = ("SELECT * FROM PaysdelaLoire where activite LIKE \""+ activite +"\" and ville LIKE \""+ ville +"\" ")

    cursor.execute(query)

    """ Afficher sous forme de tableau """
    row = cursor.fetchall()
    return row


    cursor.close()
    conn.close()
