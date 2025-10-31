name = "dna"

# You don't need to do anything here; I've already written it for you! You're welcome
def read():
    # Read in the input, remove any leading/trailing whitespace
    case = input().strip()
    
    return case

def logic(case):
    # dna: the string of DNA bases, consisting of letters A, T, C, and G
    dna = case
    # It's your turn to code! Use the variable(s) above to find your answer
    
    # TODO: YOUR CODE HERE
    
    return # Remember to output your solution; replace this line when you're done!

def main():
    T = int(input().strip())
    for _ in range(T):
        logic(read())

if __name__ == "__main__":
    main()