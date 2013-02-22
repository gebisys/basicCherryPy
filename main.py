import cherrypy

class HolaMundo:
    @cherrypy.expose
    def index(self):
        return '''Visita la p&aacute;gina de contacto
<a href="/contacto/">aqu&iacute;</a>'''

    @cherrypy.expose
    def contacto(self):
        return '''Esta es la p&aacute;gina de contacto'''
    
if __name__ == '__main__':
    cherrypy.quickstart(HolaMundo())
