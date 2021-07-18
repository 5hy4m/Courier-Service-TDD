class ArrayOpsHelpers:
    @property
    def previous_package(self):
        return self.row - 1

    def get_current_package(self, packages):
        return packages[self.row - 1]

    @property
    def previous_package_combination_with_same_weight(self):
        return self.array_2d[self.previous_package][self.col]

    def previous_package_combination(self, packages):
        return self.array_2d[self.previous_package][
            self.col - self.get_current_package(packages).weight
        ]

    def current_combination(self, packages):
        return self.previous_package_combination(packages).packages + [
            self.get_current_package(packages)
        ]
