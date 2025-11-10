def solve(N: int, M: int, G: list[str]) -> int:
    destroyed_columns = 0
    for col in range(M):
        for row in range(N):
            if G[row][col] != '.':
                destroyed_columns += 1
                break
    return destroyed_columns

def main():
    T = int(input().strip())
    for _ in range(T):
        N, M = map(int, input().split())
        G = [input().strip() for _ in range(N)]
        print(solve(N, M, G))

if __name__ == '__main__':
    main()
