from src.utils import generate_interval, format_big, save_numbers_to_file

def main():
    FACT_N = 74

    print(f"Generating an interval using {FACT_N}! ...\n")
    numbers = generate_interval(FACT_N)

    
    print("Interval start:")
    print(format_big(numbers[0]))
    print("\nInterval end:")
    print(format_big(numbers[-1]))
    print(f"\nTotal numbers: {len(numbers)}\n")

    print("All numbers (each on its own line):\n")
    for line_num, num in enumerate(numbers, start=2):
        print(f"{line_num:>2}) {format_big(num)}")

    out_filename = "interval_73_list.txt"
    save_numbers_to_file(numbers, out_filename, sep=",")
    print(f"\nSaved all numbers to: {out_filename}")


if __name__ == "__main__":
    main()
