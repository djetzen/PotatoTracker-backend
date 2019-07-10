[![Build Status](https://travis-ci.com/djetzen/PotatoTracker-backend.svg?branch=master)](https://travis-ci.com/djetzen/PotatoTracker-backend)

# PotatoTracker-backend
Shopping app backend, which should be deployed later on a raspberry pi

## First draft of Database scheme
### Tables
- User (Name:String(PK)
- Purchase (ID (PK), UserName(FK))
- Element (ID (PK), Name:String, Amount:Float, Price:Float, Purchase(FK))

### Cardinalities
- User(1)--(n)Purchase
- Purchase(1)--(n)Element
