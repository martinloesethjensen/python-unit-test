import unittest

from school_admin.school import *


class TestSchoolAdministration(unittest.TestCase):
    # Name is a string, no numbers are allowed in the string, and name should not be empty
    # Cpr format 'xxxxxx-xxxx' where x is numbers, and is a valid cpr number
    def test_if_name_is_a_string(self):
        student = Student("Name is a string", '123456-1234')

        self.assertEqual(type(student.name), str)

    def test_if_name_contains_numbers(self):
        self.assertRaises(TypeError, Student, name="Name222With444Numbers666")
