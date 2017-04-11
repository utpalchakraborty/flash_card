#!/usr/bin/env python
import os
import sys
from flash_common import *


def get_next(wd, rev):
    """
    Gets the next question from the
    :param rev:
    :return:
    """
    s, e = wd.get_random()
    q, ans = e, s
    if rev:
        q, ans = s, e
    return q, ans, s, e


if __name__ == '__main__':
    print sys.argv
    reverse = False

    if 'reverse' in sys.argv:
        reverse = True

    if os.path.isfile(WordData.words_db_file):
        word_data = WordData()
        print "total words:", word_data.num_words
        done_words_begin = word_data.done_words()
        print '--------------------------------------------------------------------------------------------------------'
        print "done words:", len(done_words_begin)
        print done_words_begin
        print '--------------------------------------------------------------------------------------------------------'

        question, answer, spanish, english = get_next(word_data, reverse)
        while question is not None:
            response = raw_input(question + ":")
            if response.lower() == "exit":
                word_data.write_db()
                break
            if response.lower() == answer:
                print "Correct!!"
                word_data.modify_freq(spanish, 1)
            elif response == "?":
                print answer
            else:
                print str.format("Wrong! {} is {}", question, answer)
                word_data.modify_freq(spanish, -1)
            question, answer, spanish, english = get_next(word_data, reverse)

        word_data.write_db()
        print '--------------------------------------------------------------------------------------------------------'
        done_words_end = word_data.done_words()
        print "done words:", len(done_words_end)
        print done_words_end
        print '--------------------------------------------------------------------------------------------------------'
        print "done this time:", done_words_end.difference(done_words_begin)

