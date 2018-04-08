from bottle import route, run, template, error, get, request, static_file, view, url
from model import modele
from pprint import pprint
import json


""" Permet la gestion des erreurs pouvant survenir durant l'utilisation du site """
@error(404)
def error404(error):
    return {"Excusez nous, une erreur 404 vient d'apparaître" : 404}

@error(405)
def error405(error):
    return {"Excusez nous, une erreur 405 vient d'apparaître" : 405}

@error(500)
def error500(error):
    return {"Excusez nous, une erreur 500 vient d'apparaître" : 500}



""" Permet l'affichage de la page d'accueil du site """
@route('/')
def home():
    return template('home', url=url )

""" Permet la liasion des fichiers externes aux templates comme les fichiers CSS, ou JS """
@route('/views/:path#.+#', name='views')
def static(path):
    return static_file(path, root='views')


""" Permet la liasion entre le modèle et la view pour l'autocomplétion par ville, renvoie sous format JSON """
@route('/autocompletionville')
def home() :
    ville = request.query.commune

    reponse = modele.autocompletionville(ville)
    pprint(reponse)
    if len(reponse) == 0:
        return template('error')

    return json.dumps(reponse)


""" Permet la liasion entre le modèle et la view pour l'autocomplétion par activité, renvoie sous format JSON """
@route('/autocompletionactivite')
def home() :
    activite = request.query.activite

    reponse = modele.autocompletionactivite(activite)
    pprint(reponse)
    if len(reponse) == 0:
        return template('error')

    return json.dumps(reponse)

""" Permet la liasion entre le modèle et la view pour la recherche par ville et activité """
@route('/villeActivite')
def home() :
    activite = request.query.activite
    # ville = request.query.ville1
    latitude = request.query.latitude
    longitude = request.query.longitude
    distance = request.query.slider
    ville = request.query.ville2
    radio = request.query.radio

    print("RADIO ---- > "+radio)

    if radio == "adresse" :
        print("-------> ADRESSE")
        reponse = list(modele.rechercheVilleActivite(activite,latitude,longitude,distance))
        if len(reponse) == 0:
            return template('error')
        lenreponse = len(reponse)
        return template('reponse', reponse=reponse, lenreponse=lenreponse, url=url)

    elif radio == "ville":
        print("-------> VILLE")
        reponse = list(modele.rechercheVilleLargeActivite(activite,ville))
        if len(reponse) == 0:
            return template('error')
        lenreponse = len(reponse)
        return template('reponse2', reponse=reponse, lenreponse=lenreponse, url=url)

    else :
        return template('error')

""" Permet la liasion entre le modèle et la view pour la recherche par ville """
@route('/ville')
def home() :
    ville = request.query.ville2

    reponse = list(modele.rechercheVille(ville))

    if len(reponse) == 0:
        return template('error')

    lenreponse = len(reponse)

    return template('reponse', reponse=reponse, lenreponse=lenreponse, url=url)

""" Permet la liasion entre le modèle et la view pour la recherche par activité """
@route('/activite')
def home() :
    activite = request.query.activite2

    reponse = list(modele.rechercheActivite(activite))
    if len(reponse) == 0:
        return template('error')

    lenreponse = len(reponse)

    return template('reponse', reponse=reponse, lenreponse=lenreponse, url=url)

run(host='localhost', port=8000, debug=False, reloader=True)
