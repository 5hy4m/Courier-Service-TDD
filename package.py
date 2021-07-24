class Package:
    def __init__(self, package):
        self.id = package["id"]
        self.weight = package["weight"]
        self.distance = package["distance"]
        self.offer_code = package["offer_code"]
        self.discount = 0.0
        self.delivery_cost = 0
        self.delivery_time = 0

    @staticmethod
    def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier

    def calculateDeliveryCost(self, base_delivery_cost):
        self.delivery_cost = (
            base_delivery_cost + (self.weight * 10) + (self.distance * 5)
        )

    def calculateDiscount(self):
        discount = round(self.delivery_cost * (self.offer_code.discount / 100), 2)
        self.discount = discount
        self.delivery_cost -= discount

    def calculate_delivery_time(self, current_time, max_speed):
        self.delivery_time = self.truncate(self.distance / max_speed, 2)
        # self.delivery_time = round(current_time + delivery_time, 2)
        return self.delivery_time
