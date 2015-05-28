#!/usr/bin/env python
# import operator
from random import choice


def problems(num_problems=10, number_sizes=1, problem_size=2):
    """
    Returns a sequence of num_problems problems.

    Arguments:
        num_problems=10 - The number of problems to generate.
        number_sizes=1 - The size of the numbers to use. One, two, etc digits.
        problem_size=2 - The number of numbers to use in the problems.
    """
    problem_size = problem_size if problem_size > 2 else 2
    number_sizes = number_sizes if number_sizes > 1 else 1
    problem_size = problem_size if problem_size > 1 else 1

    numbers = [n for n in range(10**number_sizes)]

    for _ in range(num_problems):
        yield tuple(sorted([choice(numbers) for _ in range(problem_size)],
                           reverse=True))


def _gen_problem_string(problem_size, operation_symbol='+'):
    str_problem = ''
    for _ in range(problem_size - 1):
        str_problem += '{:>5}\n'
    str_problem += operation_symbol + '{:>4}\n=====\n\n'
    return str_problem


def print_problems(operation_symbol='+', problem_size=2, **kwargs):
    str_problem = _gen_problem_string(problem_size, operation_symbol)
    for problem in problems(problem_size=problem_size, **kwargs):
        print(str_problem.format(*problem))


def addition_problems(**kwargs):
    print_problems('+', **kwargs)


def subtraction_problems(**kwargs):
    print_problems('-', **kwargs)


def multiplication_problems(problem_size=2, **kwargs):
    print_problems('x', **kwargs)


if __name__ == '__main__':
    # addition_problems(num_problems=2, number_sizes=3)
    multiplication_problems(number_sizes=2)
