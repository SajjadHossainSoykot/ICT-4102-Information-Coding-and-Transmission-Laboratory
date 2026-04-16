import numpy as np
import matplotlib.pyplot as plt

# Simulate a clean signal (a simple sine wave)
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs)  # Time vector
freq = 5  # Frequency of the sine wave
clean_signal = np.sin(2 * np.pi * freq * t)

# 1. Gaussian Noise
mean = 0
variance = 0.5  # Noise variance
gaussian_noise = np.random.normal(mean, np.sqrt(variance), fs)
noisy_signal_gaussian = clean_signal + gaussian_noise

# 2. Impulse Noise
impulse_noise = np.zeros(fs)
impulse_positions = np.random.randint(0, fs, size=50)  # Random positions for impulses
impulse_noise[impulse_positions] = np.random.choice([-5, 5], size=50)  # Impulse values
noisy_signal_impulse = clean_signal + impulse_noise

# 3. White Noise
white_noise = np.random.uniform(-1, 1, fs)  # Uniform distribution for white noise
noisy_signal_white = clean_signal + white_noise

# Plot the clean signal and the noisy signals
plt.figure(figsize=(10, 12))

# Clean Signal Plot
plt.subplot(4, 1, 1)
plt.plot(t, clean_signal)
plt.title("Clean Signal (Sine Wave)")

# Noisy Signal with Gaussian Noise
plt.subplot(4, 1, 2)
plt.plot(t, noisy_signal_gaussian)
plt.title("Noisy Signal with Gaussian Noise")

# Noisy Signal with Impulse Noise
plt.subplot(4, 1, 3)
plt.plot(t, noisy_signal_impulse)
plt.title("Noisy Signal with Impulse Noise")

# Noisy Signal with White Noise
plt.subplot(4, 1, 4)
plt.plot(t, noisy_signal_white)
plt.title("Noisy Signal with White Noise")

plt.tight_layout()
plt.show()

# Calculate Signal-to-Noise Ratio (SNR) for each type of noise
snr_gaussian = 10 * np.log10(np.var(clean_signal) / np.var(gaussian_noise))
snr_impulse = 10 * np.log10(np.var(clean_signal) / np.var(impulse_noise))
snr_white = 10 * np.log10(np.var(clean_signal) / np.var(white_noise))

print(f"Signal-to-Noise Ratio (SNR) with Gaussian Noise: {snr_gaussian:.2f} dB")
print(f"Signal-to-Noise Ratio (SNR) with Impulse Noise: {snr_impulse:.2f} dB")
print(f"Signal-to-Noise Ratio (SNR) with White Noise: {snr_white:.2f} dB")