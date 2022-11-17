import logging
import unittest

from acronym.acronym_task import abbreviate

logging.basicConfig(level=logging.INFO)


class TestAcronym(unittest.TestCase):
    def setUp(self):
        logging.info("Stepped into setUp method")

    def tearDown(self):
        logging.info("Stepped into tearDown method")

    def test_abbreviate(self):
        logging.info("Running test 1")
        self.assertEqual(abbreviate("Halley's Comet"), "HC")

    def test_abbreviate_multi_space(self):
        logging.info("Running test 2")
        self.assertEqual(abbreviate("Halley's    Comet"), "HC")

    def test_abbreviate_list(self):
        logging.info("Running test 3")
        self.failureException(abbreviate(["Jj"]))

    def test_abbreviate_numbers(self):
        logging.info("Running test 4")
        self.assertNotEqual(abbreviate("488"), 4)
        self.assertEqual(abbreviate("488"), "4")
