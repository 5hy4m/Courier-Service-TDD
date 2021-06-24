from offer import Offer
from package import Package


class PackageManager:
    @staticmethod
    def getOfferObject(package_code, offers):
        for offer in offers:
            if offer.code == package_code:
                return offer

    @classmethod
    def createPackageObjects(cls, packages, offers):
        package_objs = []
        for package in packages:
            package["offer_code"] = cls.getOfferObject(package["offer_code"], offers)
            package_objs.append(Package(package))
        return package_objs

    @staticmethod
    def createOfferObjects(offers):
        offers_objs = []
        for offer in offers:
            offers_objs.append(Offer(offer))
        return offers_objs

    @staticmethod
    def isOfferCodeExist(package_offer, offers):
        for offer in offers:
            if package_offer.code == offer.code:
                return True
        else:
            return False

    @staticmethod
    def isOfferCodeValid(package):
        offer = package.offer_code
        if (
            not offer.lower_limit_distance
            <= package.distance
            <= offer.upper_limit_distance
        ):
            # print('Offer code not valid due to distance limitation')
            return False
        if not offer.lower_limit_weight <= package.weight <= offer.upper_limit_weight:
            # print('Offer code not valid due to weight limitation')
            return False
        return True

    def calculateDeliveryCost(self, packages, offers, base_delivery_cost):
        for package in packages:
            package.delivery_cost = (
                base_delivery_cost + (package.weight * 10) + (package.distance * 5)
            )
            if self.isOfferCodeExist(package.offer_code, offers):
                if self.isOfferCodeValid(package):
                    discount = round(
                        package.delivery_cost * (package.offer_code.discount / 100), 2
                    )
                    package.discount = discount
                    package.delivery_cost -= discount
        else:
            return packages
