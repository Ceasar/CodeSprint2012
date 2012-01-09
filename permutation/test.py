import unittest

import sol


class Test(unittest.TestCase):
  def test_chunk(self):
    got = [r for r in sol.chunk((0, 1, 2), 2)]
    expected = [(0, 1), (1, 2)]
    self.assertEqual(got, expected)

  def test_score(self):
    v = [[0, 4, 5], [2, 0, -2], [0, 0, 0]]
    got = sol.score((0, 1, 2), v)
    expected = 2
    self.assertEqual(got, expected)
    

if __name__ == "__main__":
  unittest.main()
