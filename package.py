class Package:
    def __init__(self, package):
        self.id = package["id"]
        self.weight = package["weight"]
        self.distance = package["distance"]
        self.offer_code = package["offer_code"]
        self.discount = 0.0
        self.delivery_cost = 0

    def calculateDeliveryCost(self, base_delivery_cost):
        self.delivery_cost = (
            base_delivery_cost + (self.weight * 10) + (self.distance * 5)
        )

    def calculateDiscount(self):
        discount = round(self.delivery_cost * (self.offer_code.discount / 100), 2)
        self.discount = discount
        self.delivery_cost -= discount
