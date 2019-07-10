from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from backend.db.database import Base, create_database
import json


def add_endpoint(request):
    if not request.body or not __valid(request.body):
        return Response(status=400)
    else:
        return Response(status=201, body=request.body)


def __valid(request_body):
    parsed_body = json.loads(request_body)
    return (
        ("user" in parsed_body)
        and ("amount" in parsed_body)
        and ("elementName" in parsed_body)
    )


def add_all_endpoints(config):
    config.add_route("add", "/add", request_method="POST")
    config.add_view(add_endpoint, route_name="add")


if __name__ == "__main__":
    config = Configurator()
    add_all_endpoints(config)
    app = config.make_wsgi_app()
    serve(app, host="0.0.0.0", port=6543)
