from input_parser import InputParser


class Main:
    def run():
        parser = InputParser()
        base_delivery_cost, no_of_packages = parser.parseFirstLine(input())
        packages = parser.parsePackages(no_of_packages)

        pass


if __name__ == "__main__":
    Main.run()
