import unittest

from star_sign import star_sign


class TestStarSign(unittest.TestCase):
    def test_should_be_capricorn(self):
        self.assertEqual(star_sign(1, 20), "Capricorn")

    def test_should_type_int(self):
        self.assertEqual(type(star_sign(1, 20)), str)

    def test_value_should_be_a_valid_month_and_day_number(self):
        self.assertRaises(ValueError, star_sign(-1, 500))
