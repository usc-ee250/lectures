import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parameters for 802.15.4 baseband
bitrate = 250e3  # 250 kbps
chiprate = bitrate * 8  # Chipping sequence rate (8 chips per bit)

# Simulation time
time_duration = 1e-3  # 1 ms of transmission
num_bits = int(bitrate * time_duration)  # Number of bits in 1 ms
num_chips = int(chiprate * time_duration)  # Number of chips in 1 ms

# Generate random baseband signal (0 and 1 bits)
bits = np.random.randint(0, 2, num_bits)

# Map bits to bipolar (-1, 1)
baseband_signal = 2 * bits - 1

# Generate chipping sequence (8 chips per bit)
chipping_sequence = np.random.choice([-1, 1], size=8)

# Apply spreading by repeating each bit as 8 chips (direct sequence spreading)
spread_signal = np.repeat(baseband_signal, 8) * np.tile(chipping_sequence, num_bits)

# Compute power spectral density (PSD) for both signals
frequencies, psd_baseband = signal.welch(baseband_signal, fs=bitrate, nperseg=1024)
frequencies, psd_spread = signal.welch(spread_signal, fs=chiprate, nperseg=1024)

# Plot the results
plt.figure(figsize=(12, 6))

# Plot PSD of baseband signal
plt.subplot(2, 1, 1)
plt.semilogy(frequencies, psd_baseband)
plt.title('Power Spectral Density of Baseband Signal (250 kbps)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power/Frequency (dB/Hz)')
plt.grid(True)

# Plot PSD of spread signal
plt.subplot(2, 1, 2)
plt.semilogy(frequencies, psd_spread)
plt.title('Power Spectral Density of Spread Signal (32-chips per bit)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power/Frequency (dB/Hz)')
plt.grid(True)

plt.tight_layout()
plt.show()
