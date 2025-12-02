import math


def format_big(n: int) -> str:
    """Format large integers with thousands separators."""
    return f"{n:,}"


def main():
    N = math.factorial(74)

    print("74! =")
    print(format_big(N))
    print("\nGenerated interval of 73 consecutive composite numbers:\n")

    numbers = []

    for k in range(2, 75):      
        composite_num = N + k
        numbers.append(composite_num)
        print(f"{k:>2})  {format_big(composite_num)}")

    print("\nSummary:")
    print("Start:", format_big(numbers[0]))
    print("End:  ", format_big(numbers[-1]))
    print(f"Total numbers printed: {len(numbers)} (all composite)")



if __name__ == "__main__":
    main()
