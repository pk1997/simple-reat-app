import cherrypy 

class server(object):
    @cherrypy.expose
    def index(self, text = " "):
        pass
        print(text)
        return text


cherrypy.quickstart(server())