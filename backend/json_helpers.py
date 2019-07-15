import json
from backend.domain.element import Element


def valid_request_to_add_endpoint(request_body):
    parsed_body = json.loads(request_body)
    return (
        ("name" in parsed_body)
        and ("user_name" in parsed_body)
        and ("amount" in parsed_body)
    )


def create_elements(request_body):
    elements = []
    json_elements = json.loads(request_body)
    if not "elements" in json_elements:
        return []
    for json_element in json_elements["elements"]:
        elements.append(create_element_from_json(json_element))
    return elements


def create_element_from_json(loaded_json):
    element = Element(
        name=loaded_json["name"],
        amount=loaded_json["amount"],
        user_name=loaded_json["user_name"],
    )
    if "price" in loaded_json:
        element.price = loaded_json["price"]
    if "bought" in loaded_json:
        element.bought = loaded_json["bought"]
    if "purchase_id" in loaded_json:
        element.purchase_id = loaded_json["purchase_id"]
    return element
