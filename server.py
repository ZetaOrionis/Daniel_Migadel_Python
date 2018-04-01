from bottle import route, run, template, error, get, request, static_file, view, url
from model import modele

@error(404)
def error404(error):
    return {"Excusez nous, une erreur 404 vient d'apparaître" : 404}

@error(500)
def error500(error):
    return {"Excusez nous, une erreur 500 vient d'apparaître" : 500}

@route('/')
@view('home')
def home():
    return { 'url': url }

@route('/views/:path#.+#', name='views')
def static(path):
    return static_file(path, root='views')

@route('/traitement')
def home() :
    activite = request.query.activite
    ville = request.query.ville1

    reponse = list(modele.recherche(activite,ville))
    if len(reponse) == 0:
        return {"Excusez nous, nous n'avons pas trouvé de réponse à votre requète."}

    return template('reponse', reponse=reponse)

@route('/test')
def home() :
    ville = request.query.ville2
    
    reponse = list(modele.rechercheInstallation(ville))
    for rep in reponse:
        print(rep)

    if len(reponse) == 0:
        return {"Excusez nous, nous n'avons pas trouvé de réponse à votre requète."}

    print(len(reponse))

    return template('reponse', reponse=reponse)

run(host='localhost', port=8000,debug=False, reloader=True)
