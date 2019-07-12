# Travis Build
[![Build Status](https://travis-ci.com/djetzen/PotatoTracker-backend.svg?branch=master)](https://travis-ci.com/djetzen/PotatoTracker-backend)

# PotatoTracker-backend
Shopping app backend, which should be deployed later on a raspberry pi

## Contributing
Adding functionality is only possible with a pull request. Direct commits to master are prohibited. Before a pull request can be merged, the automatically triggered travis build needs to be succesful. Also the branch needs to be uptodate to master before merging. Therefore please click on the button inside the pull request or merge it manually.

## Install
This tool is developed with python3. For installation of all the necessary plugins please call locally `pip3 install -r requirements.txt`

## Hooks
Please install the pre-commit hook with hooks/install_hooks.sh. This pre-commit hook always runs black (linter/formatter) before committing files.

## Structure
There is the source folder called backend/ and the tests are inside the backend/tests folder.

## Database
### Tables
- Purchase (ID (PK), user_name:String)
- Element (ID (PK), Name:String, Amount:Float, Price:Float, user_name:String, bought: Boolean, Purchase(FK))

### Cardinalities
- Purchase(1)--(n)Element
