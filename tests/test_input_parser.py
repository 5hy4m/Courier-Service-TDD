import unittest
import os
import sys
import json
import builtins
from unittest import mock

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from tests.constants import PACKAGES_ARRAY_OF_OBJECTS, OFFERS_ARRAY_OF_OBJECTS
from input_parser import InputParser


class TestInputParser(unittest.TestCase):
    parse = InputParser()

    def test_parse_first_line_with_correct_input(self):
        self.assertEqual((100, 3), self.parse.firstLine("100 3"))

    def test_parse_first_line_with_incorrect_inputs(self):
        with self.assertRaises(ValueError):
            self.parse.firstLine("100.5 3")
            self.parse.firstLine("100 3.6")
            self.parse.firstLine("passing string")
            self.parse.firstLine("Hi This Should Give Error")

    @mock.patch(
        "builtins.input",
        side_effect=[
            "PKG1 5 5 OFR001",
            "PKG2 15 5 OFR002",
            "PKG3 10 100 OFR003",
        ],
    )
    def test_parse_packages_with_correct_input(self, mock_input):
        self.assertEqual(
            PACKAGES_ARRAY_OF_OBJECTS,
            self.parse.packages(3),
        )

    @mock.patch(
        "builtins.input",
        side_effect=["PKG1 weight distance OFR001"],
    )
    def test_parse_packages_with_incorrect_input(self, mock_input):
        with self.assertRaises(ValueError):
            self.parse.packages(1)

    def test_parse_offers(self):
        read_data = json.dumps(OFFERS_ARRAY_OF_OBJECTS)
        mock_open = mock.mock_open(read_data=read_data)
        with mock.patch("builtins.open", mock_open):
            self.assertEqual(OFFERS_ARRAY_OF_OBJECTS, self.parse.offers())


if __name__ == "__main__":
    unittest.main()
