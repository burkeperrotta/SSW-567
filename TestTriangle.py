"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""
import unittest
from triangle import classify_triangle
# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the
# framework
class TestTriangles(unittest.TestCase):
    """ class with all tests """
# define multiple sets of tests as functions with names that begin
    def testRightTriangleA(self):
        """ tests right triangle """
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        """tests right triangle  """
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        """tests right triangle  """
        self.assertEqual(classify_triangle(4,5,3),'Right','4,5,3 is a Right triangle')

    def testEquilateralTriangles(self):
        """test equiliateral triangle """
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTriangleA(self):
        """test icosceles triangle """
        self.assertEqual(classify_triangle(7,7,4),'Isosceles','7,7,4 should be isosceles')

    def testIsoscelesTriangleB(self):
        """test icosceles triangle """
        self.assertEqual(classify_triangle(4,7,7),'Isosceles','4,7,7 should be Isosceles')

    def testIsoscelesTriangleC(self):
        """test icosceles triangle """
        self.assertEqual(classify_triangle(7,4,7),'Isosceles','7,4,7 should be Isosceles')

    def testScaleneTriangleA(self):
        """ tests scalene triangle"""
        self.assertEqual(classify_triangle(7,5,11),'Scalene','7,5,11 should be scalene')

    def testScaleneTriangleB(self):
        """tests scalene triangle """
        self.assertEqual(classify_triangle(11,7,5),'Scalene','7,5,11 should be scalene')

    def testScaleneTriangleC(self):
        """ tests scalene triangle"""
        self.assertEqual(classify_triangle(5,11,7),'Scalene','7,5,11 should be scalene')

    def testA201(self):
        """tests input upper limit """
        self.assertEqual(classify_triangle(201,120,90),\
        'InvalidInput','201,120,90 should be InvalidInput')

    def testB201(self):
        """tests input upper limit """
        self.assertEqual(classify_triangle(90,201,120),'InvalidInput',\
        '90,201,120 should be InvalidInput')

    def testC201(self):
        """tests input upper limit """
        self.assertEqual(classify_triangle(120,90,201),'InvalidInput',\
        '120,90,201 should be InvalidInput')

    def testA0(self):
        """tests zero as input """
        self.assertEqual(classify_triangle(0,5,5),'InvalidInput','0,5,5 should be InvalidInput')

    def testB0(self):
        """tests zero as input """
        self.assertEqual(classify_triangle(5,0,5),'InvalidInput','5,0,5 should be InvalidInput')

    def testC0(self):
        """tests zero as input """
        self.assertEqual(classify_triangle(5,5,0),'InvalidInput','5,5,0 should be InvalidInput')

    def testANotInt(self):
        """ tests not integer inputs """
        self.assertEqual(classify_triangle(5.0,5,5),'InvalidInput','5.0,5,5 should be InvalidInput')

    def testBNotInt(self):
        """ tests not integer inputs"""
        self.assertEqual(classify_triangle(5,5.0,5),'InvalidInput','5,5.0,5 should be InvalidInput')

    def testCNotInt(self):
        """ tests not integer inputs"""
        self.assertEqual(classify_triangle(5,5,5.0),'InvalidInput','5,5,5.0 should be InvalidInput')

    def testNotTriangleA(self):
        """ tests invalid triangles """
        self.assertEqual(classify_triangle(20,6,6),'NotATriangle','20,6,6 should be NotATriangle')

    def testNotTriangleB(self):
        """tests invalid triangles """
        self.assertEqual(classify_triangle(6,20,6),'NotATriangle','6,20,6 should be NotATriangle')

    def testNotTriangleC(self):
        """tests invalid triangles """
        self.assertEqual(classify_triangle(6,6,20),'NotATriangle','6,6,20 should be NotATriangle')




if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
