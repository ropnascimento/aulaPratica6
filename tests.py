import unittest

def teste(x):
  return x + 3

class unitTest(unittest.TestCase):
  def testEquals(self):
    self.assertEqual(teste(3),6)
    
if __name__ == '__main__':
  unittest.main()
