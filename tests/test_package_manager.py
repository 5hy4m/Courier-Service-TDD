import unittest
import os
import sys
from unittest.mock import patch

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from package_manager import PackageManager
from package import Package
from tests.constants import PACKAGES_ARRAY_OF_OBJECTS


class TestPackageManager(unittest.TestCase):
    def setUp(self):
        packages = PackageManager.createPackageObjects(packages):
            
    def test_calculate_delivery_cost_of_packages():



if __name__ == "__main__":
    unittest.main()
