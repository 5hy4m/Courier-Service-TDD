import unittest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from input_parser import InputParser


class TestInputParser(unittest.TestCase):
    parser = InputParser()

    def test_parse_first_line_with_correct_input(self):
        base_delivery_cost = 100
        no_of_packages = 3

        self.assertEqual(
            (
                base_delivery_cost,
                no_of_packages,
            ),
            self.parser.parseFirstLine("100 3"),
        )

    def test_parse_first_line_with_incorrect_input(self):
        base_delivery_cost = 100
        no_of_packages = 3

        self.assertEqual(
            (
                base_delivery_cost,
                no_of_packages,
            ),
            self.parser.parseFirstLine("100 3"),
        )


if __name__ == "__main__":
    unittest.main()
