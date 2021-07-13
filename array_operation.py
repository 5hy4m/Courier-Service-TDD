class ArrayOperation:
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
            packages[self.row - 1].weight
            + self.array_2d[self.row - 1][self.col - packages[self.row - 1].weight]
            <= self.col
        )

    def is_package_weight_less_than_current_weight(self, packages):
        return packages[self.row - 1].weight <= self.col

    def assign_zero(self):
        self.array_2d[self.row][self.col] = 0

    def assign_package_weight(self):
        self.array_2d[self.row][self.col] = self.packages[self.row - 1].weight

    def assign_previous_weight(self):
        self.array_2d[self.row][self.col] = self.array_2d[self.row - 1][self.col]

    def assign_current_package_weight(self, packages):
        self.array_2d[self.row][self.col] = (
            packages[self.row - 1].weight
            + self.array_2d[self.row - 1][self.col - packages[self.row - 1].weight]
        )
