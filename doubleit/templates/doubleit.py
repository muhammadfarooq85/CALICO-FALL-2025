def solve(N: int, P: str) -> int:
    """
    Return the total money Big Ben pays
    
    N: length of the string P
    P: string of characters representing the people Big Ben talks to
    """
    # YOUR CODE HERE
    
    spent = 0
    wallet = 1

    for person in P:
        if person == "T":
            spent += wallet
            wallet = 1
        elif person == "D":
            wallet *= 2
    return spent

def main():
    T = int(input())
    for _ in range(T):
        N = input()
        P = input()
        print(solve(N, P))

if __name__ == '__main__':
    main()
