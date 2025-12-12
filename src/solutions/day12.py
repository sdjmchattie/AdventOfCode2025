from lib.types import PuzzleInput


def prepare_input(file_content: list[str]) -> PuzzleInput:
    shapes = []
    grids = []
    next_shape = []
    for line in file_content:
        if line == "" or line.endswith(":"):
            if next_shape:
                shapes.append(next_shape)
            next_shape = []
            continue

        if "x" in line:
            parts = [p.strip() for p in line.split(":")]
            dims = [int(x) for x in parts[0].split("x")]
            shape_counts = [int(x) for x in parts[1].split(" ")]
            grids.append((dims, shape_counts))
        else:
            next_shape.append(line)

    return shapes, grids


def part1(input: PuzzleInput) -> None:
    hash_sizes = []
    for grid in input[0]:
        size = 0
        for line in grid:
            size += line.count("#")
        hash_sizes.append(size)

    fits = 0
    for dims, shape_counts in input[1]:
        grid_size = dims[0] * dims[1]
        full_size_shapes = sum([c * hash_sizes[i] for i, c in enumerate(shape_counts)])

        fits += 1 if full_size_shapes < grid_size else 0

    print(fits)


def part2(input: PuzzleInput) -> None:
    pass
