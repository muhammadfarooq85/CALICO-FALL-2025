def solve(E: str, Y: int, M: int, D: int) -> str:
    """

    E: The name of the event
    Y: Year
    M: Month
    D: Day
    """
    gta6 = (2026, 11, 19)
    date = (Y, M, D)

    if date < gta6:
        return "we got " + E + " before gta6"
    else:
        return "we got gta6 before " + E
    

def main():
    T = int(input())
    for _ in range(T):
        E = input()
        temp = input().split()
        Y, M, D = int(temp[0]), int(temp[1]), int(temp[2])
        print(solve(E, Y, M, D))

if __name__ == '__main__':
    main()
