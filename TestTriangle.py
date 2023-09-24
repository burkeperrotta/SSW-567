# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""
import unittest
from Triangle import classifyTriangle
# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the
# framework
class TestTriangles(unittest.TestCase):
# define multiple sets of tests as functions with names that begin
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(7,7,4),'Isosceles','7,7,4 should be isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(4,7,7),'Isosceles','4,7,7 should be Isosceles')
    
    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(7,4,7),'Isosceles','7,4,7 should be Isosceles')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(7,5,11),'Scalene','7,5,11 should be scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(11,7,5),'Scalene','7,5,11 should be scalene')

    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(5,11,7),'Scalene','7,5,11 should be scalene')

    def testA201(self):
        self.assertEqual(classifyTriangle(201,120,90),'InvalidInput','201,120,90 should be InvalidInput')

    def testB201(self):
        self.assertEqual(classifyTriangle(90,201,120),'InvalidInput','90,201,120 should be InvalidInput')

    def testC201(self):
        self.assertEqual(classifyTriangle(120,90,201),'InvalidInput','120,90,201 should be InvalidInput')

    def testA0(self):
        self.assertEqual(classifyTriangle(0,5,5),'InvalidInput','0,5,5 should be InvalidInput')

    def testB0(self):
        self.assertEqual(classifyTriangle(5,0,5),'InvalidInput','5,0,5 should be InvalidInput')

    def testC0(self):
        self.assertEqual(classifyTriangle(5,5,0),'InvalidInput','5,5,0 should be InvalidInput')

    def testANotInt(self):
        self.assertEqual(classifyTriangle(5.0,5,5),'InvalidInput','5.0,5,5 should be InvalidInput')

    def testBNotInt(self):
        self.assertEqual(classifyTriangle(5,5.0,5),'InvalidInput','5,5.0,5 should be InvalidInput')

    def testCNotInt(self):
        self.assertEqual(classifyTriangle(5,5,5.0),'InvalidInput','5,5,5.0 should be InvalidInput')

    def testNotTriangleA(self):
        self.assertEqual(classifyTriangle(20,6,6),'NotATriangle','20,6,6 should be NotATriangle')

    def testNotTriangleB(self):
        self.assertEqual(classifyTriangle(6,20,6),'NotATriangle','6,20,6 should be NotATriangle')

    def testNotTriangleC(self):
        self.assertEqual(classifyTriangle(6,6,20),'NotATriangle','6,6,20 should be NotATriangle')




if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
