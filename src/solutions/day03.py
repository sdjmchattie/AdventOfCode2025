from lib.types import PuzzleInput


def prepare_input(file_content: list[str]) -> PuzzleInput:
    return [[int(char) for char in line] for line in file_content]


def _max_joltage(starting_bank: list[int], size: int) -> int:
    bank = starting_bank.copy()
    joltage = 0

    while size > 0:
        size -= 1
        digit = max(bank[: len(bank) - size])
        joltage += digit * (10**size)
        loc = bank.index(digit)
        bank = bank[loc + 1 :]

    return joltage


def part1(input: PuzzleInput) -> None:
    print(sum(_max_joltage(bank, 2) for bank in input))


def part2(input: PuzzleInput) -> None:
    print(sum(_max_joltage(bank, 12) for bank in input))
