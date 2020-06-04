import random

game = True

while game:
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
        wordlist = f.read().splitlines()

    word = (random.choice(wordlist))
    word_as_list = list(word.upper())
    random.shuffle(word_as_list)
    anagram = ' '.join(word_as_list)
    print('\nYou have chosen {}.\nYour letters are {}'.format(filename[:-4], anagram))

    guess = input('What is the word? ')
    if guess.upper() == word.upper():
        print('\n' + '-' * 35)
        print(' Congratulations, that is correct! ')
        print('-' * 35)
    else:
        word_length = len(word)
        print('\n' + '-' * (22 + word_length))
        print(' Wrong! The word is {}. '.format(word.upper()))
        print('-' * (22 + word_length))

    choice = input('\nPlay again? Enter Y or N: ').upper()
    if choice == 'Y':
        game = True
    else:
        break