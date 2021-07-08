import unittest
import os
import sys
from unittest.mock import patch
from unittest import mock

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from algorithm import Algorithm
from array_operation import ArrayOperation
from constants import ARRAY_2D, BUILT2DARRAY, SOLVED_ARRAY
from mock import InputMock
from input_parser import InputParser


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

    def test_build_2d_matrix(self):
        no_of_packages = 3
        max_weight = 2
        result = ArrayOperation().build2dMatrixWithZeroValues(
            no_of_packages, max_weight
        )
        self.assertEqual(result, ARRAY_2D)

    def test_built_2d_array(self):
        no_of_packages = 4
        max_weight = 4
        result_2d = Algorithm(no_of_packages, max_weight, self.packages).start()
        self.assertEqual(result_2d, SOLVED_ARRAY)
