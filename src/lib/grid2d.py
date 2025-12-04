from typing import Generic, Optional, TypeVar

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

    def adjacent_values(self, x: int, y: int) -> list[T]:
        deltas = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        values = []
        for dx, dy in deltas:
            nx, ny = x + dx, y + dy
            try:
                values.append(self[nx, ny])
            except IndexError:
                continue

        return values

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.grid])
