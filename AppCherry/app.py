import cherrypy
import os

def rel(x):
    return os.path.join(os.path.abspath('.'), u''+x+'')

class App:
    @cherrypy.expose
    def index(self):
        return open(os.path.join(rel('html'), u'index.html'))

_config = {'/css':
                  {'tools.staticdir.on':True,
                   'tools.staticdir.dir':rel('css')},
           '/js':
                   {'tools.staticdir.on':True,
                    'tools.staticdir.dir':rel('js')},
           '/images':
                   {'tools.staticdir.on':True,
                    'tools.staticdir.dir':rel('images')}
          }

if __name__ == '__main__':
    cherrypy.quickstart(App(), config=_config)
