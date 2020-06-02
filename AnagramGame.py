import random

subject = ''
while subject != '1' and subject != '2':
    subject = input('\nWould you like birds or countries?\nType 1 for birds or 2 for countries: ')
if subject == '1':
    filename = 'birds.txt'
elif subject == '2':
    filename = 'countries.txt'

with open(filename,'r') as f:
    wordlist = f.read().splitlines()

word = (random.choice(wordlist))
l = list(word.upper())
random.shuffle(l)
sw = ''.join(l)
print('\nYou have chosen {}.\nYour letters are {}.'.format(filename[:-4],sw))

guess = input('What is the word? ')
if guess.upper() == word.upper():
    print('\n' + '-' * 33)
    print('Congratulations, that is correct!')
    print('-' * 33)
else:
    lc = len(word)
    print('\n' + '-' * (20 + lc))
    print('Wrong! The word is {}.'.format(word.upper()))
    print('-' * (20 + lc))
