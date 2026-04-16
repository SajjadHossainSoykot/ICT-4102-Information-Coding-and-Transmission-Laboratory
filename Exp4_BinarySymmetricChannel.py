import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the binary entropy function H(p)
def binary_entropy(p):
    # Ensure p is not exactly 0 or 1 to avoid log(0) errors
    p = np.clip(p, 1e-10, 1 - 1e-10)  # Clip to avoid exact 0 or 1 values
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)

# Step 2: Define the channel capacity function
def bsc_capacity(p):
    return 1 - binary_entropy(p)

# Step 3: Input the probability of error p
p = float(input("Enter the probability of error (p) between 0 and 0.5: "))

# Step 4: Calculate the channel capacity
capacity = bsc_capacity(p)

# Step 5: Display the result
print(f"Channel Capacity of BSC with error probability {p}: {capacity:.4f} bits/channel use")

# Plotting the channel capacity as a function of error probability p
p_values = np.linspace(0, 0.5, 100)  # Error probability range from 0 to 0.5
capacity_values = bsc_capacity(p_values)

plt.plot(p_values, capacity_values, label="Channel Capacity")
plt.title("Binary Symmetric Channel Capacity")
plt.xlabel("Error Probability (p)")
plt.ylabel("Channel Capacity (C)")
plt.grid(True)
plt.legend()
plt.show()