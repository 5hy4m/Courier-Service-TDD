class InputParser:
    def typeCheck(self, element, datatype):
        try:
            return datatype(element)
        except Exception as error:
            print(error)

    def parseFirstLine(self, first_line):
        base_delivery_cost, no_of_packages = first_line.split(" ")

        base_delivery_cost = self.typeCheck(base_delivery_cost, int)
        no_of_packages = self.typeCheck(no_of_packages, int)

        return (base_delivery_cost, no_of_packages)
