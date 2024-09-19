import unittest
from Employee import Employee


class EmployeeTest(unittest.TestCase):

    def __init__(self):
        # Complete the initialization of the Employee
        super().__init__()
        self.employee = Employee()

    def test_BMI(self):
        # Complete this test of the BMI method from the Employee class
        # Add a few more assertEquals
        self.assertEquals(1, 1)
        pass

    def test_tax(self):
        # Complete this test of the Tax method from the Employee class
        # Add a few more assertEquals
        self.assertEquals(1, 1)
        pass

    def test_salary(self):
        # Complete this test of the getSalary method from the Employee class
        # Add a few more assertEquals
        self.assertEquals(1, 1)
        pass

    def test_print(self):
        # Complete this test of the __str__ method from the Employee class
        # Add a few more assertEquals
        self.assertEquals(1, 1)
        pass


if __name__ == "__main__":
    unittest.TestCase()
