name = "dna"

def read():
    case = input().strip()
    return case

def logic(case):
    # dna: the string of DNA bases, consisting of letters A, T, C, and G
    dna = case
    
    # TODO: YOUR CODE HERE
    result = ""
    for base in dna:
        if base == "A":
            result += "T"
        elif base == "T":
            result += "A"
        elif base == "C":
            result += "G"
        elif base == "G":
            result += "C"
    return result

def main():
    T = int(input().strip())
    for _ in range(T):
        result = logic(read())
        print(result)

if __name__ == "__main__":
    main()