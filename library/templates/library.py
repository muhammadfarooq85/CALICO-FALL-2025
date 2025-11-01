name = "library"

def read():
    case = {}
    info = input().strip().split(" ")
    case["absent"] = info[0]
    case["n"] = int(info[1])
    case["transactions"] = []
    for _ in range(case["n"]):
        info = input().strip().split(" ")
        name = info[0]
        owner = info[3][:-2]
        transaction = (name, owner)
        case["transactions"].append(transaction)
    return case

def logic(case):
    absent, n, transactions = case["absent"], case["n"], case["transactions"]
    people = [absent]
    for t in transactions:
        people.append(t[0])
    for t in transactions:
        people.remove(t[1])
    return absent, people[0]

def write(solution):
    absent, owner = solution
    print("{} HAS {}'s BOOK".format(absent, owner))

def main():
    T = int(input().strip())
    for _ in range(T):
        write(logic(read()))
        input() # Remember the blank line in between test cases!

if __name__ == "__main__":
    main()