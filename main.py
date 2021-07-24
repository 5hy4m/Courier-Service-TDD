from input_parser import InputParser

# from output_parser import OutputParser
from package_manager import PackageManager


def printOutput(packages):
    for package in packages:
        print(f"{package.id} {int(package.discount)} {int(package.delivery_cost)}")


def main():
    (
        base_delivery_cost,
        no_of_packages,
        packages,
        offers,
        vehicles,
    ) = InputParser().invoke()
    manager = PackageManager(base_delivery_cost, packages, offers, vehicles)
    manager.calculateTotalDeliveryCost()
    manager.estimate_delivery_time(vehicles)
    printOutput(packages)


if __name__ == "__main__":
    main()
