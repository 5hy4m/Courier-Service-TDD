class ArrayOpsHelpers:
    def is_end_of_columns(self, no_of_columns):
        return self.col > no_of_columns

    def is_end_of_rows(self, no_of_rows):
        return self.row > no_of_rows

    @property
    def previous_package(self):
        return self.row - 1

    @property
    def previous_shipment_with_same_weight(self):
        return self.array_2d[self.previous_package][self.col]

    def get_current_package(self, packages):
        return packages[self.row - 1]

    def previous_package_combination(self, packages):
        return self.array_2d[self.previous_package][
            self.col - self.get_current_package(packages).weight
        ]

    def current_combination(self, packages):
        return self.previous_package_combination(packages).combination + [
            self.get_current_package(packages)
        ]

    def weight_of_current_combination(self, packages):
        return (
            self.previous_package_combination(packages).weight
            + self.get_current_package(packages).weight
        )

    def current_shipment_delivery_time(self, packages):
        return_time = 2
        delivery_time = (
            self.previous_package_combination(self.packages).total_delivery_time
            + self.get_current_package(self.packages).delivery_time
        )
        return delivery_time * return_time
