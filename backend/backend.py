from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response


def add_hello_world_endpoint(request):
    print('Incoming request')
    return Response('<body><h1>Hello World!</h1></body>')

def add_endpoints(config: Configurator):
    # hello world
    config.add_route('hello', '/')
    config.add_view(add_hello_world_endpoint, route_name='hello')

if __name__ == '__main__':
    config = Configurator()
    add_endpoints(config)
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)