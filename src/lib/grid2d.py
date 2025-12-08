from lib.direction import Direction, ALL_DIRS
from lib.point2d import Point2D


class Grid2D[T]:
    def __init__(self, width: int, height: int, default: T | None = None):
        self._unbounded = False
        self.width = width
        self.height = height
        self.default = default
        self.grid = dict[Point2D[int], T]()

    @property
    def unbounded(self) -> bool:
        return self._unbounded

    @unbounded.setter
    def unbounded(self, value: bool) -> None:
        self._unbounded = value

    def __getitem__(self, key: tuple[int, int]) -> T:
        x, y = key
        point = Point2D(x, y)
        self._check_range(point)

        return self.grid.get(point, self.default)

    def __setitem__(self, key: tuple[int, int], value: T) -> None:
        x, y = key
        point = Point2D(x, y)
        self._check_range(point)
        self.grid[point] = value

    def __repr__(self):
        return f"Grid2D(width={self.width}, height={self.height}, unbounded={self.unbounded}, default={self.default})"

    def __str__(self):
        if self.unbounded:
            return self.__repr__()

        return "\n".join(
            [
                "".join(
                    str(self.grid.get(Point2D(x, y), self.default))
                    for x in range(self.width)
                )
                for y in range(self.height)
            ]
        )

    def _check_range(self, point: Point2D[int]) -> None:
        if self.unbounded:
            return

        if not 0 <= point.x < self.width or not 0 <= point.y < self.height:
            raise IndexError("Grid index out of range")

    @classmethod
    def from_data(cls, data: list[list[T]], unbounded: bool = False) -> "Grid2D[T]":
        if unbounded:
            grid = cls(0, 0)
        else:
            height = len(data)
            width = len(data[0]) if height > 0 else 0

            if any(len(row) != width for row in data):
                raise ValueError("All rows must have the same length")

            grid = cls(width, height)

        grid.unbounded = unbounded

        for y in range(height):
            for x in range(width):
                grid[x, y] = data[y][x]

        return grid

    def adjacent_value(self, x: int, y: int, direction: Direction) -> T | None:
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

    def find(self, target: T) -> tuple[int, int] | None:
        for k, v in self.grid.items():
            if v == target:
                return k.x, k.y

        return None
