from typing import Generic, Optional, TypeVar

from lib.direction import Direction, ALL_DIRS

T = TypeVar("T")


class Grid2D(Generic[T]):
    def __init__(self, width: int, height: int, default: Optional[T] = None):
        self.width = width
        self.height = height
        self.grid: list[list[T]] = [
            [default for _ in range(width)] for _ in range(height)
        ]

    @classmethod
    def from_data(cls, data: list[list[T]]) -> "Grid2D[T]":
        height = len(data)
        width = len(data[0]) if height > 0 else 0

        if any(len(row) != width for row in data):
            raise ValueError("All rows must have the same length")

        grid = cls(width, height)
        for y in range(height):
            for x in range(width):
                grid[x, y] = data[y][x]

        return grid

    def _check_range(self, x: int, y: int) -> None:
        if not 0 <= x < self.width or not 0 <= y < self.height:
            raise IndexError("Grid index out of range")

    def __getitem__(self, key: tuple[int, int]) -> T:
        x, y = key
        self._check_range(x, y)
        return self.grid[y][x]

    def __setitem__(self, key: tuple[int, int], value: T) -> None:
        x, y = key
        self._check_range(x, y)
        self.grid[y][x] = value

    def adjacent_value(self, x: int, y: int, direction: Direction) -> Optional[T]:
        nx, ny = direction.move(x, y)
        try:
            return self[nx, ny]
        except IndexError:
            return None

    def adjacent_values(
        self, x: int, y: int, dirs: list[Direction] = ALL_DIRS
    ) -> list[T]:
        values = []
        for direction in dirs:
            values.append(self.adjacent_value(x, y, direction))

        return [v for v in values if v is not None]

    def find(self, target: T) -> Optional[tuple[int, int]]:
        for y in range(self.height):
            for x in range(self.width):
                if self[x, y] == target:
                    return (x, y)
        return None

    def __str__(self):
        return "\n".join(["".join(map(str, row)) for row in self.grid])
