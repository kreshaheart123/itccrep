import unittest
from ElectricBill import ElectricBill


class ElectircBillTest(unittest.TestCase):

    def __init__(self):
        # Complete the initialization of the ElectricBill object
        super().__init__()
        self.bill = ElectricBill()

    def test_VAT(self):
        # Complete this test of the VAT method from the ElectricBill class
        # Add a few more assertEquals
        self.assertEqual(1, 1)
        pass

    def test_consumption(self):
        # Complete this test of the consumption method from the ElectricBill class
        # Add a few more assertEquals
        self.assertEqual(1, 1)
        pass

    def test_partial(self):
        # Complete this test of the getSalary method from the Employee class
        # Add a few more assertEquals
        self.assertEqual(1, 1)
        pass

    def test_final(self):
        # Completet this test of the bill method from the ElectricBill class
        # Add a few more assertEquals
        self.assertEqual(1, 1)

    def test_print(self):
        # Complete this test of the __str__ method from the Employee class
        # Add a few more assertEquals
        self.assertEqual(1, 1)
        pass


if __name__ == "__main__":
    unittest.TestCase()
