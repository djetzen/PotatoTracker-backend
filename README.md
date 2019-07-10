[![Build Status](https://travis-ci.com/djetzen/PotatoTracker-backend.svg?branch=master)](https://travis-ci.com/djetzen/PotatoTracker-backend)

# PotatoTracker-backend
Shopping app backend, which should be deployed later on a raspberry pi

## First draft of Database scheme
### Tables
- Purchase (ID (PK), user_name:String)
- Element (ID (PK), Name:String, Amount:Float, Price:Float, user_name:String, bought: Boolean, Purchase(FK))

### Cardinalities
- Purchase(1)--(n)Element
