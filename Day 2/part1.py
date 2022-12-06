rock_val = 1
paper_val = 2
scissors_val = 3

scoring = {"Win": 6, "Loss": 0, "Draw": 3}
move_values = {"Rock": 1, "Paper": 2, "Scissors": 3}
opponent = {"A": "Rock", "B": "Paper", "C": "Scissors"}
player_moves = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}


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
        result = player_win(opponent[move[0]], player_moves[move[1]])
        print(result)
        points = scoring[result]
        player_value = move_values[player_moves[move[1]]]
        player_total = player_total + player_value + points
    print(player_total)


def main():
    play_game()


if __name__ == "__main__":
    main()
