#!/usr/bin/env python3.11

# Module 1: Overview of Signal Processing
# Exercise 2: Demonstrating the Sampling Theorem

import numpy as np
import matplotlib.pyplot as plt

# Continuous time variable
t = np.linspace(0, 1, 500)  # 1 second, 500 samples

# Original continuous signal (sine wave)
frequency_continuous = 10  # 10 Hz
continuous_signal = np.sin(2 * np.pi * frequency_continuous * t)

# Sampling the continuous signal at different rates
sampling_rate_1 = 20  # Less than the Nyquist rate
sampling_rate_2 = 40  # Exactly at the Nyquist rate
sampling_rate_3 = 80  # More than the Nyquist rate
sampling_interval_1 = 1 / sampling_rate_1
sampling_interval_2 = 1 / sampling_rate_2
sampling_interval_3 = 1 / sampling_rate_3
t_sample_1 = np.arange(0, 1, sampling_interval_1)
t_sample_2 = np.arange(0, 1, sampling_interval_2)
t_sample_3 = np.arange(0, 1, sampling_interval_3)
sampled_signal_1 = np.sin(2 * np.pi * frequency_continuous * t_sample_1)
sampled_signal_2 = np.sin(2 * np.pi * frequency_continuous * t_sample_2)
sampled_signal_3 = np.sin(2 * np.pi * frequency_continuous * t_sample_3)

# Plot the signals
plt.figure(figsize=(12, 8))

# Original continuous signal
plt.subplot(4, 1, 1)
plt.plot(t, continuous_signal)
plt.title("Original Continuous Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Sampled Signal 1 (below the Nyquist Frequency)
plt.subplot(4, 1, 2)
markerline1, stemline1, baseline1 = plt.stem(t_sample_1, sampled_signal_1)
plt.title("Below Nyquist Frequency")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Sampled Signal 2 (at the Nyquist Frequency)
plt.subplot(4, 1, 3)
markerline2, stemline2, baseline2 = plt.stem(t_sample_2, sampled_signal_2)
plt.title("At Nyquist Frequency")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Sampled Signal 3 (above tthe Nyquist Frequency)
plt.subplot(4, 1, 4)
markerline3, stemline3, baseline3 = plt.stem(t_sample_3, sampled_signal_3)
plt.title("Above Nyquist Frequency")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
