[![Build Status](https://travis-ci.com/djetzen/PotatoTracker-backend.svg?branch=master)](https://travis-ci.com/djetzen/PotatoTracker-backend)

# PotatoTracker-backend
Shopping app backend, which should be deployed later on a raspberry pi

## Install
This tool is developed with python3. For installation of all the necessary plugins please call locally `pip3 install -r requirements.txt`

## Hooks
Please install the pre-commit hook with hooks/install_hooks.sh. This pre-commit hook always runs black (linter/formatter) before committing files.


## First draft of Database scheme
### Tables
- Purchase (ID (PK), user_name:String)
- Element (ID (PK), Name:String, Amount:Float, Price:Float, user_name:String, bought: Boolean, Purchase(FK))

### Cardinalities
- Purchase(1)--(n)Element
