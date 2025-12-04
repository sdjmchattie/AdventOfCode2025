from lib.grid2d import Grid2D
from lib.types import PuzzleInput


def prepare_input(file_content: list[str]) -> PuzzleInput:
    chars = [list(line.strip()) for line in file_content]

    return Grid2D.from_data(chars)


def _is_movable_roll(grid: Grid2D[str], x: int, y: int) -> None:
    current = grid[x, y]
    adjacent = grid.adjacent_values(x, y)

    return current == "@" and sum(1 for v in adjacent if v == "@") < 4


def part1(input: PuzzleInput) -> None:
    print(
        sum(
            1
            for x in range(input.width)
            for y in range(input.height)
            if _is_movable_roll(input, x, y)
        )
    )


def _removable_rolls(grid: Grid2D[str], removed: int = 0) -> int:
    before = removed

    for x in range(grid.width):
        for y in range(grid.height):
            if _is_movable_roll(grid, x, y):
                grid[x, y] = "."
                removed += 1

    return removed if removed == before else _removable_rolls(grid, removed)


def part2(input: PuzzleInput) -> None:
    print(_removable_rolls(input))
