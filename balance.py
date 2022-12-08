def split_bills(bills, goal, total, split):
    if total/split < goal:
        print("Not enough cash to split {} ways!".format(split))
    else:
        split_bills = []
        remainder = []
        for i in range(len(bills)):
            remainder.append(bills[i] % split)
            split_bills.append(bills[i] // split)
    return split_bills, remainder

def balance_drawer(denom, bills, total, goal, place):
    if total < goal:
        return "DIDN'T WORK"
    
    if total == goal:
        return bills

    if total > goal:
        if total-goal >= denom[place] and bills[place] > 0:
            bills[place] -= 1
            return balance_drawer(denom, bills, total-denom[place],goal,place)
        else:
            return balance_drawer(denom, bills,total,goal,place+1)


    