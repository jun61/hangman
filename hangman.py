def hangman(word):
    wrong = 0
    stages = ['',
            '___________',
            '|                        ',
            '|                        ',
            '|          |             ',
            '|          0             ',
            '|         /|\            ',
            '|         / \            ',
            '|                        ']
    rletters = list(word)
    borad = ['_'] * len(word)
    win = False
    print('ハングマンへようこそ')

    while wrong < len(stages) -1:
        print('\n')
        msg = '1文字入力してね'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong += 1
            print(' '.join(stages[0:e]))
        if '_' not in board:
                print('you win!!')
                print(' '.join(board))
                win = True
                break
    if not win:
            print('\n'.join(stage[0:wrong+1]))
            print('you lose!正解は　{}.'.format(word))
hangman('cat')
