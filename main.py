from input_parser import InputParser

# from output_parser import OutputParser
from package_manager import PackageManager
from package import Package
from offer import Offer


def main():
    base_delivery_cost, no_of_packages, packages, offers = InputParser().invoke()
    manager = PackageManager(base_delivery_cost, packages, offers)
    manager.calculateTotalDeliveryCost()
    # packages = manager.createPackageObjects(packages, offers)


if __name__ == "__main__":
    main()
