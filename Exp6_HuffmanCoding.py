import heapq

def huffman_coding(data):
    # Create heap
    heap = [[weight, [symbol, ""]] for symbol, weight in data.items()]
    heapq.heapify(heap)

    # Build Huffman Tree
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]

        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Final codes
    return dict(heapq.heappop(heap)[1:])


# Input data
data = {
    'A': 0.4,
    'B': 0.3,
    'C': 0.2,
    'D': 0.05,
    'E': 0.05
}

# Generate codes
codes = huffman_coding(data)

# Display output
print("Huffman Codes:")
print("Symbol\tFrequency\tCode")

for symbol in data:
    print(f"{symbol}\t{data[symbol]}\t\t{codes[symbol]}")