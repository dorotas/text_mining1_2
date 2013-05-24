__author__ = 'Dorota'

import unittest
import funkcje_digramy

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.set_of_gen = set(["wewa", "waki", "maki"])
        self.dict_of_dig1 = {"wewa waki" : 3, "wawa. waw" : 2}
        self.dict_of_dig2 = {"wewa waki" : 3, "wawa. waw" : 2}

    def test_is_genitive(self):
        funkcje_digramy.is_genitive_bonus("wewa waki", self.set_of_gen, self.dict_of_dig1)
        self.dict_of_dig2["wewa waki"] += 3
        self.assertEqual(self.dict_of_dig2, self.dict_of_dig1)

    def test_is_not_genitive(self):
        funkcje_digramy.is_genitive_bonus("wea waki", self.set_of_gen, self.dict_of_dig1)
        self.assertEqual(self.dict_of_dig2, self.dict_of_dig1)

if __name__ == '__main__':
    unittest.main()
