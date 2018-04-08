import mysql.connector
import CreateDB

""" Recherche par ville """
def rechercheVille(ville) :

    """ Connection à la base de données """

    connection,cursor = dbEquip.createConnection()

    query = ("SELECT activiteLib, equNom, equipTypeLib, name, noVoie, libelleVoie, commune, equGpsY, equGpsX FROM Installation i, Activite a, Equipement e, Coordonnes c, EquipementType et where c.coordID = i.coordID and i.commune = \""+ville+"\" and i.installationId = e.installationId and a.equipID = e.equipID and e.equipTypecode = et.equipTypeCode")
    cursor.execute(query)

    """ Afficher sous forme de tableau """
    rows = cursor.fetchall()
    return rows

    cursor.close()
    conn.close()

""" Selection d'une activitée précise dans une ville donnée """
def rechercheVilleActivite(activite,latitude,longitude,distance) :

    """ Connection à la base de données """

    connection,cursor = CreateDB.dbEquip.createConnection()

    rows = CreateDB.dbEquip.selectLocationDistance(cursor,distance,latitude,longitude,activite)

    print(rows)
    return rows

    cursor.close()
    conn.close()

""" Selection d'une activitée précise dans une ville donnée """
def rechercheVilleLargeActivite(activite,ville) :

    """ Connection à la base de données """

    connection,cursor = CreateDB.dbEquip.createConnection()

    rows = CreateDB.dbEquip.selectActiviteVille(cursor,activite,ville)

    print(rows)
    return rows

    cursor.close()
    conn.close()


""" Recherche par activitée """
def rechercheActivite(activite) :

    """ Connection à la base de données """

    connection,cursor = dbEquip.createConnection()


    query = ("SELECT activiteLib, equNom, equipTypeLib, name, noVoie, libelleVoie, commune, equGpsY, equGpsX FROM Installation i, Activite a, Equipement e, Coordonnes c, EquipementType et  where c.coordID = i.coordID and a.equipID = e.equipID and a.activiteLib = \""+activite+"\" and e.equipTypecode = et.equipTypeCode and i.installationId=e.installationId")

    cursor.execute(query)

    """ Afficher sous forme de tableau """
    row = cursor.fetchall()
    return row


    cursor.close()
    conn.close()

""" Cette fonction permet l'autocompletion du champs ville """
def autocompletionville(ville) :
    connection,cursor = CreateDB.dbEquip.createConnection()

    commune = '%'+ville+'%'

    query = ("SELECT DISTINCT commune FROM Installation where commune LIKE \'"+commune+"\'")

    cursor.execute(query)

    """ Afficher sous forme de tableau """
    row = cursor.fetchall()
    return row


    cursor.close()
    conn.close()

""" Cette fonction permet l'autocompletion du champs activite """
def autocompletionactivite(activite) :
    connection,cursor = CreateDB.dbEquip.createConnection()

    act = '%'+activite+'%'

    query = ("SELECT DISTINCT activiteLib FROM Activite where activiteLib LIKE \'"+act+"\'")

    cursor.execute(query)

    """ Afficher sous forme de tableau """
    row = cursor.fetchall()
    return row


    cursor.close()
    conn.close()
