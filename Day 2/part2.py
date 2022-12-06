rock_val = 1
paper_val = 2
scissors_val = 3

scoring = {"Win": 6, "Loss": 0, "Draw": 3}
move_values = {"Rock": 1, "Paper": 2, "Scissors": 3}
opponent = {"A": "Rock", "B": "Paper", "C": "Scissors"}
player_moves = {"X": "Loss", "Y": "Draw", "Z": "Win"}

win = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
lose = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}


def player_win(opponent_move, player_move):
    if opponent_move == "Rock":
        if player_move == "Paper":
            return "Win"
        elif player_move == "Scissors":
            return "Loss"
        else:
            return "Draw"
    elif opponent_move == "Paper":
        if player_move == "Scissors":
            return "Win"
        elif player_move == "Rock":
            return "Loss"
        else:
            return "Draw"
    elif opponent_move == "Scissors":
        if player_move == "Rock":
            return "Win"
        elif player_move == "Paper":
            return "Loss"
        else:
            return "Draw"


def play_game():
    game_input = ""
    game_list = []
    score = 0
    player_total = 0
    with open("input2.txt", encoding="utf-8") as f:
        game_input = f.read().strip()
    game_list = game_input.split("\n")
    for game in game_list:
        move = game.split()
        print(move)
        player_move = player_moves[move[1]]
        if player_move == "Win":
            winning_move = win[opponent[move[0]]]
            player_total = (
                player_total + move_values[winning_move] + scoring[player_move]
            )
        elif player_move == "Loss":
            losing_move = lose[opponent[move[0]]]
            player_total = (
                player_total + move_values[losing_move] + scoring[player_move]
            )
        else:
            player_total = (
                player_total + move_values[opponent[move[0]]] + scoring["Draw"]
            )
    print(player_total)


def main():
    play_game()


if __name__ == "__main__":
    main()
