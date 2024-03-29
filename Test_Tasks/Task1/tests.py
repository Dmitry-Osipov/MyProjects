import unittest
from Test_Tasks.Task1.geometry import Circle, Triangle


class TestFigures(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertEqual(round(circle.find_area(), 1), 78.5)

    def test_triangle_area(self):
        square_triangle = Triangle(3, 4, 5)
        self.assertEqual(square_triangle.find_area(), 6.0)
        simple_triangle = Triangle(7.2, 3.8, 8.6)
        self.assertEqual(round(simple_triangle.find_area(), 2), 13.54)

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            circle1 = Circle(-5.3)._check_figure()

        with self.assertRaises(ValueError):
            circle2 = Circle(5)
            circle2.radius = [1, 2]

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            triangle1 = Triangle(1, 20, 4)._check_figure()

        with self.assertRaises(ValueError):
            triangle2 = Triangle(3, 4, 5)
            triangle2.a = 250


if __name__ == '__main__':
    unittest.main()
