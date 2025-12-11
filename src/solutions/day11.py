from functools import cache
from lib.types import PuzzleInput


class PathFinder:
    def __init__(self, map: PuzzleInput) -> None:
        self._map = map

    @cache
    def find_path_count(
        self, src: str, specials: tuple[str] = (), seen_specials: tuple[str] = ()
    ) -> int:
        if src == "out":
            return 1 if all(s in seen_specials for s in specials) else 0
        else:
            paths = 0

            for dest in self._map[src]:
                new_seen = (
                    seen_specials + (dest,) if dest in specials else seen_specials
                )
                paths += self.find_path_count(dest, specials, new_seen)

            return paths


def prepare_input(file_content: list[str]) -> PuzzleInput:
    map = {
        src: dests
        for line in file_content
        for src, *dests in [line.replace(":", "").split(" ")]
    }

    return PathFinder(map)


def part1(input: PuzzleInput) -> None:
    print(input.find_path_count("you"))


def part2(input: PuzzleInput) -> None:
    print(input.find_path_count("svr", specials=("dac", "fft")))
