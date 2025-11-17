import importlib
from pathlib import Path
import sys
import time


def run_solve(day: int) -> None:
    day_str = f"day{int(day):02d}"
    input_file = Path("inputs") / f"{day_str}.txt"

    module_name = f"solutions.{day_str}"
    day_module = importlib.import_module(module_name)
    prepare_input = getattr(day_module, "prepare_input")
    part1 = getattr(day_module, "part1")
    part2 = getattr(day_module, "part2")

    print(f"Performing solve for Day {day}...")

    print()
    print("Starting Part 1...")
    with input_file.open("r") as f:
        p1_data = prepare_input([line.strip("\n") for line in f.readlines()])
    p1_start = time.perf_counter()
    part1(p1_data)
    p1_time_ms = (time.perf_counter() - p1_start) * 1000
    print(f"Part 1 completed in {p1_time_ms:.3f} ms")

    print()
    print("Starting Part 2...")
    with input_file.open("r") as f:
        p2_data = prepare_input([line.strip("\n") for line in f.readlines()])
    p2_start = time.perf_counter()
    part2(p2_data)
    p2_time_ms = (time.perf_counter() - p2_start) * 1000
    print(f"Part 2 completed in {p2_time_ms:.3f} ms")


def solve():
    if len(sys.argv) < 2:
        print("Usage:  uv run solve [day]")
        sys.exit(1)

    run_solve(sys.argv[1])


if __name__ == "__main__":
    solve()
