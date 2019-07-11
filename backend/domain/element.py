class Element:
    def __init__(
        self, name="", amount=0, price=0.0, user_name="", bought=False, purchase_id=None
    ):
        self.name = name
        self.amount = amount
        self.price = price
        self.user_name = user_name
        self.bought = bought
        self.purchase_id = purchase_id

    def __repr__(self):
        return (
            "Element<name: "
            + str(self.name)
            + ", amount: "
            + str(self.amount)
            + ", price: "
            + str(self.price)
            + ", user_name: "
            + str(self.user_name)
            + ", bought: "
            + str(self.bought)
            + ", purchase_id: "
            + str(self.purchase_id)
            + ">"
        )

