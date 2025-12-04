from lib.types import PuzzleInput


def prepare_input(file_content: list[str]) -> PuzzleInput:
    return file_content


def part1(input: PuzzleInput) -> None:
    zeroes = 0
    dial = 50
    for line in input:
        value = int(line[1:])

        if line[0] == "L":
            dial -= value
        else:
            dial += value

        zeroes += 1 if dial % 100 == 0 else 0

    print(zeroes)


def part2(input: PuzzleInput) -> None:
    zeroes = 0
    dial = 50
    for line in input:
        value = int(line[1:])
        prev = dial

        if line[0] == "L":
            dial -= value
            zeroes += ((prev - 1) // 100) - ((dial - 1) // 100)
        else:
            dial += value
            zeroes += (dial // 100) - (prev // 100)

    print(zeroes)
