# PotatoTracker-backend
Shopping app backend, which should be deployed later on a raspberry pi

## First draft of Database scheme
### Tables
- User (ID (PK), Name:String)
- Purchase (ID (PK), UserId(FK))
- Purchase-Element (PurchaseID(PK),ElementID(PK), alreadyBought:boolean)
- Element (ID (PK), Name:String, Amount:Float, Price:Float)

### Cardinalities
- User(1)--(n)Purchase
- Purchase(n)--(m)Element