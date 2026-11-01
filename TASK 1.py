import random

board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

def display_board():
    print()
    for i in range(3):
        print(" " + " | ".join(board[i]))
        if i < 2:
            print("---+---+---")
    print()

def check_winner(player):
  
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

   
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_draw():
    for row in board:
        for cell in row:
            if '1' <= cell <= '9':
                return False
    return True

def make_move(position, player):
    if not (1 <= position <= 9):
        return False

    row = (position - 1) // 3
    col = (position - 1) % 3

    if board[row][col] not in ('X', 'O'):
        board[row][col] = player
        return True

    return False

def minimax(computer_turn):
    if check_winner('O'):
        return 10
    if check_winner('X'):
        return -10
    if is_draw():
        return 0

    if computer_turn:
        best_score = -1000
        for i in range(1, 10):
            row = (i - 1) // 3
            col = (i - 1) % 3

            if '1' <= board[row][col] <= '9':
                old_value = board[row][col]
                board[row][col] = 'O'

                score = minimax(False)

                board[row][col] = old_value
                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = 1000
        for i in range(1, 10):
            row = (i - 1) // 3
            col = (i - 1) % 3

            if '1' <= board[row][col] <= '9':
                old_value = board[row][col]
                board[row][col] = 'X'

                score = minimax(True)

                board[row][col] = old_value
                if score < best_score:
                    best_score = score
        return best_score

def computer_move(optimal_mode):
    available = []
    for i in range(1, 10):
        row = (i - 1) // 3
        col = (i - 1) % 3
        if '1' <= board[row][col] <= '9':
            available.append(i)

    if not available:
        return

    if not optimal_mode:
        choice = random.choice(available)
        make_move(choice, 'O')
        print(f"Computer chose position {choice}")
        return

    best_position = -1
    best_score = -1000

    for position in available:
        row = (position - 1) // 3
        col = (position - 1) % 3

        old_value = board[row][col]
        board[row][col] = 'O'

        score = minimax(False)

        board[row][col] = old_value

        if score > best_score:
            best_score = score
            best_position = position

    make_move(best_position, 'O')
    print(f"Computer chose position {best_position}")

def main():
    optimal_mode = True

    print("===== TIC-TAC-TOE =====")
    print("You are X. Computer is O.")
    print("Choose positions from 1 to 9.")

    display_board()

    while True:
        try:
            position = int(input("Enter your position: "))
        except ValueError:
            print("Invalid position! Try again.")
            continue

        if not make_move(position, 'X'):
            print("Invalid position! Try again.")
            continue

        display_board()

        if check_winner('X'):
            print("Congratulations! You win!")
            break

        if is_draw():
            print("The game is a draw!")
            break

        computer_move(optimal_mode)
        display_board()

        if check_winner('O'):
            print("Computer wins!")
            break

        if is_draw():
            print("The game is a draw!")
            break

if __name__ == "__main__":
    main()
