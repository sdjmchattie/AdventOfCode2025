from dataclasses import dataclass
from enum import Enum
from itertools import combinations
from lib.types import PuzzleInput

type Point = tuple[int, int]


def prepare_input(file_content: list[str]) -> PuzzleInput:
    return tuple(tuple(map(int, line.split(","))) for line in file_content)


def _calculate_area(a: Point, b: Point) -> int:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def part1(input: PuzzleInput) -> None:
    areas = (_calculate_area(a, b) for a, b in combinations(input, 2))
    print(max(areas))


def part2(input: PuzzleInput) -> None:
    Part2(input).solve()


class Axis(Enum):
    VERTICAL = 0
    HORIZONTAL = 1


@dataclass(frozen=True)
class Edge:
    aligned: int
    perp_min: int
    perp_max: int


class Part2:
    def __init__(self, points: PuzzleInput) -> None:
        self.points = points
        self.vert_edges = self._find_edges(Axis.VERTICAL)
        self.horz_edges = self._find_edges(Axis.HORIZONTAL)

    def _find_edges(self, axis: Axis) -> set[Edge]:
        """Find the vertical or horizontal edges between points in a set."""
        aligned = axis.value
        perp = 1 - aligned
        return set(
            Edge(
                a[aligned],
                min(a[perp], b[perp]),
                max(a[perp], b[perp]),
            )
            for a, b in combinations(self.points, 2)
            if a[aligned] == b[aligned]
        )

    def _area_contains_no_edges(self, a: Point, b: Point) -> bool:
        """Check if the rectangular area defined by points a and b contains no edges."""
        x_min, x_max = min(a[0], b[0]), max(a[0], b[0])
        y_min, y_max = min(a[1], b[1]), max(a[1], b[1])

        for edge in self.vert_edges:
            if (
                x_min < edge.aligned < x_max
                and edge.perp_max > y_min
                and edge.perp_min < y_max
            ):
                return False

        for edge in self.horz_edges:
            if (
                y_min < edge.aligned < y_max
                and edge.perp_max > x_min
                and edge.perp_min < x_max
            ):
                return False

        return True

    def solve(self) -> None:
        areas = [
            _calculate_area(a, b)
            for a, b in combinations(self.points, 2)
            if self._area_contains_no_edges(a, b)
        ]
        print(max(areas))
