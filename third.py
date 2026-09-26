#1 Write a function called most_expensive_item(filename) 
# that returns just the name of the most expensive single line item
# (not total spent, not filtered by threshold — literally: find the 
#  highest cost and return that item's name).

def most_expensive_item(filename):
    best_cost = 0
    best_name = ""
    with open(filename) as f:
        for line in f:
            parts = line.split()
            qty = int(parts[1])
            price = float(parts[2])
            cost = qty * price
            if cost > best_cost:
                best_cost = cost
                best_name = parts[0]
    return best_name
print(most_expensive_item("receipt.txt"))

#output:gives the expensive item name from the receipt.txt file