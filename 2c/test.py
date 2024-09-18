import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def __init__(self):
        super().__init__()
        # Create a student object here
        self.student = Student()

    # Add test cases for getters and setters

    def test_BMI(self):
        # Add new asserts here
        # Test the BMI method of Student Class
        self.assertEqual(1, 1)

    def test_GPA(self):
        # Add new asserts here
        # Test the GPA calculate method of the Student class
        self.assertEqual(1, 1)

    def test_Print(self):
        pass


if __name__ == "__main__":
    unittest.main()
