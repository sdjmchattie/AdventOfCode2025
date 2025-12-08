from dataclasses import dataclass
from typing import Generic, TypeVar

IntFloat = TypeVar("IntFloat", int, float)


@dataclass(frozen=True)
class Point3D(Generic[IntFloat]):
    x: IntFloat
    y: IntFloat
    z: IntFloat

    def distance_to(self, other: "Point3D") -> float:
        return (
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        ) ** 0.5
