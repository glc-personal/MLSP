#!/usr/bin/env python3.11

# Module 1: Overview of Signal Processing
# Exercise: Ripple Demo
# Summary: Animation of two different pebbles causing two sets of wave fronts
#	allowing for visualization of the continuos signal and a visualization
# 	of the Sampling Theorem.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
grid_size = 100  # Grid size (x and z dimensions)
time_steps = 100  # Number of time steps in the animation
wave_speed = 0.1  # Speed of the ripple propagation
pebble_drop_times = [10, 40]  # Times at which pebbles drop (in time steps)

# Create a 2D grid of points
x = np.linspace(-5, 5, grid_size)
z = np.linspace(-5, 5, grid_size)
x, z = np.meshgrid(x, z)

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_title('2D Water Ripple Time-Lapse')
ax.set_xlabel('X')
ax.set_ylabel('Z')

# Function to generate the ripple effect at a given time t
def generate_ripple(x, z, center, time, width=1.0, decay=0.05):
    r = np.sqrt((x - center[0])**2 + (z - center[1])**2)
    ripple = np.exp(-(r**2) / (2 * width**2)) * np.sin(2 * np.pi * (r - wave_speed * time))
    return ripple * np.exp(-decay * time)

# Initialize the ripple data
ripple_data = np.zeros_like(x)

# Initialize the plot with the first frame
ripple_plot = ax.imshow(ripple_data, extent=(-5, 5, -5, 5), cmap='viridis', origin='lower', animated=True)

# Initialize the time step text
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, color='white', fontsize=12)

# Update function for the animation
def update(frame):
    global ripple_data
    ripple_data.fill(0)  # Reset the grid
    for drop_time in pebble_drop_times:
        if frame >= drop_time:
            ripple = generate_ripple(x, z, (0, 0), frame - drop_time)
            ripple_data += ripple
    ripple_plot.set_array(ripple_data)
    time_text.set_text(f'Time step: {frame}')
    return [ripple_plot, time_text]

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(time_steps), blit=True, interval=100)

# Display the animation
plt.colorbar(ripple_plot, ax=ax)
plt.show()

