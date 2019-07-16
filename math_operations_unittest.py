import unittest
import mathematical_operations 

class testMathematics_operations(unittest.TestCase):

  def testOperationsReturnSuccess(self):
    '''Tests that operations return correctly'''
    grades = [0, 80, 22, 33, 61, 15, 100, 90, 50, 22]
    self.assertEqual(mathematical_operations.grades_sum(grades),473)
    self.assertEqual(mathematical_operations.grades_mean(grades),47.3)
    self.assertEqual(mathematical_operations.grades_median(grades),41.5)
    self.assertEqual(mathematical_operations.grades_mode(grades),22)
    self.assertEqual(mathematical_operations.grades_variance(grades),10630.1)
    variance = mathematical_operations.grades_variance(grades)
    self.assertEqual(mathematical_operations.grades_std_deviation(variance),103.1)

  def testOperationsReturnCorrect(self):
    '''Tests that operations return correctly'''
    grades = [2, 0, 88, 32, 55, 0, 90]
    self.assertEqual(mathematical_operations.grades_sum(grades),267)
    self.assertEqual(mathematical_operations.grades_mean(grades),38.14)
    self.assertEqual(mathematical_operations.grades_median(grades),32)
    self.assertEqual(mathematical_operations.grades_mode(grades),0)
    self.assertEqual(mathematical_operations.grades_variance(grades),9712.86)
    variance = mathematical_operations.grades_variance(grades)
    self.assertEqual(mathematical_operations.grades_std_deviation(variance),98.55)


TestSuite = unittest.TestSuite()
TestSuite.addTest(testMathematics_operations("testOperationsReturnSuccess"))
TestSuite.addTest(testMathematics_operations("testOperationsReturnCorrect"))
runner = unittest.TextTestRunner()
runner.run(TestSuite)
