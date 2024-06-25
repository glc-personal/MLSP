#!/usr/bin/env python3.11
# Module 1: Overview of Signal Processing
# Exercise 1.1.b: Sampling Rate and Sampling Interval

import numpy as np
import matplotlib.pyplot as plt

# Continuous timevariable
t_continuous = np.linspace(0, 2, 1000)  # 2 seconds, 1000 samples

# Generate a sine wave to simulate water ripples
frequency = 2  # 2 Hz (ripple frequency)
amplitude = 1  # Amplitude of the ripples
analog_signal = amplitude * np.sin(2 * np.pi * frequency * t_continuous)

# Sampling the continuous signal at different rates
sampling_rate_1 = 10  # 10 samples per second
sampling_rate_2 = 50  # 50 samples per second
sampling_interval_1 = 1 / sampling_rate_1
sampling_interval_2 = 1 / sampling_rate_2

# Setup the time variables for these two digital signals
t_sample_1 = np.arange(0, 2, sampling_interval_1)
t_sample_2 = np.arange(0, 2, sampling_interval_2)

# Setup the two digital signals
sampled_signal_1 = amplitude * np.sin(2 * np.pi * frequency * t_sample_1)
sampled_signal_2 = amplitude * np.sin(2 * np.pi * frequency * t_sample_2)

# Plotting the analog and sampled signals
plt.figure(figsize=(12,8))

# Plot the analog signal
plt.subplot(3, 1, 1)
plt.plot(t_continuous, analog_signal, label="Analog Signal")
plt.title("Analog Signal (Continuous)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Plot the sampled signal with the lower sampling rate
plt.subplot(3, 1, 2)
markerline1, stemline1, baseline1 = plt.stem(t_sample_1, sampled_signal_1)
plt.title("Sampled Signal (10 Hz Sampling Rate)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Plot the sampled signal with the higher sampling rate
plt.subplot(3, 1, 3)
markerline2, stemline2, baseline2 = plt.stem(t_sample_2, sampled_signal_2)
plt.title("Sampled Signal (50 Hz Sampling Rate)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
