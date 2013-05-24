__author__ = 'Dorota'

from operator import itemgetter
import heapq
import collections

def find_all_digrams(corps, set_of_nouns, set_of_genitives, dict_of_digrams):
    result = open("digrams_result.txt", 'w')
    set_of_rare_nouns = least_common_values(set_of_nouns, 1000)
    for line in range(len(corps)) :
        for nr_elementu in range(len(corps[line])):
            word_last = corps[line][nr_elementu]
            if nr_elementu > 0 :
                word_first = corps[line][nr_elementu-1]
                if word_last in set_of_nouns and word_first in set_of_nouns:
                    key = word_first + " " + word_last
                    common_bonus(key, dict_of_digrams)
                    is_genitive_bonus(key, set_of_genitives, dict_of_digrams)
                    is_rare_bonus(key, set_of_rare_nouns, dict_of_digrams)
    for k in dict_of_digrams :
        result.write(k + ' ' + str(dict_of_digrams[k]) + '\n')
    result.close()

def common_bonus(digram, dict_of_digrams):
    if dict_of_digrams.has_key(digram):
        dict_of_digrams[digram] += 1
    else:
        dict_of_digrams[digram] = 1

def is_genitive_bonus(digram, set_of_genitives, dict_of_digrams):
    pair = digram.split(" ")
    if pair[0] in set_of_genitives and pair[1] in set_of_genitives:
        dict_of_digrams[digram] += 3


def least_common_values(array, to_find):
    list_of_rare_nouns = []
    counter = collections.Counter(array)
    tuple = heapq.nsmallest(to_find, counter.items(), key=itemgetter(1))
    for k in tuple:
        list_of_rare_nouns.append(k[0])
        set_of_rare_nouns = set(list_of_rare_nouns)
        return set_of_rare_nouns

def is_rare_bonus(digram, set_of_rare, dict_of_digrams):
    pair = digram.split(" ")
    if pair[0] in set_of_rare and pair[1] in set_of_rare:
        dict_of_digrams[digram] +=5

