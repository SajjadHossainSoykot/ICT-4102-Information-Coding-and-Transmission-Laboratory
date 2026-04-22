def shannon_fano_coding(data):
    items = list(data.items())

    # Base case: only one symbol
    if len(items) == 1:
        return {items[0][0]: ""}

    # Sort by probability in descending order
    items.sort(key=lambda x: x[1], reverse=True)

    total = sum(prob for symbol, prob in items)
    cumulative = 0
    split_index = 0

    # Find split point
    for i in range(len(items)):
        cumulative += items[i][1]
        if cumulative >= total / 2:
            split_index = i
            break

    # Divide into two groups
    left_data = dict(items[:split_index + 1])
    right_data = dict(items[split_index + 1:])

    # Recursive code assignment
    codes = {}

    left_codes = shannon_fano_coding(left_data)
    for symbol in left_codes:
        codes[symbol] = "0" + left_codes[symbol]

    if right_data:
        right_codes = shannon_fano_coding(right_data)
        for symbol in right_codes:
            codes[symbol] = "1" + right_codes[symbol]

    return codes


# Input data
data = {
    'A': 0.4,
    'B': 0.3,
    'C': 0.2,
    'D': 0.05,
    'E': 0.05
}

# Generate codes
codes = shannon_fano_coding(data)

# Display output
print("Shannon-Fano Codes:")
print("Symbol\tProbability\tCode")

for symbol in data:
    print(f"{symbol}\t{data[symbol]}\t\t{codes[symbol]}")