import unittest
import os
import sys
from unittest.mock import patch
from unittest import mock

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from package_manager import PackageManager
from input_parser import InputParser
from mock import InputMock
from package import Package
from offer import Offer
from tests.constants import (
    PACKAGES_ARRAY_OF_OBJECTS,
    OFFERS_ARRAY_OF_OBJECTS,
    PARSED_OFFERS_ARRAY_OF_OBJECTS,
)


class TestPackageManager(unittest.TestCase):
    @mock.patch("builtins.input")
    def setUp(self, mock_input):
        InputMock.execute(mock_input)
        (
            self.base_delivery_cost,
            self.no_of_packages,
            self.packages,
            self.offers,
            self.vehicles,
        ) = InputParser().invoke()
        self.manager = PackageManager(
            self.base_delivery_cost, self.packages, self.offers
        )

    def test_calculate_delivery_cost_of_packages(self):
        output = self.manager.calculateTotalDeliveryCost()
        self.assertEqual(output[0].discount, 0)
        self.assertEqual(output[1].discount, 0)
        self.assertEqual(output[2].discount, 35)
        self.assertEqual(output[0].delivery_cost, 175)
        self.assertEqual(output[1].delivery_cost, 275)
        self.assertEqual(output[2].delivery_cost, 665)


if __name__ == "__main__":
    unittest.main()
