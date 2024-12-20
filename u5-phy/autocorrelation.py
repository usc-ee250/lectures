# Auto-Generated by ChatGPT
# import numpy as np
import matplotlib.pyplot as plt

# Generate a pseudo-noise (PN) sequence
pn_sequence = np.array([1, -1, 1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1])

# Auto-correlation of the PN sequence
auto_corr = np.correlate(pn_sequence, pn_sequence, mode='full')

# Normalize the auto-correlation
auto_corr = auto_corr / np.max(auto_corr)

# Generate lags for the plot
lags = np.arange(-len(pn_sequence)+1, len(pn_sequence))

# Plot the auto-correlation function
plt.figure(figsize=(8, 5))
plt.stem(lags, auto_corr, use_line_collection=True)
plt.title('Auto-correlation of PN Sequence')
plt.xlabel('Lag')
plt.ylabel('Normalized Auto-correlation')
plt.grid(True)
plt.show()
