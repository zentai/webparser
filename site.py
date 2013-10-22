import cherrypy

class Resource(object):
    exposed = True
    def GET(self):
        return "good job!!"

class Root(object):
    pass

if __name__ == '__main__':
    root = Root()
    root.gj = Resource()

    conf = {
        'global': {
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 8080,
        },
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        }
    }

    cherrypy.quickstart(root, '/', conf)
