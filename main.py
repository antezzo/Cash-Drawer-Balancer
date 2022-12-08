import balance

DENOMINATIONS = [100, 50, 20, 10, 5, 1]

def get_counts():
    print("Please enter the number of bills for ALL denominations, separated by commas with no spaces")
    bill_str = input("(100,50,20,10,5,1): ")
    return list(map(int, bill_str.split(",")))

def split_drawers(bills, drawer_goal, total):
    split = int(input("Please enter the number of drawers you would like to balance: "))
    split_bills, remainder = balance.split_bills(bills,drawer_goal,total,split)

    if split > 1:
        drawers = []
        for i in range(split):
            if i == split - 1:
                drawers.append([i1 + i2 for i1, i2 in zip(split_bills, remainder)])
            else:
                drawers.append(split_bills)
    else:
        drawers = [split_bills]

    return drawers, split

def pretty_output(bills):
    for i in range(len(bills)):
        print("${}: {} (${})".format(DENOMINATIONS[i],bills[i],DENOMINATIONS[i] * bills[i]))
    total = sum([i1 * i2 for i1, i2 in zip(DENOMINATIONS, bills)])
    print("TOTAL: ${}".format(total))

def main_output(total, drawers, split, remainder):
    print("----- TOTAL -----")
    print("TOTAL: ${}".format(total))
    for i in range(split):
        print("----- DRAWER {} COUNT -----".format(i+1))
        pretty_output(drawers[i])
    print("----- REMAINDER COUNT -----")
    pretty_output(remainder)

if __name__ == "__main__":
    # bills = [4, 5, 25, 15, 37, 43]

    bills = get_counts()
    bills_copy = bills.copy()
    drawer_goal = int(input("Please enter your desired drawer total: "))
    total = sum([i1 * i2 for i1, i2 in zip(DENOMINATIONS, bills)])

    drawers, split = split_drawers(bills,drawer_goal,total)
         
    for drawer in drawers:
        drawer_total = sum([i1 * i2 for i1, i2 in zip(DENOMINATIONS, drawer)])
        balance.balance_drawer(DENOMINATIONS, drawer, drawer_total, drawer_goal, 0)

    drawers_total = [sum(i) for i in zip(*drawers)]
    balanced_remainder = [i1 - i2 for i1, i2 in zip(bills_copy, drawers_total)]
    
    main_output(total,drawers,split,balanced_remainder)