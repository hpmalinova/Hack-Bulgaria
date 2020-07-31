import unittest

from silence_errors import silence_exception, silence_exception_class


class TestSilenceErrorsWithContextManager(unittest.TestCase):
    def test_when_raised_expected_error(self):
        with silence_exception(ValueError):
            # nothing should happen
            raise ValueError('Test')

    def test_when_raised_unexpected_error(self):
        with self.assertRaisesRegex(TypeError, 'Test'):
            with silence_exception(ValueError):
                # the error should be re-raised since it is not expected.
                raise TypeError('Test')

    def test_when_raised_expected_error_with_msg(self):
        with silence_exception(ValueError, 'Test'):
            # nothing should happen
            raise ValueError('Test')

    def test_when_raised_unexpected_error_with_msg(self):
        with self.assertRaisesRegex(ValueError, 'Test'):
            with silence_exception(ValueError, 'Testing.'):
                # the error should be re-raised since it is not expected.
                raise ValueError('Test')


class TestSilenceErrorsWithClass(unittest.TestCase):
    def test_class_when_raised_expected_error(self):
        with silence_exception_class(ValueError):
            # nothing should happen
            raise ValueError('Test')

    def test_class_when_raised_unexpected_error(self):
        with self.assertRaisesRegex(TypeError, 'Test'):
            with silence_exception_class(ValueError):
                # the error should be re-raised since it is not expected.
                raise TypeError('Test')

    def test_class_when_raised_expected_error_with_msg(self):
        with silence_exception_class(ValueError, 'Test'):
            # nothing should happen
            raise ValueError('Test')

    def test_class_when_raised_unexpected_error_with_msg(self):
        with self.assertRaisesRegex(ValueError, 'Test'):
            with silence_exception_class(ValueError, 'Testing.'):
                # the error should be re-raised since it is not expected.
                raise ValueError('Test')


if __name__ == '__main__':
    unittest.main()
