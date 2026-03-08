from itertools import combinations

patients = [
    ['fever', 'cough', 'fatigue'],
    ['fever', 'cough'],
    ['cough', 'fatigue'],
    ['fever', 'fatigue'],
    ['fever', 'cough', 'headache']
]

min_support = 2

items = set(item for p in patients for item in p)

def support(itemset):
    count = 0
    for p in patients:
        if set(itemset).issubset(set(p)):
            count += 1
    return count

print("Frequent Itemsets (Healthcare):")

for i in range(1,3):
    for combo in combinations(items,i):
        s = support(combo)
        if s >= min_support:
            print(combo, "support:", s)