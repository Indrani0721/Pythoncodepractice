def total_spent(filename):
    total = 0
    with open(filename) as f:
        for line in f:
            parts = line.split()
            qty = int(parts[1])
            price = float(parts[2])
            total = total + qty * price
    return total

print(total_spent("receipt.txt"))