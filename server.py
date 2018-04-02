from bottle import route, run, template, error, get, request, static_file, view, url
from model import modele

@error(404)
def error404(error):
    return {"Excusez nous, une erreur 404 vient d'apparaître" : 404}

@error(500)
def error500(error):
    return {"Excusez nous, une erreur 500 vient d'apparaître" : 500}

@route('/')
def home():
    activites = list(modele.rechercheActivites())
    return template('home',activites=activites, url=url )
   

@route('/views/:path#.+#', name='views')
def static(path):
    return static_file(path, root='views')

@route('/traitement')
def home() :
    activite = request.query.activite
    ville = request.query.ville1

    reponse = list(modele.recherche(activite,ville))
    if len(reponse) == 0:
        return template('error')

    lenreponse = len(reponse)

    return template('reponse', reponse=reponse, lenreponse=lenreponse)

@route('/test')
def home() :
    ville = request.query.ville2
    
    reponse = list(modele.rechercheInstallation(ville))

    if len(reponse) == 0:
        return template('error')

    lenreponse = len(reponse)

    return template('reponse', reponse=reponse, lenreponse=lenreponse)

run(host='localhost', port=8000, debug=False, reloader=True)
