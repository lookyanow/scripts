from bottle import route, run, template

@route('/hello/<name>')
def index(name='World'):
    return template('<b>Hi {{name}}</b>!', name=name)

@route('/')
def index():
    return template('<b>Test index page</b>')

@route('/test')
def index():
    return "This is test string"


run(host='localhost', port=8080)

#comment
