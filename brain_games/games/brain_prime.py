from random import randrange
from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import check_player_answer
from brain_games.consts import PRIME_RULES, MIN_RANGE_LENGTH, MAX_RANGE_LENGTH


def play_prime():
    """
    The game asks a player whether a number is prime or not.
    If a player answers correctly 3 times, they win.
    """
    name = welcome_user()

    print(PRIME_RULES)

    rounds = 0

    while -1 < rounds < 3:

        random_num = randrange(MIN_RANGE_LENGTH, MAX_RANGE_LENGTH)

        correct_answer = "no" if random_num == 1 else "yes"

        for el in range(2, random_num):
            if random_num % el == 0 and el != random_num:
                correct_answer = "no"
                break
            else:
                correct_answer = "yes"

        question_expression = str(random_num)

        rounds = check_player_answer(correct_answer,
                                     name,
                                     question_expression,
                                     rounds
                                     )

        if rounds == 3:
            print(f"Congratulations, {name}!")
