name = "car"

def read():
    case = {}
    info = input().strip().split(":")
    case["v"] = float(info[0])
    case["x"] = float(info[1])
    return case

def logic(case):
    # v: A non-negative decimal value denoting the vehicle’s current speed (in m/s)
    # x: A positive decimal value denoting the obstacle distance from the front of the car (in m)
    v, x = case["v"], case["x"]
    
    # TODO: YOUR CODE

    if v == 0:
        return "SAFE"

    # using the basic formula to extract the time
    time = x / v

    if time <= 1:
        return "SWERVE"
    if time <= 5:
        return "BRAKE"
    else:
        return "SAFE"    

def main():
    T = int(input().strip())
    for _ in range(T):
        result = logic(read())
        print(result)

if __name__ == "__main__":
    main()