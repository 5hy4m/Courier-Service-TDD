import unittest
import os
import sys
from unittest.mock import patch
from io import StringIO

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from package_manager import PackageManager
from package import Package
from offer import Offer
from tests.constants import PACKAGES_ARRAY_OF_OBJECTS, OFFERS_ARRAY_OF_OBJECTS, OUTPUT
from main import main
from mock import InputMock


class TestMainFunction(unittest.TestCase):
    @patch("builtins.input")
    def test_output(self, mock_input):
        InputMock.execute(mock_input)

        with patch("sys.stdout", new=StringIO()) as fake_out:
            main()
            self.assertEqual(
                fake_out.getvalue(),
                OUTPUT,
            )


if __name__ == "__main__":
    unittest.main()
