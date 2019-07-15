from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from backend.db.database import Base, create_database
from backend.services.element_service import element_service_impl
from backend.json_helpers import (
    valid_request_to_add_endpoint,
    create_element_from_json,
    create_elements,
)
from backend.db.json_mapper import JSONMapper
import json


def add_endpoint(request):
    if not request.body or not valid_request_to_add_endpoint(request.body):
        return Response(status=400)
    else:
        element = create_element_from_json(json.loads(request.body))
        element_service_impl.create_new_element(element)
        return Response(status=201, body=json.dumps(element, cls=JSONMapper))


def cart_endpoint(request):
    if not request.matchdict or not "user_name" in request.matchdict:
        return Response(status=400)
    entities = element_service_impl.find_open_elements_by_user(
        request.matchdict["user_name"]
    )
    return Response(status=200, body=str(json.dumps(entities, cls=JSONMapper)))


def purchase_id_endpoint(request):
    if not request.matchdict or not "id" in request.matchdict:
        return Response(status=400)
    elements = element_service_impl.find_elements_by_purchase_id(
        request.matchdict["id"]
    )
    return Response(status=200, body=str(json.dumps(elements, cls=JSONMapper)))


def cart_endpoint_put(request):
    if not request.body:
        return Response(status=400)
    elements = create_elements(request.body)
    if not elements:
        return Response(status=400)
    else:
        bought_elements = element_service_impl.buy_elements(elements)
        return Response(
            status=200, body=str(json.dumps(bought_elements, cls=JSONMapper))
        )


def add_all_endpoints(config):
    # add endpoint
    config.add_route("add", "/add", request_method="POST")
    config.add_view(add_endpoint, route_name="add")

    # cart endpoint /GET
    config.add_route("cart", "/cart/{user_name}", request_method="GET")
    config.add_view(cart_endpoint, route_name="cart")

    # purchase/id endpoint
    config.add_route("purchase_id", "/purchase/{id}", request_method="GET")
    config.add_view(purchase_id_endpoint, route_name="purchase_id")

    # cart endpoint /PUT
    config.add_route("cart_put", "/cart/{user_name}", request_method="PUT")
    config.add_view(cart_endpoint_put, route_name="cart_put")


def main():
    config = Configurator()
    add_all_endpoints(config)
    app = config.make_wsgi_app()
    return app


if __name__ == "__main__":
    app = main()
    serve(app, host="0.0.0.0", port=6543)
