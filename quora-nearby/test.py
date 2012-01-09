import unittest

import sol


class Test(unittest.TestCase):
  def test_distance(self):
    got = sol.distance(0, 0, 3, 4)
    expected = 5
    self.assertEqual(got, expected)
    got = sol.distance(0, 0, 3, -4)
    expected = 5
    self.assertEqual(got, expected)
    got = sol.distance(0, 0, -3, -4)
    expected = 5
    self.assertEqual(got, expected)
    got = sol.distance(0, 0, -3, 4)
    expected = 5
    self.assertEqual(got, expected)


    

if __name__ == "__main__":
  unittest.main()
