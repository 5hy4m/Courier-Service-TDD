import json


class InputParser:
    @staticmethod
    def typeConvert(element, datatype):
        try:
            return datatype(element)
        except Exception as error:
            raise ValueError(error)

    def firstLine(self, first_line):
        base_delivery_cost, no_of_packages = first_line.split(" ")

        base_delivery_cost = self.typeConvert(base_delivery_cost, int)
        no_of_packages = self.typeConvert(no_of_packages, int)

        return (base_delivery_cost, no_of_packages)

    def packages(self, no_of_packages):
        packages = []
        for _ in range(no_of_packages):
            id, weight_in_kg, distance_in_km, offer_code = input().split(" ")
            packages.append(
                {
                    "id": id,
                    "weight_in_kg": self.typeConvert(weight_in_kg, int),
                    "distance_in_km": self.typeConvert(distance_in_km, float),
                    "offer_code": offer_code,
                }
            )
        return packages

    @staticmethod
    def readOffers():
        try:
            with open("offers.json") as f:
                offers = json.load(f)
            return offers
        except FileNotFoundError as error:
            raise error

    @classmethod
    def offers(cls):
        offers = cls.readOffers()
        for offer in offers:
            offer["lower_limit_distance"] = cls.typeConvert(
                offer["lower_limit_distance"], int
            )
            offer["upper_limit_distance"] = cls.typeConvert(
                offer["upper_limit_distance"], int
            )
            offer["lower_limit_weight"] = cls.typeConvert(
                offer["lower_limit_weight"], int
            )
            offer["upper_limit_weight"] = cls.typeConvert(
                offer["upper_limit_weight"], int
            )
            offer["discount"] = cls.typeConvert(offer["discount"], float)
        return offers
