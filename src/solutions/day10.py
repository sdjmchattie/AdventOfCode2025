from functools import reduce
from lib.types import PuzzleInput
from z3 import Int, Optimize, Sum


class Machine:
    def __init__(
        self, lights: str, buttons: list[list[int]], joltages: list[int]
    ) -> None:
        self._lights_binary = lights.replace(".", "0").replace("#", "1")
        self.button_bin_digits = [
            self._button_binary(button, len(lights)) for button in buttons
        ]
        self.button_ints = [
            int("".join(map(str, bits)), 2) for bits in self.button_bin_digits
        ]
        self.joltages = joltages

    @property
    def lights_int(self) -> str:
        return int(self._lights_binary, 2)

    def _button_binary(self, effect: list[int], lights_count: int) -> list[int]:
        return [1 if i in effect else 0 for i in range(lights_count)]


def prepare_input(file_content: list[str]) -> PuzzleInput:
    machines = []
    for line in file_content:
        parts = line.split(" ")
        lights = parts[0][1:-1]
        buttons = [list(map(int, part[1:-1].split(","))) for part in parts[1:-1]]
        joltages = tuple(map(int, parts[-1][1:-1].split(",")))

        machines.append(Machine(lights, buttons, joltages))

    return machines


def part1(input: PuzzleInput) -> None:
    best_per_machine = []

    for machine in input:
        machine_combos = []
        button_count = len(machine.button_ints)
        for combo in range(2**button_count):
            buttons = [
                machine.button_ints[i] for i in range(button_count) if (combo >> i) & 1
            ]
            combined_effect = reduce(lambda acc, b: acc ^ b, buttons, 0)
            if combined_effect == machine.lights_int:
                machine_combos.append(bin(combo).count("1"))

        best_per_machine.append(min(machine_combos))

    print(sum(best_per_machine))


def _solve_machine(buttons: list[list[int]], joltages: list[int]) -> int:
    presses = [Int(f"p_{i}") for i in range(len(buttons))]
    eqs = [
        Sum([presses[j] * buttons[j][i] for j in range(len(buttons))]) == joltages[i]
        for i in range(len(joltages))
    ]

    opt = Optimize()
    for p in presses:
        opt.add(p >= 0)

    opt.add(*eqs)

    total = Sum(presses)
    opt.minimize(total)
    opt.check()
    model = opt.model()
    return model.evaluate(total).as_long()


def part2(input: PuzzleInput) -> None:
    results = [
        _solve_machine(machine.button_bin_digits, machine.joltages) for machine in input
    ]

    print(sum(results))
