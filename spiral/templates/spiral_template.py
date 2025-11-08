name = "spiral"

def draw_spiral(n):
    size = 4 * n - 1
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    
    for k in range(n):
        start = 2 * k
        end = size - 1 - 2 * k

        # Top edge
        for j in range(start, end + 1):
            grid[start][j] = '@'
        
        # Right edge
        for i in range(start, end + 1):
            grid[i][end] = '@'
        
        # Bottom edge
        for j in range(end, start - 1, -1):
            grid[end][j] = '@'
        
        # Left edge
        for i in range(end, start - 1, -1):
            grid[i][start] = '@'
    
    for row in grid:
        print(''.join(row))


def main():
    T = int(input().strip())
    for t in range(T):
        n = int(input().strip())
        draw_spiral(n)
        if t < T - 1:
            print()  # Blank line between test cases


if __name__ == "__main__":
    main()
