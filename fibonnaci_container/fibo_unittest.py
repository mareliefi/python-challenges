import unittest
import fibonnaci

class testFibonacci_operator(unittest.TestCase):

  def testOperationSuccess(self):
    '''Tests that operation returns correctly test1'''
    self.assertEqual(fibonnaci.generate_fibonnaci_up_to_n(1),0)

  def testOperationSuccess2(self):
    '''Tests that operation returns correctly test2'''
    self.assertEqual(fibonnaci.generate_fibonnaci_up_to_n(10),[0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

  def testOperationSuccess3(self):
    '''Tests that operation returns correctly test3'''
    self.assertEqual(fibonnaci.generate_fibonnaci_up_to_n(2),[0, 1])

  def testOperationSuccess4(self):
    '''Tests that operation returns correctly test4'''
    self.assertEqual(fibonnaci.generate_fibonnaci_up_to_n(5),[0, 1, 1, 2, 3])
    

TestSuite = unittest.TestSuite()
TestSuite.addTest(testFibonacci_operator("testOperationSuccess"))
TestSuite.addTest(testFibonacci_operator("testOperationSuccess2"))
TestSuite.addTest(testFibonacci_operator("testOperationSuccess3"))
TestSuite.addTest(testFibonacci_operator("testOperationSuccess4"))
runner = unittest.TextTestRunner()
runner.run(TestSuite)
