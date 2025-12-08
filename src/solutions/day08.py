from dataclasses import dataclass
from functools import reduce
from itertools import combinations
from lib.point3d import Point3D
from lib.types import PuzzleInput


@dataclass
class JunctionPair:
    a: Point3D[int]
    b: Point3D[int]
    distance: float


type Circuits = list[set[Point3D[int]]]
type Pairs = list[JunctionPair]


def prepare_input(file_content: list[str]) -> PuzzleInput:
    return [
        Point3D(x, y, z)
        for x, y, z in (map(int, line.split(",")) for line in file_content)
    ]


def _parse_circuits_and_pairs(
    input: PuzzleInput,
) -> tuple[Circuits, Pairs]:
    circuits = [{junc} for junc in input]
    pairs = [
        JunctionPair(c[0], c[1], c[0].distance_to(c[1])) for c in combinations(input, 2)
    ]
    pairs.sort(key=lambda jp: jp.distance)

    return circuits, pairs


def _join_junctions(pair: JunctionPair, circuits: Circuits) -> Circuits:
    to_merge = list(c for c in circuits if pair.a in c or pair.b in c)
    merged_circuit = set().union(*to_merge)

    circuits = [c for c in circuits if c not in to_merge]
    circuits.append(merged_circuit)

    return circuits


def part1(input: PuzzleInput) -> None:
    circuits, pairs = _parse_circuits_and_pairs(input)

    for pair in pairs[:1000]:
        circuits = _join_junctions(pair, circuits)

    circuit_sizes = sorted([len(c) for c in circuits], reverse=True)

    print(reduce(lambda a, x: a * x, circuit_sizes[:3], 1))


def part2(input: PuzzleInput) -> None:
    circuits, pairs = _parse_circuits_and_pairs(input)

    for pair in pairs:
        circuits = _join_junctions(pair, circuits)

        if len(circuits) == 1:
            print(pair.a.x * pair.b.x)
            return
