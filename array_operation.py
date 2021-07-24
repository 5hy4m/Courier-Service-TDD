import functools
from array_operation_helpers import ArrayOpsHelpers


class ArrayOperation(ArrayOpsHelpers):
    def __init__(self, array_2d, row, col):
        self.row = row
        self.col = col
        self.array_2d = array_2d

    @staticmethod
    def build2dMatrixWithZeroValues(no_of_columns, no_of_rows):
        return [[0 for i in range(no_of_rows + 1)] for j in range(no_of_columns + 1)]

    def is_maximum_capacity_of_cell_is_zero(self):
        return self.row == 0 or self.col == 0

    def is_end_of_columns(self, no_of_columns):
        return self.col > no_of_columns

    def is_end_of_rows(self, no_of_rows):
        return self.row > no_of_rows

    def can_add_more_package_in_current_weight(self, packages):
        return (
            self.get_current_package(packages).weight
            + self.previous_package_combination(packages).weight
            <= self.col
        )

    def is_current_combination_has_same_no_of_packages(self, packages):
        return len(self.current_combination(packages)) == len(
            self.previous_package_combination_with_same_weight.packages
        )

    def is_current_combination_has_max_packages(self, packages):
        return len(self.current_combination(packages)) > len(
            self.previous_package_combination_with_same_weight.packages
        )

    def is_current_combination_has_max_weight(self, packages):

        return len(self.current_combination(packages).weight) > len(
            self.previous_package_combination_with_same_weight.weight
        )

    def current_combination_delivery_time(self, packages):
        array = max(
            [
                package.delivery_time
                for package in self.previous_package_combination(packages).packages
                + [self.get_current_package(packages)]
            ]
        )
        return array * 2

    def previous_combination_with_same_weight_delivery_time(self):
        return self.previous_package_combination_with_same_weight.total_delivery_time

    def is_current_package_weight_can_contain_in_current_max_weight(self, packages):
        return self.get_current_package(packages).weight <= self.col

    def assign_zero(self):
        self.array_2d[self.row][self.col] = CellValue()

    def assign_current_package(self, packages):
        self.array_2d[self.row][self.col] = CellValue(
            self.get_current_package(packages)
        )

    def assign_previous_package(self):
        self.array_2d[self.row][
            self.col
        ] = self.previous_package_combination_with_same_weight

    def assign_current_combination(self, packages):
        self.array_2d[self.row][self.col] = CellValue().add_package_to_combination(
            self.previous_package_combination(packages),
            self.get_current_package(packages),
        )

    def assign_previous_combination(self, packages):
        self.array_2d[self.row][
            self.col
        ] = self.previous_package_combination_with_same_weight


class CellValue:
    def __init__(self):
        self.packages = []
        self.weight = 0
        self.total_delivery_time = 0.0

    @property
    def update_weight(self):
        weight_array = [package.weight for package in self.packages]
        self.weight = functools.reduce(self.add, weight_array)

    @staticmethod
    def add(a, b):
        return a + b

    @property
    def update_delivery_time(self):
        delivery_time_array = [package.delivery_time for package in self.packages]
        self.total_delivery_time = max(delivery_time_array) * 2

    def add_package_to_combination(self, instance, package):
        self.packages = instance.packages + [package]
        self.update_weight
        self.update_delivery_time
        return self

    # def assign_combination(self, instance):
    #     self.packages = instance.packages
    #     import pdb

    #     pdb.set_trace()
    #     self.update_weight
    #     self.update_delivery_time
    #     return self
