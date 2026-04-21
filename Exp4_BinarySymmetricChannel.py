import numpy as np
import matplotlib.pyplot as plt

# Binary entropy function
def binary_entropy(p):
    p = np.clip(p, 1e-10, 1 - 1e-10)
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)

# Channel capacity function
def bsc_capacity(p):
    return 1 - binary_entropy(p)

# Input
p = float(input("Enter the probability of error (p) between 0 and 0.5: "))

# Validation
if p < 0 or p > 0.5:
    raise ValueError("p must be between 0 and 0.5")

# Calculation
capacity = bsc_capacity(p)

print(f"Channel Capacity of BSC with error probability {p}: {capacity:.4f} bits/channel use")

# Plot
p_values = np.linspace(0, 0.5, 100)
capacity_values = bsc_capacity(p_values)

plt.plot(p_values, capacity_values, label="Channel Capacity")
plt.title("Binary Symmetric Channel Capacity")
plt.xlabel("Error Probability (p)")
plt.ylabel("Channel Capacity (C)")
plt.grid(True)
plt.legend()
plt.show()