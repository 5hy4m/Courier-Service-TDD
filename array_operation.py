class ArrayOperation:
    def build2dMatrixWithZeroValues(self, rows, columns):
        return [[0 for i in range(columns + 1)] for j in range(rows + 1)]
