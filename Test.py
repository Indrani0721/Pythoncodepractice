#2Add a feature to count how many total items (not lines — actual quantity) were bought. 
# Example: apples 3 1.20 contributes 3 to that count, bananas 6 0.30 contributes 6, etc. 
# Sum all the quantities across every line and print the total at the end, alongside 
# total and most_expensive_item.

def most_expensive_item(filename):
    best_cost = 0
    best_name = ""
    total_quantity = 0
    with open(filename) as f:
        for line in f:
            parts = line.split()
            qty = int(parts[1])
            price = float(parts[2])
            cost = qty * price
            if cost > best_cost:
                best_cost = cost
                best_name = parts[0]
            total_quantity += qty
    return best_name, total_quantity

print(most_expensive_item("receipt.txt"))