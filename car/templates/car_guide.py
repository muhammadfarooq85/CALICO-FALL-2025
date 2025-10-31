name = "car"

# You don't need to do anything here; I've already written it for you! You're welcome
def read():
    # Creates a dictionary to store the inputs
    case = {}
    
    # Read in the input, remove any leading/trailing whitespace, and break it up over the colon
    # Ex: turns "12.33:39.33" into ["12.33", "39.33"]
    info = input().strip().split(":")
    
    # Turn the string into a decimal value
    case["v"] = float(info[0])
    # Turns the string into a decimal value
    case["x"] = float(info[1])
    
    return case

def logic(case):
    # v: A non-negative decimal value denoting the vehicle’s current speed (in m/s)
    # x: A positive decimal value denoting the obstacle distance from the front of the car (in m)
    v, x = case["v"], case["x"]
    # It's your turn to code! Use the variable(s) above to find your answer
    
    # TODO: YOUR CODE HERE
    
    return # Remember to output your solution; replace this line when you're done!

def main():
    T = int(input().strip())
    for _ in range(T):
        logic(read())

if __name__ == "__main__":
    main()