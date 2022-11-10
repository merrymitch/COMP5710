import unittest
import calculator
from datetime import datetime

class TestCalc(unittest.TestCase):
    def testSubtract_ValidInputs(self):
        self.assertEqual(2, calculator.subtract(4, 2), "Subtraction operation for 4-2 is = 2")

    def testSubtract_InvalidInputs(self):
        self.assertEqual("Input provided was invalid", calculator.subtract("Bad", 4), "Subtraction operation with strings is invalid")

    def testSubtract_InvalidInputs2(self):
        bad = {}
        bad['invalid'] = 'input'
        self.assertEqual("Something went wrong check inputs", calculator.subtract(bad, 3), "Subtraction operation with non-integers is invalid")

    def testSubtract_ExecutionTime(self):
        start = datetime.now()
        startTS = datetime.timestamp(start)
        calculator.subtract(7, 3)
        end = datetime.now()
        endTS = datetime.timestamp(end)
        self.assertGreaterEqual(0.001, endTS - startTS, "Subtraction operation should be fast")

    def testMultiplication_ValidInputs(self):
        self.assertEqual(20, calculator.multiply(4, 5), "Multiplication operation for 4*5 is = 20")
    
    def testMultiplication_InvalidInputs(self):
        self.assertEqual("Input provided was invalid", calculator.multiply("Bad", 8), "Multiplication operation with strings is invalid")

    def testMultiplication_InvalidInputs2(self):
        bad = {}
        bad['invalid'] = 'input'
        self.assertEqual("Something went wrong check inputs", calculator.multiply(bad, 2), "Multiplication operation with non-integers is invalid")
    
    def testMultiplication_ExecutionTime(self):
        start = datetime.now()
        startTS = datetime.timestamp(start)
        calculator.multiply(3, 2)
        end = datetime.now()
        endTS = datetime.timestamp(end)
        self.assertGreaterEqual(0.001, endTS - startTS, "Multiplication operation should be fast")

    def testDivision_ValidInputs(self):
        self.assertEqual(4, calculator.divide(12, 3), "Division operation for 12/3 is = 4")

    def testDivision_InvalidInputs(self):
        self.assertEqual("Input provided was invalid", calculator.divide("Bad", 12), "Division operation with strings is invalid")

    def testDivision_InvalidInputs2(self):
        bad = {}
        bad['invalid'] = 'input'
        self.assertEqual("Something went wrong check inputs", calculator.divide(bad, 1), "Division operation with non-integers is invalid")
    
    def testDivision_DivideByZero(self):
        self.assertEqual("Cannot divide by zero", calculator.divide(9, 0), "Division operation with denominator 0 is invalid")

    def testDivision_ExecutionTime(self):
        start = datetime.now()
        startTS = datetime.timestamp(start)
        calculator.divide(10, 5)
        end = datetime.now()
        endTS = datetime.timestamp(end)
        self.assertGreaterEqual(0.001, endTS - startTS, "Division operation should be fast")

if __name__ == '__main__': 
    unittest.main() 