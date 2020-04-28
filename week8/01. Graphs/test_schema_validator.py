import unittest
from schema_validator import schema_validator


class TestSchemaValidator(unittest.TestCase):
    def setUp(self):
        self.schema = [
            'key1',
            'key2',
            [
                'key3',
                ['inner_key1', 'inner_key2']
            ]
        ]
        self.data = {
            'key1': 'val1',
            'key2': 'val2',
            'key3': {
                'inner_key1': 'val1',
                'inner_key2': 'val2'
            }
        }

    def test_schema_validator_when_data_is_not_dictionary_then_raise_exc(self):
        data = [
            'key1', 'val1',
            'key2', 'val2',
            'key3', {
                'inner_key1': 'val1',
                'inner_key2': 'val2'
            }
        ]

        with self.assertRaisesRegex(TypeError, 'Data should be of type dictionary'):
            schema_validator(self.schema, data)

    def test_schema_validator_when_schema_is_not_list_then_raise_exc(self):
        schema = {1: 'a', 2: 'b'}
        data = {
            'key1': 'val1',
            'key2': 'val2',
            'key3': {
                'inner_key1': 'val1',
                'inner_key2': 'val2'
            }
        }

        with self.assertRaisesRegex(TypeError, 'Schema should be of type list'):
            schema_validator(schema, data)

    def test_schema_validator_when_data_is_valid_then_return_true(self):
        self.assertTrue(schema_validator(self.schema, self.data))

    def test_schema_validator_when_data_has_more_keys_then_return_false(self):
        self.data['key4'] = 'not_expected'

        self.assertFalse(schema_validator(self.schema, self.data))

    def test_schema_validator_when_schema_has_more_keys_then_return_false(self):
        self.schema.append('key4')

        self.assertFalse(schema_validator(self.schema, self.data))

    def test_schema_validator_when_data_and_schema_have_different_key_names_then_return_false(self):
        data = {
            'key1': 'val1',
            'key2': 'val2',
            'key3': {
                'inner_key1': 'val1',
                'inner_key3': 'val2'
            }
        }

        self.assertFalse(schema_validator(self.schema, data))


if __name__ == '__main__':
    unittest.main()
