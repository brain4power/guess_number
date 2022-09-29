import random

from typing import Callable


def number_guesser(hidden_number: int) -> int:
    """
    guess the number via binary search algorithm
    :param hidden_number: hidden number
    :return: number of attempts
    """
    low = 1
    high = 100
    attempts_number = 1
    guess = (low + high) // 2
    while guess != hidden_number:
        guess = (low + high) // 2
        if guess > hidden_number:
            high = guess
        elif guess < hidden_number:
            low = guess + 1
        attempts_number += 1
    return attempts_number


def guesser_checker(guess_algorithm_func: Callable[[int], float]) -> float:
    """
    Calculate mean of number of attempts of number guess algorithm
    :param guess_algorithm_func: guess algorithm function
    :return: Average of number of attempts
    """
    total_checks = 1000
    accumulated_attempts_value = 0
    for _ in range(total_checks):
        number = random.randint(1, 100)
        attempts_number = guess_algorithm_func(number)
        accumulated_attempts_value += attempts_number
    return accumulated_attempts_value / total_checks


if __name__ == '__main__':
    result = guesser_checker(number_guesser)
    print(f'Average of a 1000 attempts number_guesser: {result:.2f}')
