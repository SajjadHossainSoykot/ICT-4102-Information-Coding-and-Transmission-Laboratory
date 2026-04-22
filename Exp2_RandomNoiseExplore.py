import numpy as np
import matplotlib.pyplot as plt

# Simulate a clean signal (a simple sine wave)
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs)  # Time vector
freq = 5  # Frequency of the sine wave
clean_signal = np.sin(2 * np.pi * freq * t)

# Noise Characteristics
means = [0, 1, -1]  # Different means of noise
variances = [0.1, 1, 10]  # Different variances of noise

#Plot Clean Signal
plt.figure(figsize=(15,3))
plt.plot(t, clean_signal)
plt.title("Clean Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

#Plot Noise Signals in grid
fig, axes = plt.subplots(len(means),len(variances),figsize=(15,10))
snr_values={}

for i, mean in enumerate(means):
    for j, variance in enumerate (variances):
        noise = np.random.normal(mean, np.sqrt(variance),fs)
        noisy_signal = clean_signal + noise
        
        #Plot        
        axes[i,j].plot(t,noisy_signal)
        axes[i,j].set_title(f"Mean={mean}, Var={variance}")
        axes[i,j].grid()
        
        #SNR
        signal_power = np.var(clean_signal)
        noise_power = np.var(noise)
        snr=10*np.log10(signal_power/noise_power)
        snr_values[(mean,variance)] = snr
        
plt.tight_layout()
plt.show()

#Print SNR
print("\nSNR Results (dB):")
print(f"{'Mean':>5} {'Variance':>10} {'SNR (dB)':>12}")
print("-" * 30)

for (mean, variance), snr in snr_values.items():
    print(f"{mean:5} {variance:10} {snr:12.2f}")