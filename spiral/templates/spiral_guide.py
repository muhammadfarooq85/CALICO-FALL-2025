name = "spiral"

# You don't need to do anything here; I've already written it for you! You're welcome
def read():
    # Read in the input, remove any leading/trailing whitespace, and turn it into an integer
    case = int(input().strip())
    
    return case

def logic(case):
    # n: A positive integer denoting the number of loops the spiral must have
    n = case
    # It's your turn to code! Use the variable(s) above to find your answer
    
    # TODO: YOUR CODE HERE
    
    return # Remember to output your solution; replace this line when you're done!

def main():
    T = int(input().strip())
    for _ in range(T):
        logic(read())
        print("") # Remember the blank line in between outputs!

if __name__ == "__main__":
    main()