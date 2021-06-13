from input_parser import InputParser


class Main:
    def run():
        parser = InputParser()

        base_delivery_cost, no_of_packages = parser.parseFirstLine()
        pass


if __name__ == "__main__":
    Main.run()
