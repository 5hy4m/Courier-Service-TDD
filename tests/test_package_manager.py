import unittest
import os
import sys
from unittest.mock import patch

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from package_manager import PackageManager
from input_parser import InputParser
from package import Package
from tests.constants import (
    PACKAGES_ARRAY_OF_OBJECTS,
    OFFERS_ARRAY_OF_OBJECTS,
    PARSED_OFFERS_ARRAY_OF_OBJECTS,
)


class TestPackageManager(unittest.TestCase):
    def setUp(self):
        self.package_manager = PackageManager()
        self.input_parser = InputParser()
        self.base_delivery_cost = 100
        self.offers = self.package_manager.createOfferObjects(
            PARSED_OFFERS_ARRAY_OF_OBJECTS
        )
        self.packages = self.package_manager.createPackageObjects(
            PACKAGES_ARRAY_OF_OBJECTS, self.offers
        )

    def test_calculate_delivery_cost_of_packages(self):
        output = self.package_manager.calculateDeliveryCost(
            self.packages, self.offers, self.base_delivery_cost
        )
        self.assertEqual(output[0].discount, 0)
        self.assertEqual(output[1].discount, 0)
        self.assertEqual(output[2].discount, 35)
        self.assertEqual(output[0].delivery_cost, 175)
        self.assertEqual(output[1].delivery_cost, 275)
        self.assertEqual(output[2].delivery_cost, 665)


if __name__ == "__main__":
    unittest.main()
