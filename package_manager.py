from offer import Offer
from package import Package
from algorithm import Algorithm


class PackageManager:
    def __init__(self, base_delivery_cost, packages, offers, vehicles):
        self.packages = packages
        self.offers = offers
        self.base_delivery_cost = base_delivery_cost
        self.vehicles = vehicles
        self.current_time = 0.0

    def calculateTotalDeliveryCost(self):
        for package in self.packages:
            offer_code = package.offer_code
            package.calculateDeliveryCost(self.base_delivery_cost)
            package.calculate_delivery_time(
                self.current_time, self.vehicles[0].max_speed
            )
            if (
                offer_code
                and offer_code.isOfferCodeExist(self.offers)
                and offer_code.isOfferCodeValid(package.weight, package.distance)
            ):
                package.calculateDiscount()
        else:
            return self.packages

    def estimate_delivery_time(self, vehicles):
        max_weight = vehicles[0].max_weight
        is_done = False
        while not is_done:
            combination_finder = Algorithm(
                len(self.packages), max_weight, self.packages
            )
            combination_finder.start()
            combination = combination_finder.find()

            is_done = True
            # import pdb

            # pdb.set_trace()
