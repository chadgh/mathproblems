#!/usr/bin/env python
import operator
from random import choice

OPERATOR_SLUGS = {
    '+': 'add',
    '-': 'sub',
    'x': 'mul',
    # '/': 'add',
}


def solve_problem(numbers, op):
    numbers = list(numbers)
    rtn = numbers.pop(0)
    do = getattr(operator, OPERATOR_SLUGS[op])
    for n in numbers:
        rtn = do(rtn, n)
    return rtn


def _gen_problems(numbers, operators,
                  num_problems=10,
                  problem_size=2,
                  bottom_numbers=None):
    problem_sets = _gen_problem_number_tuples(numbers,
                                              num_problems,
                                              bottom_numbers,
                                              problem_size)
    for nums in problem_sets:
        yield tuple([nums, choice(operators)])


def _gen_numbers(number_sizes=1):
    return [n for n in range(10**number_sizes)]


def _gen_problem_number_tuples(numbers,
                               num_problems=10,
                               bottom_numbers=None,
                               problem_size=2):
    problem_size = problem_size if problem_size > 2 else 2
    problem_sets = []

    for _ in range(num_problems):
        if bottom_numbers:
            problem_sets.append(tuple(sorted([choice(numbers),
                                              choice(bottom_numbers)],
                                             reverse=True)))
        else:
            problem_sets.append(tuple(sorted([choice(numbers)
                                              for _ in range(problem_size)],
                                             reverse=True)))
    return problem_sets


def _gen_problem_string(numbers, op):
    str_problem = ''
    for _ in range(len(numbers) - 1):
        str_problem += '{:>5}\n'
    str_problem += op + '{:>4}\n=====\n\n'
    return str_problem


def print_problems(problems):
    for problem in problems:
        numbers, op = problem
        str_problem = _gen_problem_string(numbers, op)
        print(str_problem.format(*numbers))


def gen_random_problems(number_sizes=1, operators=['+'], **kwargs):
    return _gen_problems(_gen_numbers(number_sizes), operators, **kwargs)


def gen_specific_problems(number_sizes=1, operators=['x'],
                          bottom_numbers=[1, 2, 3, 4, 5, 10], **kwargs):
    return _gen_problems(_gen_numbers(number_sizes), operators,
                         bottom_numbers=bottom_numbers, **kwargs)


def solve_problems(problems):
    grade = 0
    total_problems = 0
    for prob in problems:
        total_problems += 1
        numbers, op = prob
        print(_gen_problem_string(numbers, op).format(*numbers))
        solution = solve_problem(numbers, op)
        submitted_solution = int(input())
        if submitted_solution == solution:
            print('Right!')
            grade += 1
        else:
            print('Wrong :(')
            print('The answer was: {}'.format(submitted_solution))
    print('You got {}%'.format((grade / total_problems) * 100))


if __name__ == '__main__':
    # print(list(gen_random_problems()))
    solve_problems(gen_random_problems(num_problems=5))
