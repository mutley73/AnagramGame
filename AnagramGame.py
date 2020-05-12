import random

wordlist = ('random', 'speaker', 'clippers', 'garage', 'rabbit', 'module', 'laptop', 'folder', 'fridge', 'printer')
word = (random.choice(wordlist)) #Select random word from wordlist
l = list(word) #Split word into characters
random.shuffle(l) #Shuffle characters
sw = ''.join(l) #Join shuffled characters

print('Make a word from the letters {}.'.format(sw))
guess = input('What is the word? ')

if guess.lower() == word:
    print('\n' + '-' * 33)
    print('Congratulations, that is correct!')
    print('-' * 33)
else:
    lc = len(word)
    print('\n' + '-' * (20 + lc))
    print('Wrong! The word is {}.'.format(word))
    print('-' * (20 + lc))