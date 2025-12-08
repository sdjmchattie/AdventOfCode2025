from dataclasses import dataclass


@dataclass(frozen=True)
class Point3D[IntFloat: (int, float)]:
    x: IntFloat
    y: IntFloat
    z: IntFloat

    def distance_to(self, other: "Point3D") -> float:
        return (
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        ) ** 0.5
