from dataclasses import dataclass
from functools import reduce
import operator
import re

from lib.types import PuzzleInput


OPERATORS = {
    "+": operator.add,
    "*": operator.mul,
}


@dataclass
class MathsProblem:
    values: tuple[int]
    operator: callable


def prepare_input(file_content: list[str]) -> PuzzleInput:
    return file_content


def _solve(maths_problems: list[MathsProblem]):
    results = []
    for problem in maths_problems:
        results.append(
            reduce(
                lambda a, x: problem.operator(a, x),
                problem.values[1:],
                problem.values[0],
            )
        )

    return sum(results)


def part1(input: PuzzleInput) -> None:
    values = [re.findall(r"\S+", line) for line in input]
    transposed = list(zip(*values))
    maths_problems = [
        MathsProblem(
            values=tuple(int(x) for x in prob[:-1]), operator=OPERATORS[prob[-1]]
        )
        for prob in transposed
    ]

    print(_solve(maths_problems))


def part2(input: PuzzleInput) -> None:
    transpose = list(zip(*input)) + [(" ")]
    maths_problems = []
    operator = None
    values = []
    for line in transpose:
        val_str = "".join(line[:-1]).strip()

        if len(val_str) == 0:
            maths_problems.append(MathsProblem(values=tuple(values), operator=operator))
            values = []
            continue

        if line[-1] != " ":
            operator = OPERATORS[line[-1]]

        values.append(int(val_str))

    print(_solve(maths_problems))
