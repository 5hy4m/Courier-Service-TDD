from array_operation import ArrayOperation


class Algorithm:
    def __init__(self, no_of_packages, max_weight, packages):
        self.array_ops = ArrayOperation
        self.no_of_rows = no_of_packages
        self.no_of_columns = max_weight
        self.packages = packages
        self.array_2d = self.array_ops.build2dMatrixWithZeroValues(
            self.no_of_rows, self.no_of_columns
        )

    def start(self):
        self.solve(0, 0)
        self.print_array(self.array_2d)
        print("DONE")
        return self.array_2d

    def print_array(self, array_2d):
        for row in array_2d:
            print(row)

    def solve(self, row, col):
        array_ops = ArrayOperation(self.array_2d, row, col)
        if array_ops.is_end_of_columns(self.no_of_columns):
            return self.solve(row + 1, 0)

        if array_ops.is_end_of_rows(self.no_of_rows):
            return array_ops

        if array_ops.is_maximum_capacity_of_cell_is_zero():
            array_ops.assign_zero()
            return self.solve(row, col + 1)

        if array_ops.can_add_more_package_in_current_weight(self.packages):
            array_ops.assign_current_package_weight(self.packages)
            return self.solve(row, col + 1)

        if array_ops.is_package_weight_less_than_current_weight(self.packages):
            array_ops.assign_package_weight()
            return self.solve(row, col + 1)
        else:
            array_ops.assign_previous_weight()
            return self.solve(row, col + 1)
