from typing import List

class Person():

    def __init__(self, name : str, age: int, skills : List[str]) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.skills = skills

    def __str__(self) -> str:
        return f'{self.name} ({self.age}): {self.skills}'
