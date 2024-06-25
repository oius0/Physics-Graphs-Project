import matplotlib.pyplot as plt
import numpy as np

# Given values
wavelength = 500e-9  # meters (500 nm)
slit_separation = 0.1e-3  # meters (0.1 mm)
distance_to_screen = 1  # meters

# Calculations
fringe_spacing = (wavelength * distance_to_screen) / slit_separation
angular_separation = wavelength / slit_separation
path_difference_first_order = wavelength
screen_width = 0.5  # meters (assuming)
number_of_fringes = int(screen_width / fringe_spacing)

# Time intervals
time = np.linspace(0, 10, 100)

# Graph 1: Intensity Pattern vs Position
position = np.linspace(-0.05, 0.05, 1000)
intensity = np.cos(2 * np.pi * position / fringe_spacing)**2

plt.figure(figsize=(10, 6))
plt.plot(position, intensity, label='Intensity Pattern')
plt.xlabel('Position (m)')
plt.ylabel('Intensity')
plt.title('Intensity Pattern vs Position')
plt.legend()
plt.grid(True)
plt.show()

# Graph 2: Fringe Spacing vs Distance to Screen
distance_to_screen_values = np.linspace(0.5, 2, 100)
fringe_spacing_values = (wavelength * distance_to_screen_values) / slit_separation

plt.figure(figsize=(10, 6))
plt.plot(distance_to_screen_values, fringe_spacing_values, label='Fringe Spacing')
plt.xlabel('Distance to Screen (m)')
plt.ylabel('Fringe Spacing (m)')
plt.title('Fringe Spacing vs Distance to Screen')
plt.legend()
plt.grid(True)
plt.show()

# Graph 3: Angular Separation vs Wavelength
wavelength_values = np.linspace(400e-9, 700e-9, 100)
angular_separation_values = wavelength_values / slit_separation

plt.figure(figsize=(10, 6))
plt.plot(wavelength_values * 1e9, angular_separation_values, label='Angular Separation')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Angular Separation (rad)')
plt.title('Angular Separation vs Wavelength')
plt.legend()
plt.grid(True)
plt.show()

# Graph 4: Path Difference vs Order
order = np.arange(1, 11)
path_difference_values = order * wavelength

plt.figure(figsize=(10, 6))
plt.plot(order, path_difference_values * 1e9, label='Path Difference')
plt.xlabel('Order')
plt.ylabel('Path Difference (nm)')
plt.title('Path Difference vs Order')
plt.legend()
plt.grid(True)
plt.show()

# Graph 5: Number of Fringes vs Screen Width
screen_width_values = np.linspace(0.1, 1, 100)
number_of_fringes_values = screen_width_values / fringe_spacing

plt.figure(figsize=(10, 6))
plt.plot(screen_width_values, number_of_fringes_values, label='Number of Fringes')
plt.xlabel('Screen Width (m)')
plt.ylabel('Number of Fringes')
plt.title('Number of Fringes vs Screen Width')
plt.legend()
plt.grid(True)
plt.show()
