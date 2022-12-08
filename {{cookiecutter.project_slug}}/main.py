def part_one(data: list[str]):
    pass


def part_two(data: list[str]):
    pass

def read_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return list(map(lambda x: x.strip(), f.readlines()))

def main():
    data = read_data("input_test.txt")
    print(f'Part one: {part_one(data)}')
    print(f'Part two: {part_two(data)}')


if __name__ == "__main__":
    main()