from offer import Offer
from package import Package


class PackageManager:
    def __init__(self, base_delivery_cost, packages, offers):
        self.packages = packages
        self.offers = offers
        self.base_delivery_cost = base_delivery_cost
        self.package_class = Package

    def calculateTotalDeliveryCost(self):
        for package in self.packages:
            package.calculateDeliveryCost(self.base_delivery_cost)
            if package.offer_code.isOfferCodeExist(self.offers):
                if package.offer_code.isOfferCodeValid(
                    package.weight, package.distance
                ):
                    package.calculateDiscount()
        else:
            return self.packages

    def estimateDeliveryTime(self):
        pass
