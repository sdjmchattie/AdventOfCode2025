from dataclasses import dataclass


@dataclass
class InputData:
    fresh_stock: list[tuple[int, int]]
    stock: list[int]


def prepare_input(file_content: list[str]) -> InputData:
    split = file_content.index("")
    fresh, all = file_content[:split], file_content[split + 1 :]

    fresh_stock = [
        tuple(int(val_str) for val_str in range_str.split("-")) for range_str in fresh
    ]
    stock = [int(line) for line in all]

    return InputData(fresh_stock=fresh_stock, stock=stock)


def part1(input: InputData) -> None:
    def item_is_fresh(item: int, fresh_stock: list[tuple[int, int]]) -> bool:
        return any(fresh[0] <= item <= fresh[1] for fresh in fresh_stock)

    print(sum(1 for item in input.stock if item_is_fresh(item, input.fresh_stock)))


def part2(input: InputData) -> None:
    merged_ranges = []
    for fresh in input.fresh_stock:
        start, end = fresh

        # Find any lower end range that this new range extends.
        # Also find any upper end range that this new range extends.
        # There could be one at both ends!
        # We also need to find any ranges that are within the new one because
        # the new one will replace it entirely.
        # All discovered ranges can be removed from merged_ranges.
        lower = next((r for r in merged_ranges if r[0] <= start <= r[1]), None)
        upper = next((r for r in merged_ranges if r[0] <= end <= r[1]), None)
        within = list(
            r for r in merged_ranges if start <= r[0] <= end and start <= r[1] <= end
        )
        merged_ranges = [r for r in merged_ranges if r not in [lower, upper] + within]

        # Adjust our new range to include lower and upper ranges, then append to merged_ranges
        start = lower[0] if lower else start
        end = upper[1] if upper else end
        merged_ranges.append((start, end))

    print(sum(r[1] - r[0] + 1 for r in merged_ranges))
