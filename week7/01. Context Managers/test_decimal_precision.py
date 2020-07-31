import unittest
from decimal import *

from decimal_precision import change_decimal_precision, ChangeDecimalPrecision


class TestChangePrecisionWithContextManager(unittest.TestCase):
    def test_change_precision_when_result_is_less_than_1_then_change_precision_in_with_block(self):
        expected_result = Decimal('0.36')

        with change_decimal_precision(2):
            result = Decimal('0.123') + Decimal('0.236')

        self.assertEqual(result, expected_result)

    def test_change_precision_when_result_is_greater_than_1_then_change_precision_in_with_block(self):
        expected_result = Decimal('3.3592')

        with change_decimal_precision(5):
            result = Decimal('1.123123') + Decimal('2.236123')

        self.assertEqual(result, expected_result)

    def test_when_change_precision_then_restore_previous_precision_after_with_block(self):
        expected_result = Decimal('3.359246')

        with change_decimal_precision(2):
            pass

        result = Decimal('1.123123') + Decimal('2.236123')

        self.assertEqual(result, expected_result)

    def test_when_divide_by_zero_raise_DivisionByZero_exception(self):
        with self.assertRaises(DivisionByZero):
            with change_decimal_precision(2):
                Decimal('0.123123') / Decimal('0')

    def test_when_operator_gets_float_and_decimal_raise_TypeError(self):
        with self.assertRaises(TypeError):
            with change_decimal_precision(2):
                Decimal('0.123123') + 0.123123

    def test_when_operator_gets_decimal_from_float_and_decimal_dont_raise_TypeError(self):
        with change_decimal_precision(2):
            Decimal('0.123123') + getcontext().create_decimal_from_float(0.123123)

    def test_when_decimal_created_from_float_then_is_set_to_precision(self):
        expected_result = Decimal('0.13')

        with change_decimal_precision(2):
            result = getcontext().create_decimal_from_float(0.128123)

        self.assertEqual(result, expected_result)

class TestChangePrecisionWithClass(unittest.TestCase):
    def test_change_precision_when_result_is_less_than_1_then_change_precision_in_with_block(self):
        expected_result = Decimal('0.36')

        with ChangeDecimalPrecision(2):
            result = Decimal('0.123') + Decimal('0.236')

        self.assertEqual(result, expected_result)

    def test_change_precision_when_result_is_greater_than_1_then_change_precision_in_with_block(self):
        expected_result = Decimal('3.3592')

        with ChangeDecimalPrecision(5):
            result = Decimal('1.123123') + Decimal('2.236123')

        self.assertEqual(result, expected_result)

    def test_when_change_precision_then_restore_previous_precision_after_with_block(self):
        expected_result = Decimal('3.359246')

        with ChangeDecimalPrecision(2):
            pass

        result = Decimal('1.123123') + Decimal('2.236123')

        self.assertEqual(result, expected_result)

    def test_when_divide_by_zero_raise_DivisionByZero_exception(self):
        with self.assertRaises(DivisionByZero):
            with ChangeDecimalPrecision(2):
                Decimal('0.123123') / Decimal('0')

    def test_when_operator_gets_float_and_decimal_raise_TypeError(self):
        with self.assertRaises(TypeError):
            with ChangeDecimalPrecision(2):
                Decimal('0.123123') + 0.123123

    def test_when_operator_gets_decimal_from_float_and_decimal_dont_raise_TypeError(self):
        with ChangeDecimalPrecision(2):
            Decimal('0.123123') + getcontext().create_decimal_from_float(0.123123)

    def test_when_decimal_created_from_float_then_is_set_to_precision(self):
        expected_result = Decimal('0.13')

        with ChangeDecimalPrecision(2):
            result = getcontext().create_decimal_from_float(0.128123)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
