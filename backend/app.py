from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from backend.db.database import Base, create_database
from backend.services.element_service import element_service_impl
from backend.json_helpers import valid_request_to_add_endpoint, create_element
from backend.db.json_mapper import JSONMapper
import json


def add_endpoint(request):
    if not request.body or not valid_request_to_add_endpoint(request.body):
        return Response(status=400)
    else:
        element = create_element(request.body)
        element_service_impl.create_new_element(element)
        return Response(status=201, body=json.dumps(element, cls=JSONMapper))


def show_cart_endpoint(request):
    return Response(status=200)


def add_all_endpoints(config):
    # add endpoint
    config.add_route("add", "/add", request_method="POST")
    config.add_view(add_endpoint, route_name="add")

    # showCart endpoint
    config.add_route("showCart", "/showCart", request_method="GET")
    config.add_view(show_cart_endpoint, route_name="showCart")


if __name__ == "__main__":
    config = Configurator()
    add_all_endpoints(config)
    app = config.make_wsgi_app()
    serve(app, host="0.0.0.0", port=6543)
