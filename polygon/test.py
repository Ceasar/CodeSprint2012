import unittest

import sol


class TestSquare(unittest.TestCase):
  def setUp(self):
    self.poly = [(0, 0), (0, 10), (10, 10), (10, 0)]

  def test_in(self):
    self.assertTrue(sol.in_poly(self.poly, (5, 5)))

  def test_out(self):
    self.assertFalse(sol.in_poly(self.poly, (0, 100)))
    self.assertFalse(sol.in_poly(self.poly, (0, -100)))
    self.assertFalse(sol.in_poly(self.poly, (20, 20)))
  
  def test_vertices(self):
    for point in self.poly:
      self.assertTrue(sol.in_poly(self.poly, point))

  def test_edges(self):
    self.assertTrue(sol.in_poly(self.poly, (9, 5)))
    self.assertTrue(sol.in_poly(self.poly, (10, 5)))
    self.assertFalse(sol.in_poly(self.poly, (11, 5)))

    self.assertTrue(sol.in_poly(self.poly, (5, 1)))
    self.assertTrue(sol.in_poly(self.poly, (5, 0)))
    self.assertFalse(sol.in_poly(self.poly, (5, -1)))

    self.assertFalse(sol.in_poly(self.poly, (-1, 5)))
    self.assertTrue(sol.in_poly(self.poly, (0, 5)))
    self.assertTrue(sol.in_poly(self.poly, (1, 5)))



class TestTriangle(unittest.TestCase):
  def setUp(self):
    self.poly = [(0, 0), (10, 10), (20, 0)]

  def test_in(self):
    self.assertTrue(sol.in_poly(self.poly, (10, 1)))
    self.assertTrue(sol.in_poly(self.poly, (3, 3)))
    self.assertTrue(sol.in_poly(self.poly, (18, 1)))

  def test_out(self):
    self.assertFalse(sol.in_poly(self.poly, (0, 10)))
    self.assertFalse(sol.in_poly(self.poly, (20, 10)))
  
  def test_vertices(self):
    for point in self.poly:
      self.assertTrue(sol.in_poly(self.poly, point))

  def test_edges(self):
    self.assertTrue(sol.in_poly(self.poly, (5, 4)))
    self.assertTrue(sol.in_poly(self.poly, (5, 5)))
    self.assertFalse(sol.in_poly(self.poly, (5, 6)))

    self.assertTrue(sol.in_poly(self.poly, (15, 4)))
    self.assertTrue(sol.in_poly(self.poly, (15, 5)))
    self.assertFalse(sol.in_poly(self.poly, (15, 6)))

  

if __name__ == "__main__":
  unittest.main()
