import unittest
import os
import sys
from unittest.mock import patch
from unittest import mock

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from algorithm import ShipmentFinder
from array_operation import ArrayOperation
from constants import (
    ARRAY_2D,
    BUILT2DARRAY,
    SOLVED_ARRAY,
    SOLVED_ARRAY_WITH_WEIGHT_CONSTRAINT,
)
from mock import InputMock
from input_parser import InputParser
from package_manager import PackageManager


class TestAlgorithm(unittest.TestCase):
    @mock.patch("builtins.input")
    def setUp(self, mock_input):
        InputMock.execute(mock_input, data="algorithm")
        (
            self.base_delivery_cost,
            self.no_of_packages,
            self.packages,
            self.offers,
            self.vehicles,
        ) = InputParser().invoke()
        self.manager = PackageManager(
            self.base_delivery_cost, self.packages, self.offers, self.vehicles
        )

    def test_build_2d_matrix(self):
        no_of_packages = 3
        max_weight = 2
        result = ArrayOperation.build2dMatrixWithZeroValues(no_of_packages, max_weight)
        self.assertEqual(result, ARRAY_2D)

    def test_solve_2d_array(self):
        no_of_packages = 4
        max_weight = 4
        output = self.manager.calculateTotalDeliveryCost()
        shipment_finder = ShipmentFinder(
            no_of_packages,
            max_weight,
            self.packages,
        )
        shipment_finder.solve(0, 0)
        result_2d_array = shipment_finder.array_2d
        for row in range(no_of_packages + 1):
            for col in range(max_weight + 1):
                result_2d_array[row][col] = result_2d_array[row][col].weight
        self.assertEqual(result_2d_array, SOLVED_ARRAY)

    @mock.patch("builtins.input")
    def test_solve_2d_array_check_weight(self, mock_input):
        InputMock.execute(mock_input, data="algorithm_with_weight")
        (
            base_delivery_cost,
            no_of_packages,
            packages,
            offers,
            vehicles,
        ) = InputParser().invoke()
        manager = PackageManager(base_delivery_cost, packages, offers, vehicles)
        no_of_packages = len(packages)
        max_weight = vehicles[0].max_weight
        manager.calculateTotalDeliveryCost()
        shipment_finder = ShipmentFinder(
            no_of_packages,
            max_weight,
            packages,
        )
        shipment_finder.solve(0, 0)
        result_2d_array = shipment_finder.array_2d

        for row in range(no_of_packages + 1):
            for col in range(max_weight + 1):
                result_2d_array[row][col] = result_2d_array[row][col].weight
        # for row in result_2d_array:
        #     row_ele = []
        #     for ele in row:
        #         row_ele.append(ele.weight)
        #     print(row_ele)
        self.assertEqual(result_2d_array, SOLVED_ARRAY_WITH_WEIGHT_CONSTRAINT)


if __name__ == "__main__":
    unittest.main()
