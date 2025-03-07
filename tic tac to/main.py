#Write a Python Program to create a Tic Tac Toe game. You can use different modules and functions to create this game. Make sure that you print the board after every move.

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
'4': ' ' , '5': ' ' , '6': ' ' ,
'1': ' ' , '2': ' ' , '3': ' ' }

''' We will have to print the updated board after every move in the game and

thus we will make a function in which we'll define the printBoard function

so that we can easily print the board everytime by calling this function. '''
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])




def game():
    turn='X'
    count=0
    for i in range (10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")
        move = input()
        if theBoard[move] == ' ':
           theBoard[move] = turn
           count += 1
        else:
           print("That place is already filled.\nMove to which place?")
           continue
        if count>=5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
               printBoard(theBoard)
               print("\nGame Over.\n")
               print(" **** " +turn + " won. ****")
               break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\n Game Over. \n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\n Game Over. \n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\n Game Over. \n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle side
                printBoard(theBoard)
                print("\n Game Over. \n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\n Game Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # down the diagonal side
                printBoard(theBoard)
                print("\n Game Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # down the diagonal side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
        if turn =='X':
           turn = 'O'
        else:
           turn = 'X'



if __name__ == "__main__":
    game()