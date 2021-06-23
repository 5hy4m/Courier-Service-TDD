from input_parser import InputParser
from package_manager import PackageManager
from package import Package
from offer import Offer


def main():
    parse = InputParser()
    base_delivery_cost, no_of_packages = parse.firstLine(input())
    packages = parse.packages(no_of_packages)
    offers = parse.offers()

    manager = PackageManager()
    manager.createPackageObjects(packages)
    manager.createOfferObjects(offers)

    pass


if __name__ == "__main__":
    main()
