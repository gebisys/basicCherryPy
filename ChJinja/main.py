import cherrypy
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('template'))

class Root:
    @cherrypy.expose
    def index(self):
        tpl = env.get_template('index.html')
        d = {}
        for i in range(10):
            d[i] = i
            
        return tpl.render(salutation='hello', target=d)

if __name__ == '__main__':
    cherrypy.quickstart(Root())

