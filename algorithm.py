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

    def print_array(self, array_2d):
        for row in array_2d:
            row_ele = []
            for ele in row:
                row_ele.append(ele.weight)
            print(row_ele)

    def find(self):
        return self.array_2d[-1][-1]

    def solve(self, row, col):
        for row in range(self.no_of_rows + 1):
            for col in range(self.no_of_columns + 1):
                array_ops = ArrayOperation(self.array_2d, row, col)

                if array_ops.is_end_of_columns(self.no_of_columns):
                    continue

                if array_ops.is_end_of_rows(self.no_of_rows):
                    continue

                if array_ops.is_maximum_capacity_of_cell_is_zero():
                    array_ops.assign_zero()
                    continue

                if array_ops.can_add_more_package_in_current_weight(self.packages):
                    if array_ops.is_current_combination_has_max_packages(self.packages):
                        array_ops.assign_current_combination(self.packages)
                    elif array_ops.is_current_combination_has_same_no_of_packages(
                        self.packages
                    ):
                        if array_ops.is_current_combination_has_max_weight:
                            array_ops.assign_current_combination(self.packages)
                        elif array_ops.is_current_combination_has_same_weight:
                            if (
                                array_ops.current_combination_delivery_time(
                                    self.packages
                                )
                                <= array_ops.previous_combination_with_same_weight_delivery_time()
                            ):
                                array_ops.assign_current_combination(self.packages)
                            else:
                                array_ops.assign_previous_combination(self.packages)
                        else:
                            array_ops.assign_previous_combination(self.packages)
                    else:
                        array_ops.assign_previous_combination(self.packages)
                    continue

                if array_ops.is_current_package_weight_can_contain_in_current_max_weight(
                    self.packages
                ):
                    array_ops.assign_current_package(self.packages)
                    continue
                else:
                    array_ops.assign_previous_package()
                    continue

    # def solve(self, row, col):
    #     array_ops = ArrayOperation(self.array_2d, row, col)

    #     if array_ops.is_end_of_columns(self.no_of_columns):
    #         return self.solve(row + 1, 0)

    #     if array_ops.is_end_of_rows(self.no_of_rows):
    #         return

    #     if array_ops.is_maximum_capacity_of_cell_is_zero():
    #         array_ops.assign_zero()
    #         return self.solve(row, col + 1)

    #     if array_ops.can_add_more_package_in_current_weight(self.packages):
    #         if array_ops.is_current_combination_has_max_packages(self.packages):
    #             array_ops.assign_current_combination(self.packages)
    #         else:
    #             array_ops.assign_previous_combination(self.packages)
    #         return self.solve(row, col + 1)

    #     if not array_ops.is_current_package_weight_can_contain_in_current_max_weight(
    #         self.packages
    #     ):
    #         array_ops.assign_current_package(self.packages)
    #         return self.solve(row, col + 1)
    #     else:
    #         array_ops.assign_previous_package()
    #         return self.solve(row, col + 1)
