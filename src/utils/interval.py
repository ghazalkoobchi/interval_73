import math
from typing import List


def format_big(n: int, sep: str = ",") -> str:
    s = f"{n:,}"
    if sep != ",":
        s = s.replace(",", sep)
    return s


def factorial_n(n: int) -> int:
    
    return math.factorial(n)


def generate_interval(n_factorial: int = 74) -> List[int]:
  
    N = factorial_n(n_factorial)
    return [N + k for k in range(2, n_factorial + 1)]


def save_numbers_to_file(numbers: List[int], filename: str, sep: str = ",") -> None:

    with open(filename, "w", encoding="utf-8") as f:
        for i, num in enumerate(numbers, start=2):
            f.write(f"{i}) {format_big(num, sep=sep)}\n")
