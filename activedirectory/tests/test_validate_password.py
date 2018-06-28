import unittest

from activedirectory.validate_password import ValidatePassword

class TestValidatePassword(unittest.TestCase):

    def test_it_contains_a_numrical_digit(self):
        i = ValidatePassword().match_password_complexity('5')
        self.assertTrue(True in i)

    def test_it_contains_a_special_character(self):
        i = ValidatePassword().match_password_complexity('$')
        self.assertTrue(True in i)

    def test_it_contains_lower_case_character(self):
        i = ValidatePassword().match_password_complexity('d')
        self.assertTrue(True in i)

    def test_it_contains_upper_case_character(self):
        i = ValidatePassword().match_password_complexity('U')
        self.assertTrue(True in i)


if __name__ == '__main__':
    unittest.main()
