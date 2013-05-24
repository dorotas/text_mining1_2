__author__ = 'Dorota'

import funkcje_digramy

corps = open('korpus_tm1.txt', 'r')
all_words_in_corps = map(lambda l: l.split(" "), corps.readlines())

list_of_nouns = open('lista_rzeczownikow.txt').read().split('\n')
set_of_nouns = set(list_of_nouns)

list_of_genitives = open('lista_dopelniaczy.txt').read().split('\n')
set_of_genitives = set(list_of_genitives)

dict_of_digrams = {}

funkcje_digramy.find_all_digrams(all_words_in_corps, set_of_nouns, set_of_genitives, dict_of_digrams)

