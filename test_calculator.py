# https://github.com/maralvar/lab10-MA-AM.git
# Partner 1: Mario A Alvarez
# Partner 2: Atreyu Morales

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
     def test_add(self): # 3 assertions

         self.assertEqual(add(5, 5), 10)


         self.assertEqual(add(-5, -5), -10)


         self.assertAlmostEqual(add(2.7, 5.6), 8.3)





     def test_subtract(self): # 3 assertions

         self.assertEqual(sub(5, 5), 0)

         self.assertEqual(sub(-5, -5), 0)

         self.assertAlmostEqual(sub(2.7, 5.6), -2.9)


    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code
    def test_multiply(self):
        self.assertEqual(mul(2, 5), 10)
        self.assertEqual(mul(-2, 5), -10)
        self.assertAlmostEqual(mul(2.5,5),12.5)

    # def test_divide(self): # 3 assertions
    #     fill in code
    def test_divide(self):
        self.assertRaises(ZeroDivisionError, div, 0, 5)
        self.assertAlmostEqual(div(4, 10), 2.5)
        self.assertEqual(div(1, -5), -5)
    # ##########################

    ######## Partner 2
     def test_divide_by_zero(self): # 1 assertion

         with self.assertRaises(ZeroDivisionError):
            div(5, 0)


     def test_logarithm(self): # 3 assertions

        self.assertEqual(log(1, 10), 0)

        self.assertEqual(log(1, math.e), 0)

        self.assertEqual(log(math.e, math.e), 1)




     def test_log_invalid_base(self): # 1 assertion

        with self.assertRaises(ValueError):

            log(5, 0)

    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    # def test_hypotenuse(self): # 3 assertions
    #     fill in code
    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(1, 1), math.sqrt(2))
        self.assertEqual(hypotenuse(5, 0), 5)

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(3), math.sqrt(3))
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()