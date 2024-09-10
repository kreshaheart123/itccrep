import unittest

class ArithmeticTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5 + 5, add(5, 5))
    
    def test_add2(self):
        # Make it so that this line should not return an error
        # Do not change the values being supplied.
        self.assertEqual(1.05 + 1.05, add(1.05, 1.05))

    # Add additional tests for subtract, multiply, and divide

# Probably add new functions?

def add(x : int, y : int) -> int:
    assert type(x) == "int"
    assert type(y) == "int"
    return x + y

def subtract(x : int, y: int) -> int:
    # Assert parameters are int
    # Complete function
    return None

def multiply(x : int, y: int) -> int:
    # Assert parameters are int
    # Complete function
    return None

def divide(x : int, y: int) -> int:
    # Assert parameters are int
    # Complete function
    return None

if __name__ == "__main__":
    unittest.main()