from offer import Offer
from package import Package
from algorithm import ShipmentFinder
import copy


class PackageManager:
    def __init__(self, base_delivery_cost, packages, offers, vehicles):
        self.packages = packages
        self.offers = offers
        self.base_delivery_cost = base_delivery_cost
        self.vehicles = vehicles
        self.current_time = 0.0

    @classmethod
    def get_available_vehicle(cls, vehicles):
        # print("VEHICLES", (vehicles[0].available, vehicles[1].available))
        # print(
        #     "VEHICLES",
        #     (vehicles[0].return_time, vehicles[1].return_time),
        # )
        return_vehicle = vehicles[0]
        for vehicle in vehicles[1:]:
            if return_vehicle.return_time > vehicle.return_time:
                return_vehicle = vehicle
        return return_vehicle

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

    def remove_delivered_packages(self, shipment, non_delivered_packages):
        return [
            package for package in non_delivered_packages if package not in shipment
        ]

    def addition(self, package):
        package.delivery_time = self.current_time + package.delivery_time
        return package

    def estimate_delivery_time(self, vehicles):
        max_weight = vehicles[0].max_weight
        is_done = False
        while self.packages:
            vehicle = self.get_available_vehicle(vehicles)
            if vehicle.available:
                shipment_finder = ShipmentFinder(
                    len(self.packages), max_weight, self.packages
                )
                shipment = shipment_finder.find()

                # Setting Vehicle return time
                vehicle.return_time += shipment.total_delivery_time
                vehicle.available = False

                for package in shipment.combination:
                    package.delivery_time = self.current_time + package.delivery_time

                self.packages = list(
                    filter(lambda x: x not in shipment.combination, self.packages)
                )
            else:
                # Waiting for the vehicle nearest vehicle to return

                self.current_time += vehicle.return_time - self.current_time
                vehicle.available = True
