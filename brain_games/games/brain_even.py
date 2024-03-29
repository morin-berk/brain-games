from random import randrange
from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import check_player_answer
from brain_games.consts import EVEN_RULES, MIN_RANGE_LENGTH, MAX_RANGE_LENGTH


def play_even_num():
    """
    The game asks a player if a number is even or odd.
    If a player answers correctly 3 times, they win.
    """
    name = welcome_user()

    print(EVEN_RULES)

    rounds = 0

    while -1 < rounds < 3:
        random_number = randrange(MIN_RANGE_LENGTH, MAX_RANGE_LENGTH)

        question_expression = f'{str(random_number)}'

        correct_answer = "yes" if random_number % 2 == 0 else "no"

        rounds = check_player_answer(correct_answer,
                                     name,
                                     question_expression,
                                     rounds)

        if rounds == 3:
            print(f"Congratulations, {name}!")
