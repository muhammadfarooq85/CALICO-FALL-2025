name = "frame"

def read():
    case = input().strip().split(" ")
    return case

def logic(case):
    phrase = case
    max_len = max([len(word) for word in phrase])  # Find longest word length
    ans = ""
    
    # Build top border
    for _ in range(max_len + 2):
        ans += "*"
    ans += "\n"
    
    # Build word lines
    for word in phrase:
        ans += "*"
        ans += word
        for _ in range(max_len - len(word)):  # Add padding spaces
            ans += " "
        ans += "*\n"
    
    # Build bottom border  
    for _ in range(max_len + 2):
        ans += "*"
    ans += "\n"
    return ans

def write(solution):
    print(solution)
    print("")  # Adds blank line after each test case

def main():
    T = int(input().strip())  # Read number of test cases
    for _ in range(T):
        write(logic(read()))

if __name__ == "__main__":
    main()