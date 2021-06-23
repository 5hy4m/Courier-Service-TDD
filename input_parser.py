import json


class InputParser:
    def typeConvert(self, element, datatype):
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

    def offers(self):
        try:
            with open("offers.json") as f:
                offers = json.load(f)
            return offers
        except FileNotFoundError as error:
            raise error
