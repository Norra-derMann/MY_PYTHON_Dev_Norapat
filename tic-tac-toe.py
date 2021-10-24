#use dictionary for declare board
thisBoard = {'top-L' : '', 'top-M' : '', 'top-R' : '',
         'mid-L' : '', 'mid-M' : '', 'mid-R': '',
         'low-L' : 'X', 'low-M' : '', 'low-R': 'X'}
turn = 'O'
status = True
#store win case by using tuple
WINS = (('top-L','top-M','top-R'),('mid-L','mid-M','mid-R'),('low-L','low-M','low-R'), #horizontal
        ('top-L','mid-L','low-L'),('top-M','mid-M','low-M'),('top-R','mid-R','low-R'), #vertical
        ('top-L','mid-M','low-R'),('top-R','mid-M','low-L'))#diagonal
def printBoard(board):
    print(thisBoard['top-L'] + '|' + thisBoard['top-M'] + '|' + thisBoard['top-R'])
    print('-+-+-')
    print(thisBoard['mid-L'] + '|' + thisBoard['mid-M'] + '|' + thisBoard['mid-R'])
    print('-+-+-')
    print(thisBoard['low-L'] + '|' + thisBoard['low-M'] + '|' + thisBoard['low-R'])

def checkWinner(board,turn):
    for win in WINS:
        if((board[win[0]] == board[win[1]] == board[win[2]]) and board[win[0]] != '' and board[win[1]] != '' and board[win[2]] != ''):
            print('Winner is ' + turn + '!!!')
            print(win)
            return True
    return False
        
def swapPlayer(player):
    if player == 'X' :
        return 'O'
    else: 
        return 'X'
    
while(status) : 
    printBoard(thisBoard)
    print('Turn for '  + turn +'. Move on which space?')
    move = input()
    if(thisBoard[move] == ''):
        thisBoard[move] = turn
        if(checkWinner(thisBoard,turn)):
            printBoard(thisBoard)
            break;
        else:
            turn = swapPlayer(turn)
    else : 
        print('Please select new position')