from offer import Offer
from package import Package


class PackageManager:
    @staticmethod
    def calculateDeliveryCost(package, base_delivery_cost):
        package.delivery_cost = (
            base_delivery_cost + (package.weight * 10) + (package.distance * 5)
        )

    @staticmethod
    def calculateDiscount(package):
        discount = round(package.delivery_cost * (package.offer_code.discount / 100), 2)
        package.discount = discount
        package.delivery_cost -= discount

    def calculateTotalDeliveryCost(self, packages, offers, base_delivery_cost):
        for package in packages:
            self.calculateDeliveryCost(package, base_delivery_cost)
            if Offer.isOfferCodeExist(package.offer_code, offers):
                if Offer.isOfferCodeValid(package):
                    self.calculateDiscount(package)
        else:
            return packages
