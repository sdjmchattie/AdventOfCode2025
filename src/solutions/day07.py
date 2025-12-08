from lib.types import PuzzleInput
from lib.grid2d import Grid2D


def prepare_input(file_content: list[str]) -> PuzzleInput:
    original = Grid2D[str].from_data(file_content)
    parsed = Grid2D(original.width, original.height, 0)

    parsed[original.find("S")] = 1

    # Transfer original data into tachyon counts
    for y in range(original.height - 1):
        y_next = y + 1
        for x in range(original.width):
            x_left = x - 1
            x_right = x + 1
            current_count = parsed[x, y]
            if current_count > 0:
                if original[x, y_next] == "^":
                    parsed[x_left, y_next] += current_count
                    parsed[x_right, y_next] += current_count
                else:
                    parsed[x, y_next] += current_count

    return parsed


def part1(input: PuzzleInput) -> None:
    # Count active splitters
    count = 0
    for y in range(1, input.height):
        y_prev = y - 1
        for x in range(input.width):
            if input[x, y] == 0:
                adjacent = input[x, y_prev]
                if adjacent > 0:
                    count += 1

    print(count)


def part2(input: PuzzleInput) -> None:
    # Sum tachyon counts in the bottom row
    print(sum(input[x, input.height - 1] for x in range(input.width)))
