from itertools import combinations

transactions = [
    ['printer', 'ink', 'paper'],
    ['paper', 'stapler'],
    ['printer', 'ink'],
    ['paper', 'ink'],
    ['printer', 'paper']
]

min_support = 2

items = set(item for t in transactions for item in t)

def get_support(itemset):
    count = 0
    for t in transactions:
        if set(itemset).issubset(set(t)):
            count += 1
    return count

print("Frequent Itemsets (Supply Analysis):")

for i in range(1,3):
    for combo in combinations(items,i):
        support = get_support(combo)
        if support >= min_support:
            print(combo, "support:", support)