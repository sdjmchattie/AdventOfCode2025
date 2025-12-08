from dataclasses import dataclass


@dataclass(frozen=True)
class Point2D[IntFloat: (int, float)]:
    x: IntFloat
    y: IntFloat
