#!/usr/bin/env python3.11

# Module 1: Overview of Signal Processing
# Exercide 3: Fourier Transform and Frequency Domain Analysis

import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

# Parameters
N = 500  # Number of samples
T = 1.0 / 500.0  # Sample spacing (space between samples in time)

# Continuous time variable
t = np.linspace(0, 1, N)

# Signal generation: a sum of 50 Hz and 80 Hz sine waves
signal = np.sin(50.0 * 2.0 * np.pi * t) + 0.5 * np.sin(80.0 * 2.0 * np.pi * t)

# Compute the FFT of the signal
yf = fft(signal)
xf = fftfreq(N, T)[:N // 2]

# Plot the original signal
plt.figure(figsize=(12,8))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Original Signal in Time Domain")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Plot the frequency domain representation of this signal
plt.subplot(2, 1, 2)
plt.plot(xf, 2.0 / N * np.abs(yf[:N // 2]))
plt.title("Signal in the Frequency Domain")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()
