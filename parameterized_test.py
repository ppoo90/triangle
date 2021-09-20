import unittest
from triangle import is_triangle

class TriangleTest(unittest.TestCase):
    valid_triangles = [
        (1, 1, 1),
        (3, 4, 5),
        (3, 4, 6),
        (8, 10, 12)
    ]

    def test_valid_triangle(self):
        """loop over each set of test data"""
        for a, b, c in self.valid_triangles:
            with self.subTest():
                msg = f"side lengths ({a},{b},{c})"
                self.assertTrue(is_triangle(a, b, c), msg)

    def test_not_triangle(self):
        self.assertFalse( is_triangle(21, 10, 10) )
        self.assertFalse( is_triangle(2, 1, 1) )   # borderline case
        self.assertFalse( is_triangle(6, 10, 4) )  # borderline case
        self.assertFalse( is_triangle(6, 20, 4) )
        self.assertFalse(is_triangle(5, 1, 1))

    def test_invalid_argument_raises_exception(self):
        """any non-positive argument should raise ValueError"""
        with self.assertRaises(ValueError):
            b2 = is_triangle(1, 0, 2)  # this should raise exception
            b1 = is_triangle(-1, 2, 2)

        with self.assertRaises(ValueError):
            b2 = is_triangle(1,  0, 2)
            b1 = is_triangle(1, -1, 2)

        with self.assertRaises(ValueError):
            b1 = is_triangle(1, 2, -1)
            b2 = is_triangle(1, 2,  0)

        with self.assertRaises(ValueError):
            b1 = is_triangle( -1, -1, -1)
            b2 = is_triangle( 0, 0, 0)

