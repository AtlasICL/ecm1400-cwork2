import random
import json

import components, game_engine

players = {}

def get_board_size(board) -> int:
    board_size: int = len(board)
    assert board_size > 0, "BOARD LEN 0"
    return board_size

def display_mp_welcome() -> None:
    print("Welcome to battleships game")

def generate_attack(board) -> tuple:
    board_size: int = get_board_size(board)
    attack_x: int = random.randint(0, board_size-1)
    attack_y: int = random.randint(0, board_size-1)
    return (attack_x, attack_y)


def initialise_players_dict(placements_filepath: str ="placement.json") -> dict[str, dict]:
    user_board = components.make_custom_board(placements_filepath)
    player_ships = components.get_player_ships(placements_filepath)

    ai_opponent_board = components.make_random_board()

    players = {
        "user": {
            "board": user_board,
            "ships": player_ships
        },
        "ai": {
            "board": ai_opponent_board,
            "ships": player_ships
        }
    }
    return players

def ai_opponent_game_loop():

    global players
    players = initialise_players_dict()

    display_mp_welcome()

    all_user_ships_sunk = False
    all_ai_ships_sunk = False

    while not all_user_ships_sunk and not all_ai_ships_sunk:

        (x, y) = game_engine.cli_coordinates_input()
        game_engine.attack((x, y), players["ai"]["board"], players["ai"]["ships"])

        (x, y) = generate_attack(players["user"]["board"])
        game_engine.attack((x, y), players["user"]["board"], players["user"]["ships"])

        components.print_board(players["user"]["board"])
        components.print_board(players["ai"]["board"])

        all_user_ships_sunk = game_engine.is_all_ships_sunk(players["user"]["ships"])
        all_ai_ships_sunk = game_engine.is_all_ships_sunk(players["ai"]["ships"])
    
    
    





def main():
    ai_opponent_game_loop()

if __name__ == "__main__":
    main()