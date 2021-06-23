import unittest
import os
import sys
from unittest.mock import patch

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from offer import Offer


class TestOffer(unittest.TestCase):
    def test_read_offer(self):
        self.assertEqual([], Offer.readOffer())
