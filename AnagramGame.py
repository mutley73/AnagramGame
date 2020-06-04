import random

subject = ''
while subject != '1' and subject != '2' and subject != '3':
    subject = input('\nWould you like birds, countries or colours?\nType 1 for birds, 2 for countries or 3 for colours: ')
if subject == '1':
    filename = 'birds.txt'
elif subject == '2':
    filename = 'countries.txt'
else:
    filename = 'colours.txt'

with open(filename,'r') as f:
    wl = f.read().splitlines()

w = (random.choice(wl))
l = list(w.upper())
random.shuffle(l)
sw = ''.join(l)
print('\nYou have chosen {}.\nYour letters are {}.'.format(filename[:-4],sw))

g = input('What is the word? ')
if g.upper() == w.upper():
    print('\n' + '-' * 33)
    print('Congratulations, that is correct!')
    print('-' * 33)
else:
    lc = len(w)
    print('\n' + '-' * (20 + lc))
    print('Wrong! The word is {}.'.format(w.upper()))
    print('-' * (20 + lc))