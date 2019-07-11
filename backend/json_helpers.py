import json
from backend.db.scheme import Element

def valid_request_to_add_endpoint(request_body):
    parsed_body = json.loads(request_body)
    return (
        ("name" in parsed_body)
        and ("user_name" in parsed_body)
        and ("amount" in parsed_body)
    )

def create_element(request_body):
    parsed_body = json.loads(request_body)
    element = Element(name=parsed_body["name"], amount=parsed_body["amount"], user_name=parsed_body["user_name"])
    if "price" in parsed_body:
        element.price = parsed_body["price"]
    if "bought" in parsed_body:
        element.bought = parsed_body["bought"]
    print(element)
    return element