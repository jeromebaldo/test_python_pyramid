from wsgiref.simple_server import make_server
from pyramid.config import Configurator

from controler import HomeController

if __name__ == '__main__':
    config = Configurator()

    # Créez une instance du contrôleur
    home_controller = HomeController()

    # Associez les méthodes du contrôleur aux routes et aux vues correspondantes
    config.add_route('home', '/')
    config.add_view(home_controller.index, route_name='home', request_method='GET')

    config.add_route('about', '/about')
    config.add_view(home_controller.about, route_name='about', request_method='GET')

    # pour créer application wsgi
    app = config.make_wsgi_app()
    
    #specifie le serveur et le port a utiliser
    server = make_server('127.0.0.1', 8080, app)
    server.serve_forever()