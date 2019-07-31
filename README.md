# Travis Build
[![Build Status](https://travis-ci.com/djetzen/PotatoTracker-backend.svg?branch=master)](https://travis-ci.com/djetzen/PotatoTracker-backend)

# PotatoTracker-backend
Shopping app backend, which should be deployed later on a raspberry pi

## Contributing
Adding functionality is only possible with a pull request. Direct commits to master are prohibited. Before a pull request can be merged, the automatically triggered travis build needs to be succesful. Also the branch needs to be uptodate to master before merging. Therefore please click on the button inside the pull request or merge it manually.

## Install
This tool is developed with python3. For installation of all the necessary plugins please call locally `pip3 install -r requirements.txt`

## Docker
You can build a docker image using `docker -t <yourNameOfTheImage> build .` from root directory. Running the container can be done with `docker container run -p 654:6543 <yourNameOfTheImage>`

## Hooks
Please install the pre-commit hook with hooks/install_hooks.sh. This pre-commit hook always runs black (linter/formatter) before committing files.

## Structure
There is the source folder called backend/ and the tests are inside the backend/tests folder.

## Endpoints
There are several endpoints, which are the following:
### /add
This is a POST-Endpoint. Input is something like this: `{"user_name": "User","name": "lemons","amount": "5"}` and return value on success is something like this: `{"name": "lemons", "amount": "5", "price": 0.0, "user_name": "User", "bought": false, "purchase_id": null}`

### /cart/{user_name}
This endpoint exists in two different methods. GET and PUT
#### GET
This endpoint returns all the elements, which are assigned to a user and which are not already bought (bought:False)
#### PUT
This PUT endpoint indicates, that a purchase is triggered. Therefore the elements are given in such a way:
```
{"elements": [{"name": "Lemons","amount": 5,"user_name": "User"},{"name": "Apples","amount": 3,"price": 0,"user_name": "User"}]}
```
and returned is something like this:
```
[{"name": "Lemons", "amount": 5, "price": 0.0, "user_name": "User", "bought": true, "purchase_id": 1}, {"name": "Apples", "amount": 3, "price": 0.0, "user_name": "User", "bought": true, "purchase_id": 1}]
```

### /purchases/{id}
This is a GET endpoint, which returns all the elements, which are assigned to a specific purchase.
Example return value:
```
[{"name": "Lemons", "amount": 5, "price": 0.0, "user_name": "User", "bought": false, "purchase_id": null}, {"name": "Apples", "amount": 3, "price": 0.0, "user_name": "User", "bought": false, "purchase_id": null}]
```

### /purchases/
This is a GET endpoint, which returns all the purchases which were created so far.

## Database
### Tables
- Purchase (ID (PK), user_name:String)
- Element (ID (PK), Name:String, Amount:Float, Price:Float, user_name:String, bought: Boolean, Purchase(FK))

### Cardinalities
- Purchase(1)--(n)Element
