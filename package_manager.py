from offer import Offer
from package import Package


class PackageManager:
    def createPackageObjects(self, packages):
        package_objs = []
        for package in packages:
            package_objs.append(Package(package))
        return package_objs

    def createOfferObjects(self, offers):
        for offer in offers:
            Offer(offer)

    def calculateDeliveryCost():
        pass
