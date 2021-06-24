from offer import Offer


class Package:
    def __init__(self, package):
        self.id = package["id"]
        self.weight = package["weight_in_kg"]
        self.distance = package["distance_in_km"]
        self.offer_code = package["offer_code"]
        self.discount = 0.0
        self.delivery_cost = 0
