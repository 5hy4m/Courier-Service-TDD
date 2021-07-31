from array_operation import ArrayOperation


class ShipmentFinder:
    def __init__(self, no_of_packages, max_weight, packages):
        self.array_ops = ArrayOperation
        self.no_of_rows = no_of_packages
        self.no_of_columns = max_weight
        self.packages = packages
        self.array_2d = self.array_ops.build2dMatrixWithZeroValues(
            self.no_of_rows, self.no_of_columns
        )

    def print_array(self, array_2d):
        for row in array_2d:
            row_ele = []
            for ele in row:
                row_ele.append(ele.weight)
            print(row_ele)

    def find(self):
        self.solve(0, 0)
        # self.print_array(self.array_2d)
        return self.array_2d[-1][-1]

    def solve(self, row, col):
        for row in range(self.no_of_rows + 1):
            for col in range(self.no_of_columns + 1):
                array_ops = ArrayOperation(self.array_2d, row, col, self.packages)

                if array_ops.base_check(self.no_of_rows, self.no_of_columns):
                    continue

                elif array_ops.is_maximum_capacity_of_cell_is_zero():
                    array_ops.assign_zero()

                elif array_ops.can_add_package_to_shipment():
                    if (
                        array_ops.is_current_shipment_has_max_packages()
                        or (
                            array_ops.is_current_shipment_has_same_no_of_packages()
                            and array_ops.is_current_shipment_has_max_weight()
                        )
                        or (
                            array_ops.is_current_shipment_has_same_weight()
                            and array_ops.is_current_shipment_has_low_delivery_time()
                        )
                    ):
                        array_ops.assign_current_shipment()
                    else:
                        array_ops.assign_previous_shipment()

                elif (
                    array_ops.is_current_shipment_weight_can_contain_in_current_max_weight()
                ):
                    array_ops.assign_current_package()
                else:
                    array_ops.assign_previous_shipment()
