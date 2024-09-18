import unittest

class AreaTest(unittest.TestCase):

    def test_square(self):
        self.assertEqual(squareArea(4), 16.0)

    def test_rec(self):
        pass

def squareArea(s : float) -> float:
    """
        Parameters:
              s (float): Side length of the square.
    """
    return s * s

def rectangleArea(w : float, h : float) -> float:
    """
        Parameters:
            w (float): Width of the rectangle.
            h (float): Height of the rectangle.
    """
    # Complete this method
    pass

def triangleArea(b : float, h: float) -> float:
    """
        Parameters:
              b (float): Base of the triangle.
              h (float): Height of the triangle.
    """
    # Complete this method
    pass

def pentagonArea(a : float) -> float:
    """
        Parameteres:
            a (float): Side length of the pentagon.
    """
    # Complete this method
    pass

if __name__ == "__main__":
    unittest.main()