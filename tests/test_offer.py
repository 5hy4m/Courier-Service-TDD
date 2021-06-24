import unittest
import os
import sys
from unittest.mock import patch
from input_parser import InputParser

from tests.constants import PACKAGES_ARRAY_OF_OBJECTS, PARSED_OFFERS_ARRAY_OF_OBJECTS

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from offer import Offer


class TestOffer(unittest.TestCase):
    def test_read_offer(self):
        self.assertEqual(PARSED_OFFERS_ARRAY_OF_OBJECTS, InputParser.offers())
