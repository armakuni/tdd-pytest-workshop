from dataclasses import asdict, dataclass


@dataclass
class CuteAnimal:
    name: str
    age: int
    cuteness_level: int

    def to_dict(self):
        return asdict(self)
