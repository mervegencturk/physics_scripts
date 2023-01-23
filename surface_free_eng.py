import numpy as np

# Constants
R = 8.314 # J/mol*K
T = 298 # K

# Input data
molar_mass = input("Enter the molar mass of the material (g/mol): ")
molar_mass = float(molar_mass)
surface_area = input("Enter the surface area of the material (m^2): ")
surface_area = float(surface_area)

# Calculation
molar_volume = molar_mass / (0.6022 * 1E+03) # m^3/mol
surface_free_energy = 2 * (R * T * np.log(surface_area / molar_volume)) / (surface_area * 1E-4) # J/cm^2

# Output
print("The surface free energy of the material is {:.2f} J/cm^2".format(surface_free_energy))
