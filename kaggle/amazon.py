def icountBoughtItems(m, cost):
    '''
    '''
    number_items = 0
    position = -1
    for item in cost:
        position += 1
        while m >= item: # if budget is enough
            m -= item
            cost[position] = item*2
            number_items += 1
            print(position)
        else:
            return number_items

def countBoughtItems(m, cost):
    '''
    '''
    og_cost = cost.copy()
    number_items = 0
    mult = 1
    while True:
        mult += 1
        for i in range(len(cost)):
            if m >= cost[i]: # if budget is enough
                m -= cost[i]
                cost[i] = og_cost[i] * mult
                number_items += 1
                print("enough, ", m, cost[i], number_items)
            else:
                return number_items

print(countBoughtItems(20, [3,3,5,2]))
print(countBoughtItems(10, [1]))


def countBoughtItems(m, cost):
    '''
    The function is expected to return a LONG_INTEGER.
    The function accepts following parameters:
        #  1. LONG_INTEGER m
        #  2. INTEGER_ARRAY cost
    '''
    number_items = 0
    mult = 1
    while True:
        mult += 1
        for i in range(len(cost)):
            if m >= cost[i]: # if budget is enough
                m -= cost[i]
                cost[i] = (cost[i] * mult)/(mult-1)
                number_items += 1
            else:
                return number_items