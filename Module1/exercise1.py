#!/usr/bin/env python
# Module 1: Overview of Signal Processing
# Exercise 1: Generating and Plotting Signals

import numpy as np
import matplotlib.pyplot as plt

# Time variables
t = np.linspace(0, 1, 500)  # 1 seconds, 500 sanmples

# Generate a sine wave (analog signal, could be a voltage, current, etc.)
frequency = 5  # 5 Hz
amplitude = 1  # Amplitude of the signal
analog_signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Convert the analog signal to a digital signal by sampling
sampling_rate = 50  # 50 samples per second
sampling_interval = 1 / sampling_rate  # 1 / 50 = 0.02 s (collecting data every 0.02 seconds)
t_digital = np.arange(0, 1, sampling_interval)
digital_signal = amplitude * np.sin(2 * np.pi * frequency * t_digital)

# Plotting the analog and digital signals
plt.figure(figsize=(10, 6))

# Plot the analog signal
plt.subplot(2, 1, 1)
plt.plot(t, analog_signal)
plt.title("Analog Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot the digital signal
plt.subplot(2, 1, 2)
markerline, stemlines, baseline = plt.stem(t_digital, digital_signal)
#plt.plot(t_digital, digital_signal)
plt.title("Digital Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
