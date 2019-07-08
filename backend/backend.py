from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world_endpoint(request):
    print('Incoming request')
    return Response(status=200, body='Hello World!')

def add_endpoints(config):
    config.add_route('hello', '/')
    config.add_view(hello_world_endpoint, route_name='hello')

if __name__ == '__main__':
    config = Configurator()
    add_endpoints(config)
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)