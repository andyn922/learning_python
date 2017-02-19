import random

def get_word(wordlists: list):

    chosen_wordlist = random.choice(wordlists)
    # print('chosen wl is: ' + chosen_wordlist)

    # import file and strip whitespace
    with open(chosen_wordlist) as file:
        wordlist = [line.rstrip('\n') for line in file]

    return random.choice(wordlist)

def get_int():
    return str(random.randint(1000, 9999))
