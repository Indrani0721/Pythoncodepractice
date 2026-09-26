total = 0
items = {}

with open("receipt.txt") as f:
    for line in f:
        parts = line.split()
        name = parts[0]
        qty = int(parts[1])
        price = float(parts[2])
        cost = qty * price
        total = total + cost
        items[name] = cost

print(total)
print(max(items, key=items.get))