__author__ = 'Dorota'

import unittest
import funkcje_digramy

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.corp = [["aba", "ba"],["nanana", "das", "fef", "ggg"],["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh"]]
        self.nouns = set(["das", "nanana", "ggg", "aa", "bb", "dd", "ee", "ff"])

    def test_find(self):
        all_digrams = funkcje_digramy.find_all_digrams(self.corp, self.nouns)
        self.assertEqual(["nanana das", "aa bb", "dd ee", "ee ff"], all_digrams)


if __name__ == '__main__':
    unittest.main()
