__author__ = 'Dorota'

import unittest
import funkcje_digramy

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.dict_of_digrams1 = {"one" : 4, "two" : 2}
        self.dict_of_digrams2 = {"one" : 4, "two" : 2}

    def test_digram_in(self):
        funkcje_digramy.common_bonus("one", self.dict_of_digrams1)
        self.dict_of_digrams2["one"] += 1
        self.assertEqual(self.dict_of_digrams2, self.dict_of_digrams1)

    def test_digram_not_in(self):
        funkcje_digramy.common_bonus("three", self.dict_of_digrams1)
        self.dict_of_digrams2["three"] = 1
        self.assertEqual(self.dict_of_digrams2, self.dict_of_digrams1)

if __name__ == '__main__':
    unittest.main()
