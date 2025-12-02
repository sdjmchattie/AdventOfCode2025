from .types import PuzzleInput


def prepare_input(file_content: list[str]) -> PuzzleInput:
    ranges = file_content[0].split(",")
    numbers = [[int(x) for x in r.split("-")] for r in ranges]
    return numbers


def part1(input: PuzzleInput) -> None:
    bad = []
    for start, end in input:
        for x in range(start, end + 1):
            str_x = str(x)
            half_length = len(str_x) // 2

            first_half = str_x[:half_length]
            second_half = str_x[half_length:]

            if first_half == second_half:
                bad.append(x)

    print(sum(bad))


def part2(input: PuzzleInput) -> None:
    bad = []
    for start, end in input:
        for x in range(start, end + 1):
            str_x = str(x)
            half_length = len(str_x) // 2
            for chunk_size in range(1, half_length + 1):
                if len(str_x) % chunk_size != 0:
                    continue

                chunks = [
                    str_x[i : i + chunk_size]
                    for i in range(0, len(str_x), chunk_size)
                ]
                if all(chunk == chunks[0] for chunk in chunks):
                    bad.append(x)
                    break

    print(sum(bad))
