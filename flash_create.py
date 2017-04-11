#!/usr/bin/env python

import sys
import os.path

from flash_common import *


if __name__ == '__main__':
    if os.path.isfile(WordData.words_db_file):
        word_data = WordData()

        print "total words:", len(word_data.words_dict)

        while True:
            spanish = raw_input('Enter Spanish:')
            if spanish == 'exit':
                word_data.write_db()
                sys.exit()
            if spanish in word_data.words_dict:
                print 'word already exists.'
                continue
            english = raw_input('Enter English:')
            word_data.add_word(spanish, english)






