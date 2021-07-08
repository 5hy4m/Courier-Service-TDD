from array_operation import ArrayOperation


class Algorithm:
    def __init__(self, no_of_packages, max_weight, packages):
        self.array_ops = ArrayOperation()
        self.no_of_rows = no_of_packages
        self.no_of_columns = max_weight
        self.packages = packages
        self.array_2d = self.array_ops.build2dMatrixWithZeroValues(
            self.no_of_rows, self.no_of_columns
        )

    def start(self):
        self.solve(0, 0)
        self.print_array()
        return self.array_2d
        print("DONE")

    def print_array(self):
        for row in self.array_2d:
            print(row)

    def is_end_of_column(self, col):
        return col > self.no_of_columns

    def solve(self, row, col):
        if self.is_end_of_column(col):
            return self.solve(row + 1, 0)

        if row > self.no_of_rows:
            return

        if row == 0 or col == 0:
            self.array_2d[row][col] = 0
            return self.solve(row, col + 1)

        if (
            self.packages[row - 1].weight
            + self.array_2d[row - 1][col - self.packages[row - 1].weight]
            <= col
        ):
            self.array_2d[row][col] = (
                self.packages[row - 1].weight
                + self.array_2d[row - 1][col - self.packages[row - 1].weight]
            )
            return self.solve(row, col + 1)

        if self.packages[row - 1].weight <= col:
            self.array_2d[row][col] = self.packages[row - 1].weight
            return self.solve(row, col + 1)
        else:
            self.array_2d[row][col] = self.array_2d[row - 1][col]
            return self.solve(row, col + 1)
