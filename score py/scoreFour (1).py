def printBoard(data):
    print('  1   2   3   4   5   6   7')
    print('+---+---+---+---+---+---+---+')
    for i in range(6):
        print('|   |   |   |   |   |   |   |')
        print('|', data[i][0], '|', data[i][1], '|', data[i][2], '|', data[i][3], '|', data[i][4], '|', data[i][5], '|',
              data[i][6], '|')
        print('|   |   |   |   |   |   |   |')
        print('+---+---+---+---+---+---+---+')


def dropPiece(data, name, piece):
    print('Your turn ', name)
    column = input('Select column: ')
    # Check for correct input
    while (not column.isnumeric() or int(column) < 1 or int(column) > 7 or data[0][int(column) - 1] != ' '):
        print('Please choose a correct number')
        column = input('Select column: ')

    column = int(column)

    for i in range(5, -1, -1):
        if (data[i][column - 1] == ' '):
            data[i][column - 1] = piece
            break


def checkWin(data):
    # Check the rows
    for row in range(0, 6):
        for i in range(0, 4):
            if (data[row][i] != ' '):
                if (data[row][i] == data[row][i + 1] == data[row][i + 2] == data[row][i + 3]):
                    return True
    # Check the columns
    for column in range(0, 7):
        for row in range(0, 3):
            for i in range(0, 4):
                if (data[row][column] != ' '):
                    if (data[row][column] == data[row + 1][column] == data[row + 2][column] == data[row + 3][column]):
                        return True
    # Check diagonal forward
    for row in range(0, 3):
        for i in range(0, 4):
            if (data[row][i] != ' '):
                if (data[row][i] == data[row + 1][i + 1] == data[row + 2][i + 2] == data[row + 3][i + 3]):
                    return True
    # Check diagonial backward
    for row in range(0, 3):
        for col in range(6, 2, -1):
            if (data[row][i] != ' '):
                if (data[row][col] == data[row + 1][col - 1] == data[row + 2][col - 2] == data[row + 3][col - 3]):
                    return True


# Stack operations
# To peek the latest winner
def peekWinner(winners):
    if (isEmpty(winners) == False):
        return winners[len(winners) - 1]
    return False


# To pop the latest winner
def popWinner(winners):
    if (isEmpty(winners) == False):
        return winners.pop(len(winners) - 1)
    return False


# To add the new winner
def addWinner(winners, winnerName):
    winners.append(winnerName)
    return winners


# To check if there is any winner
def isEmpty(winners):
    if (len(winners) == 0):
        return True
    return False


# To print all winners
def printWinners(winners):
    for i in range(len(winners) - 1, -1, -1):
        print(winners[i])


def main():
    data = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    # Enter player names
    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")

    pl1 = ['Pl1', 'x', player1]
    pl2 = ['Pl2', 'o', player2]

    hasWon = False

    printBoard(data)

    for turn in range(21):
        player = pl1
        dropPiece(data, player[0], player[1])
        printBoard(data)
        hasWon = checkWin(data)
        if (hasWon):
            print(player[2], 'wins!')
            addWinner(winners, player[2])
            break

        player = pl2
        dropPiece(data, player[0], player[1])
        printBoard(data)
        hasWon = checkWin(data)
        if (hasWon):
            print(player[2], 'wins!')
            addWinner(winners, player[2])
            break

        if (turn == 20):
            print('Game Over! Draw!')


# Driver code

# Winners stack
winners = []

print("Welcome to board game!")
while (True):
    print("1 - For latest winner name")
    print("2 - To print all winners")
    print("3 - To remove latest winner")
    print("4 - For new game")
    print("5 - To exit")
    op = int(input())
    if (op == 1):
        winner = peekWinner(winners)
        if (winner):
            print("latest winner is ", winner)
        else:
            print("No latest winner")
    elif (op == 2):
        printWinners(winners)
    elif (op == 3):
        winner = popWinner(winners)
        if (winner):
            print("latest winner is ", winner)
        else:
            print("No winners yet")
    elif (op == 4):
        main()
    else:
        print("Thanks for playing")
        break
