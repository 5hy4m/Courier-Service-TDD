import unittest
import os
import sys
from unittest.mock import patch

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from package_manager import PackageManager
from package import Package
from offer import Offer
from tests.constants import PACKAGES_ARRAY_OF_OBJECTS, OFFERS_ARRAY_OF_OBJECTS


class TestMainFunction(unittest.TestCase):
    manager = PackageManager()

    def test_create_packages(self):
        packages = PACKAGES_ARRAY_OF_OBJECTS
        for package in self.manager.createPackageObjects(packages):
            self.assertIsInstance(package, Package)

    # def test_offer_packages(self):
    #     offers = OFFERS_ARRAY_OF_OBJECTS
    #     for offer in self.manager.createOfferObjects(offers):
    #         self.assertIsInstance(offer, Offer)


if __name__ == "__main__":
    unittest.main()
