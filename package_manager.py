from offer import Offer
from package import Package
from algorithm import Algorithm


class PackageManager:
    def __init__(self, base_delivery_cost, packages, offers):
        self.packages = packages
        self.offers = offers
        self.base_delivery_cost = base_delivery_cost

    def calculateTotalDeliveryCost(self):
        for package in self.packages:
            offer_code = package.offer_code
            package.calculateDeliveryCost(self.base_delivery_cost)
            if offer_code.isOfferCodeExist(self.offers) and offer_code.isOfferCodeValid(
                package.weight,
                package.distance,
            ):
                package.calculateDiscount()
        else:
            return self.packages

    def estimate_delivery_time(self, vehicles):
        max_weight = vehicles[0].max_weight
        is_done = True
        combination = Algorithm(len(self.packages), max_weight, self.packages).start()
        return combination
