import unittest

import sol


class Test(unittest.TestCase):
  def test_normalize_email(self):
    got = sol.normalize_email("BuGS@BuNnY.CoM")
    expected = "bugs@bunny.com"
    self.assertEqual(got, expected)

    got = sol.normalize_email("bugs.1@bunny.com")
    expected = "bugs1@bunny.com"
    self.assertEqual(got, expected)

    got = sol.normalize_email("bugs+10@bunny.com")
    expected = "bugs@bunny.com"
    self.assertEqual(got, expected)

  def test_normalize_address(self):
    got = sol.normalize_address("123 SeSAME street")
    expected = "123 sesame street"
    self.assertEqual(got, expected)

    got = sol.normalize_address("123 Sesame st.")
    expected = "123 sesame street"
    self.assertEqual(got, expected)

  def test_normalize(self):
    record = {
        'email': 'BuGS.1+10@BuNnY.cOm',
        'address': "123 SeSaME sT.",
        'city': 'NeW YoRk',
        'state': 'illinois'
        }
    sol.normalize(record)
    got = record
    expected = {
        'email': 'bugs1@bunny.com',
        'address': "123 sesame street",
        'city': 'new york',
        'state': 'il'
        }
    self.assertEqual(got, expected)
    

if __name__ == "__main__":
  unittest.main()
