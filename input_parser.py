import json
from offer import Offer
from package import Package
from vehicle import Vehicle


class InputParser:
    def __init__(self):
        self.base_delivery_cost = 0
        self.no_of_packages = 0
        self.packages = []
        self.offers = []
        self.vehicles = []

    def invoke(self):
        self.firstLine(input())
        self.extractOffers()
        self.extractPackages()
        self.extractVehicles()
        return (
            self.base_delivery_cost,
            self.no_of_packages,
            self.packages,
            self.offers,
            self.vehicles,
        )

    def firstLine(self, first_line):
        self.base_delivery_cost, self.no_of_packages = first_line.split(" ")

        self.base_delivery_cost = self.typeConvert(self.base_delivery_cost, int)
        self.no_of_packages = self.typeConvert(self.no_of_packages, int)

        return (self.base_delivery_cost, self.no_of_packages)

    def getOfferObject(self, package_code):
        for offer in self.offers:
            if offer.code == package_code:
                return offer

    def extractPackages(self):
        for _ in range(self.no_of_packages):
            inputs = input()
            id, weight, distance, offer_code = inputs.split(" ")
            self.packages.append(
                Package(
                    {
                        "id": id,
                        "weight": self.typeConvert(weight, int),
                        "distance": self.typeConvert(distance, float),
                        "offer_code": self.getOfferObject(offer_code),
                    }
                )
            )

    def extractOffers(self):
        self.offers = self.readOffers()
        for index, offer in enumerate(self.offers):
            offer["lower_limit_distance"] = self.typeConvert(
                offer["lower_limit_distance"], int
            )
            offer["upper_limit_distance"] = self.typeConvert(
                offer["upper_limit_distance"], int
            )
            offer["lower_limit_weight"] = self.typeConvert(
                offer["lower_limit_weight"], int
            )
            offer["upper_limit_weight"] = self.typeConvert(
                offer["upper_limit_weight"], int
            )
            offer["discount"] = self.typeConvert(offer["discount"], float)
            self.offers[index] = Offer(offer)

    def extractVehicles(self):
        no_of_vehicles, speed, max_weight = input().split(" ")
        no_of_vehicles = self.typeConvert(no_of_vehicles, int)
        max_weight = self.typeConvert(max_weight, int)
        speed = self.typeConvert(speed, int)

        for _ in range(no_of_vehicles):
            self.vehicles.append(Vehicle(speed, max_weight))

    @staticmethod
    def typeConvert(element, datatype):
        try:
            return datatype(element)
        except Exception as error:
            raise ValueError(error)

    @staticmethod
    def readOffers():
        try:
            with open("offers.json") as f:
                offers = json.load(f)
            return offers
        except FileNotFoundError as error:
            raise error
