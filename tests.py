import unittest
from format_price import format_price


class TestFormatPriceFunction(unittest.TestCase):
    def test_billion_value(self):
        self.assertEqual(format_price(1234567890), '1\xa0234\xa0567\xa0890')
    def test_removing_zeros(self):
        self.assertEqual(format_price(123.4500), '123.45')
    def test_long_float_value(self):
        self.assertEqual(format_price(123456.0000001), '123\xa0456')
    def test_rounding(self):
        self.assertEqual(format_price(0.987654321), '0.99')
    def test_float_with_comma(self):
        self.assertEqual(format_price('0,12'), '0.12')
    def test_correct_value(self):
        self.assertEqual(format_price('123.45'), '123.45')
    def test_first_space(self):
        self.assertEqual(format_price(' 123.45'), '123.45')
    def test_zero(self):
        self.assertEqual(format_price(0), 'Not available')
    def test_negative_value(self):
        self.assertEqual(format_price(-1), 'Not available')
    def test_empty_value(self):
        self.assertEqual(format_price(''), 'Not available')
    def test_incorrect_value(self):
        self.assertEqual(format_price('a1234'), 'Not available')
    def test_list_value(self):
        self.assertEqual(format_price(['1', [2]]), 'Not available')
    def test_none_value(self):
        self.assertEqual(format_price(None), 'Not available')


if __name__ == "__main__":
    unittest.main()