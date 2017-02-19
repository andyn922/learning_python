from random import randint
import argparse
import glob
import functions as fn

parser = argparse.ArgumentParser(description='Simple password generator')
parser.add_argument('--count', type=int, default='5',
                    help='number of password(s) to return')
args = parser.parse_args()

wordlists = glob.glob('wordlists//*.txt')

## Main

for i in range(0, args.count):
    got_word = fn.get_word(wordlists)
    got_int = fn.get_int()
    print(got_word + '#' + got_int)
