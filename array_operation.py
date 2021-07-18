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

    def is_current_combination_has_max_packages(self, packages):
        return len(self.current_combination(packages)) >= len(
            self.previous_package_with_same_weight.packages
        )

    def is_current_package_weight_can_contain_in_current_max_weight(self, packages):
        return self.get_current_package(packages).weight <= self.col

    def assign_zero(self):
        self.array_2d[self.row][self.col] = CellValue(0)

    def assign_current_package(self, packages):
        self.array_2d[self.row][self.col] = CellValue(
            self.get_current_package(packages)
        )

    def assign_previous_package(self):
        self.array_2d[self.row][self.col] = CellValue(
            self.previous_package_with_same_weight
        )

    def assign_current_combination(self, packages):
        self.array_2d[self.row][self.col] = CellValue(
            self.previous_package_combination(packages),
            self.get_current_package(packages),
        )

    def assign_previous_combination(self, packages):
        self.array_2d[self.row][self.col] = CellValue(
            self.previous_package_with_same_weight,
        )


# class CellValue:
#     def __init__(self):
#         self.package = []
#         self.weight = 0

#     @property
#     def update_weight(self):
#         weight_array = [package.weight for package in self.packages]
#         self.weight = functools.reduce(self.add, weight_array)

#     @staticmethod
#     def add(a, b):
#         return a + b

#     def add_package_to_the_cell_value(self, instance, package):
#         self.packages = instance1.packages + [package]
#         self.update_weight

#     def assign_cell_value(self, instance):
#         self.packages = instance.packages
#         self.update_weight


class CellValue:
    def __init__(self, instance1, package=None):
        if isinstance(instance1, CellValue):
            if not package:
                self.packages = instance1.packages
            else:
                self.packages = instance1.packages + [package]
            if len(self.packages) != 0:
                weight_array = [package.weight for package in self.packages]
                self.weight = functools.reduce(self.add, weight_array)
            else:
                self.weight = 0
        else:
            self.packages = []
            self.weight = 0

    @staticmethod
    def add(a, b):
        return a + b
