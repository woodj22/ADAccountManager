import unittest

from activedirectory.validate_password import ValidatePassword

class TestValidatePassword(unittest.TestCase):

    def test_it_contains_a_numrical_digit(self):
        i = ValidatePassword()._match_password_complexity('5')
        self.assertTrue(True in i)

    def test_it_contains_a_special_character(self):
        i = ValidatePassword()._match_password_complexity('$')
        self.assertTrue(True in i)

    def test_it_contains_lower_case_character(self):
        i = ValidatePassword()._match_password_complexity('d')
        self.assertTrue(True in i)

    def test_it_contains_upper_case_character(self):
        i = ValidatePassword()._match_password_complexity('U')
        self.assertTrue(True in i)

    def test_it_has_enough_characters(self):
        has_enough_characters = ValidatePassword().has_enough_characters('Uddwi04ho3')
        self.assertTrue(has_enough_characters)

    def test_it_has_not_reached_character_limit_returns_false_when_its_reached_the_character_limit(self):
        has_enough_characters = ValidatePassword().has_not_reached_character_limit('Uddwidsdgrfsgdrd54504ho3')
        self.assertFalse(has_enough_characters)

    def test_it_has_not_reached_character_limit_returns_true_when_its_under_the_character_limit(self):
        has_enough_characters = ValidatePassword().has_not_reached_character_limit('Uddwidho3')
        self.assertTrue(has_enough_characters)

    def test_it_has_complexity(self):
        is_complex = ValidatePassword().has_complexity('Uddwiho7')
        self.assertTrue(is_complex)

    def test_it_has_no_spaces_returns_false_if_it_contains_a_space(self):
        has_not_spaces = ValidatePassword().has_no_spaces('Uddwi ho7')
        self.assertFalse(has_not_spaces)

    def test_it_validates_a_string(self):
        validator = ValidatePassword()
        validator.validate('oha sdf')
        i = validator.exception_messages
        print(i)


if __name__ == '__main__':
    unittest.main()
