import unittest
import os
import sys
from unittest.mock import patch

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from input_parser import InputParser


class TestInputParser(unittest.TestCase):
    parser = InputParser()

    def test_parse_first_line_with_correct_input(self):
        self.assertEqual((100, 3), self.parser.parseFirstLine("100 3"))

    def test_parse_first_line_with_incorrect_inputs(self):
        with self.assertRaises(ValueError):
            self.parser.parseFirstLine("100.5 3")
            self.parser.parseFirstLine("100 3.6")
            self.parser.parseFirstLine("passing string")
            self.parser.parseFirstLine("Hi This Should Give Error")

    @patch(
        "builtins.input",
        side_effect=[
            "PKG1 5 5 OFR001",
            "PKG2 15 5 OFR002",
            "PKG3 10 100 OFR003",
        ],
    )
    def test_parse_packages_with_correct_input(self, mock_input):
        self.assertEqual(
            [
                {
                    "id": "PKG1",
                    "weight_in_kg": 5,
                    "distance_in_km": 5,
                    "offer_code": "OFR001",
                },
                {
                    "id": "PKG2",
                    "weight_in_kg": 15,
                    "distance_in_km": 5,
                    "offer_code": "OFR002",
                },
                {
                    "id": "PKG3",
                    "weight_in_kg": 10,
                    "distance_in_km": 100,
                    "offer_code": "OFR003",
                },
            ],
            self.parser.parsePackages(3),
        )

    @patch(
        "builtins.input",
        side_effect=[
            "PKG1 weight distance OFR001",
        ],
    )
    def test_parse_packages_with_incorrect_input(self, mock_input):
        with self.assertRaises(ValueError):
            self.parser.parsePackages(1)


if __name__ == "__main__":
    unittest.main()
