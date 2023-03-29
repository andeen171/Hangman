import random


def play_game(attempts_qnty, possible_words) -> bool:
    word = random.choice(possible_words)
    letters = {letter: '-' for letter in word}
    attempts = []
    while attempts_qnty > 0:
        hint = ''.join(letters[c] for c in word)
        if hint == word:
            print('You guessed the word {}!'.format(word))
            print('You survived!')
            return True

        print(hint)
        letter = input('Input a letter: ')

        if len(letter) != 1:
            print('Please, input a single letter')
            continue

        if not letter.isalpha() or not letter.islower():
            print('Please, enter a lowercase letter from the English alphabet.')
            continue

        if letter in attempts:
            print('You\'ve already guessed this letter')
            continue

        attempts.append(letter)

        if letter in letters:
            letters[letter] = letter
        else:
            attempts_qnty -= 1
            print(f'That letter doesn\'t appear in the word.  # {attempts_qnty} attempts')

    else:
        print('You lost!')
        return False


def main():
    possible_words = ('python', 'java', 'swift', 'javascript')
    attempts_qnty = 8
    results = []
    print(f'H A N G M A N  # {attempts_qnty} attempts\n')

    while True:
        command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        if command == 'play':
            result = play_game(attempts_qnty, possible_words)
            results.append(result)
        elif command == 'results':
            print(f'You won: {results.count(True)} times.\n'
                  f'You lost: {results.count(False)} times.')
        else:
            print('Bye!')
            break


if __name__ == '__main__':
    main()
