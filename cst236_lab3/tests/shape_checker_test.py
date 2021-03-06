"""
Test for source.shape_checker
"""
from ReqTracer import requirements
from source.shape_checker import get_triangle_type, get_quadrilateral_type
from unittest import TestCase

class TestShapeType(TestCase):
    
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1.003, 1.003, 1.003)
        self.assertEqual(result, 'equilateral')

        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

        result = get_triangle_type(1, 1, 3)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_invalid(self):
        result = get_triangle_type(1, 'a', 3)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003','#0004'])
    def test_get_corners_and_sides_right_angles(self):
        result = get_quadrilateral_type(3, 3, 3, 3, 90, 90, 90, 90)
        self.assertEqual( result, "square")

    def test_get_corners_and_sides_right_angles2(self):
        result = get_quadrilateral_type(1, 3.14159, 1, 3.14159, 90, 90, 90, 90)
        self.assertEqual( result, "rectangle")

    def test_get_corners_and_sides_disconnected(self):
        result = get_quadrilateral_type(2, 5, 2, 5, 100, 90, 90, 90)
        self.assertEqual( result, "disconnected")
    @requirements(['#0005'])
    def test_get_quad_rhombus(self):
        result = get_quadrilateral_type(5, 5, 5, 5, 100.5, 79.5, 100.5, 79.5)
        self.assertEqual( result, "rhombus")

    def test_get_corners_and_sides_disconnected2(self):
        result = get_quadrilateral_type(5, 1, 5, 5, 100, 80, 100, 80)
        self.assertEqual( result, "disconnected")

    def test_get_triangle(self):
        ret = get_triangle_type(-5, 5, 5)
        self.assertEqual(ret, "invalid")

        my_dict = {
                    1:1,
                    2:2,
                    3:3,
                   }
        ret2 = get_triangle_type(my_dict)
        self.assertEqual(ret2, "scalene")

        my_list = [5,4,6]
        ret = get_triangle_type(my_list)
        self.assertEqual(ret, "scalene")

    def test_get_quad(self):
        ret = get_quadrilateral_type('h', 5, 5, 4)
        self.assertEqual(ret, "invalid")

        ret2 = get_quadrilateral_type(5, 5, 5, 4, 90, 90, 90, 'f')
        self.assertEqual(ret2, "invalid")

        ret2 = get_quadrilateral_type(1, 5, 5, 9, 90, 90, 90, 90)
        self.assertEqual(ret2, "disconnected")
        
        





        
