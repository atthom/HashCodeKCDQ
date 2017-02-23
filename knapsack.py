def totalvalue(comb):
    ' Totalise a particular combination of items'
    totwt = totval = 0
    for item, wt, val in comb:
        totwt += wt
        totval += val
    return (totval, -totwt) if totwt <= 400 else (0, 0)


# item (name, weight, value)




def add_item(item, items):
    items.append(item)


items = [
    (0, 9, 150), (1, 13, 35), (2, 153, 200), (3, 50, 160),
    (4, 15, 60), (5, 68, 45), (6, 27, 60), (7, 39, 40),
    (8, 23, 30), (9, 52, 10), (10, 11, 70), (11, 32, 30),
    (12, 24, 15), (13, 48, 10), (14, 73, 40), (15, 42, 70), (16, 43, 75),
    (17, 22, 80), (18, 7, 20), (19, 18, 12), (20, 4, 50), (21, 30, 10)
]


def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for j in range(len(items) + 1)]

    for j in range(1, len(items) + 1):
        item, wt, val = items[j - 1]
        for w in range(1, limit + 1):
            if wt > w:
                table[j][w] = table[j - 1][w]
            else:
                table[j][w] = max(table[j - 1][w],
                                  table[j - 1][w - wt] + val)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j - 1][w]

        if was_added:
            item, wt, val = items[j - 1]
            result.append(items[j - 1])
            w -= wt

    return result




def solve_it(tab_of_tab_request_servers, sizeof_server):
    result = []
    for tab_for_one_server in tab_of_tab_request_servers:
        result.append(knapsack01_dp(tab_for_one_server, sizeof_server))



print(items)
add_item((21, 2, 20), items)
print(items)




bagged = knapsack01_dp(items, 400)
#print("Bagged the following items\n  " +
#      '\n  '.join(sorted(item for item, _, _ in bagged)))
#val, wt = totalvalue(bagged)
#print("for a total value of %i and a total weight of %i" % (val, -wt))