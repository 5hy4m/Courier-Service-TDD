import unittest
import os
import sys
import json
import builtins
from unittest import mock

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from tests.constants import (
    PACKAGES_ARRAY_OF_OBJECTS,
    OFFERS_ARRAY_OF_OBJECTS,
    PARSED_OFFERS_ARRAY_OF_OBJECTS,
)
from input_parser import InputParser


class TestInputParser(unittest.TestCase):
    parse = InputParser()

    def test_parse_first_line_with_correct_input(self):
        self.assertEqual((100, 3), self.parse.firstLine("100 3"))

    def test_parse_first_line_with_incorrect_inputs(self):
        with self.assertRaises(ValueError):
            self.parse.firstLine("100.5 3")
        with self.assertRaises(ValueError):
            self.parse.firstLine("100 3.6")
        with self.assertRaises(ValueError):
            self.parse.firstLine("passing string")
        with self.assertRaises(ValueError):
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

        self.parse.no_of_packages = len(PACKAGES_ARRAY_OF_OBJECTS)
        self.parse.extractOffers()
        self.parse.extractPackages()
        self.assertEqual(
            PACKAGES_ARRAY_OF_OBJECTS[0]["offer_code"],
            self.parse.packages[0].offer_code.code,
        )
        self.assertEqual(
            PACKAGES_ARRAY_OF_OBJECTS[0]["weight"],
            self.parse.packages[0].weight,
        )
        self.assertEqual(
            PACKAGES_ARRAY_OF_OBJECTS[0]["distance"],
            self.parse.packages[0].distance,
        )
        self.assertEqual(
            PACKAGES_ARRAY_OF_OBJECTS[0]["id"],
            self.parse.packages[0].id,
        )

    @mock.patch(
        "builtins.input",
        side_effect=["PKG1 weight distance OFR001"],
    )
    def test_parse_packages_with_incorrect_input(self, mock_input):
        with self.assertRaises(ValueError):
            self.parse.extractPackages()

    def test_parse_offers(self):
        second_element = 1
        read_data = json.dumps(OFFERS_ARRAY_OF_OBJECTS)
        mock_open = mock.mock_open(read_data=read_data)
        self.parse.extractOffers()
        with mock.patch("builtins.open", mock_open):
            self.assertEqual(
                PARSED_OFFERS_ARRAY_OF_OBJECTS[second_element]["discount"],
                self.parse.offers[second_element].discount,
            )
            self.assertEqual(
                PARSED_OFFERS_ARRAY_OF_OBJECTS[second_element]["lower_limit_distance"],
                self.parse.offers[second_element].lower_limit_distance,
            )
            self.assertEqual(
                PARSED_OFFERS_ARRAY_OF_OBJECTS[second_element]["upper_limit_distance"],
                self.parse.offers[second_element].upper_limit_distance,
            )
            self.assertEqual(
                PARSED_OFFERS_ARRAY_OF_OBJECTS[second_element]["lower_limit_weight"],
                self.parse.offers[second_element].lower_limit_weight,
            )
            self.assertEqual(
                PARSED_OFFERS_ARRAY_OF_OBJECTS[second_element]["upper_limit_weight"],
                self.parse.offers[second_element].upper_limit_weight,
            )


if __name__ == "__main__":
    unittest.main()
