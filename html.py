import cherrypy

class Html5:
    structure = '''<!Doctype html>
<html>
    <head>
        <title>Mi primer app en Cherrypy</title>
    </head>
    <body>
        <h1>Mi primer app en Cherrypy</h1>
    </body>
</html>
'''
    @cherrypy.expose
    def index(self):
        return self.structure

if __name__ == '__main__':
    cherrypy.quickstart(Html5())
