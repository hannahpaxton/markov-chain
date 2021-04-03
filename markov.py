"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split() #list

    words.append(None) #stopping point for when we should stop creating Markov text. 

    for i in range(len(words) - 2): #number of words
        bigram = (words[i], words[i+1])
 
        #check if in dictionary. if not in dictionary, give the key a value of an empty list; if empty list, append to the list
        if bigram not in chains: #guarantees that the keypair is in the dict
            chains[bigram] = [] # we put this in the dictonary key: bigram value: empty list. we add empty list as a default, when it's the first time being added to the dict

        chains[bigram].append(words[i+2]) # append words to the value

    return chains


def make_text(chains):
    """Return text from chains."""
#list the keys from your dictionary; here it's a tuple so convert to list
    key = choice(list(chains.keys())) #here we are getting a list of all tuples and getting 1 random tuple in our key; since we did import from choice at the top, just call choice fn
    words = [key[0], key[1]] #unpacking to our list

#grab a random word from the value of the key
    random_word = choice(chains[key])

    while random_word is not None: # last tuple will be Sam, None
        key = (key[1], random_word)
        words.append(random_word)
        random_word = choice(chains[key])

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
