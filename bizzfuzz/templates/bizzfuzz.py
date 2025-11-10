def solve(W1: str, W2: str) -> str:
    """
    Return the string containing the word you should say
 
    W1: the second-to-last word said 
    W2: the last word said
    """
    # YOUR CODE HERE

    if W2.isdigit():
        current = int(W2)
    elif W1.isdigit():
        current = int(W1) + 1 # 39
    else:
         return "crap"
    
    next_num = current + 1
    if next_num % 15 == 0:
            return "bizzfuzz"
    elif next_num % 3 == 0:
            return "bizz"
    elif next_num % 5 == 0:
            return "fuzz"
    else:
        return str(next_num)


def main():
    T = int(input())

    for _ in range(T):
        W1 = input()
        W2 = input()
        print(solve(W1, W2))

if __name__ == '__main__':
    main()