import matplotlib.pyplot as plt

wavelengths = [
    260.190809, 261.56786, 263.2687678, 265.854645, 266.345656, 268.76546, 272.480, 272.988, 273.5890, 275.0866, 276.8334, 278.3368, 279.945734
]
intensities = [
    12.3456789012, 23.4567890123, 16.5678901234, 12.6789012345, 11.2345678901, 
    22.3456754678, 19.4567835456, 21.5679012345, 10.1234567890, 20.2345678901, 
    18.3457856798, 27.4567890123, 18.5678901234
]

plt.figure(figsize=(10, 5))

# First plot: Wavelengths vs Intensities
plt.subplot(1, 2, 1)
plt.plot(wavelengths, intensities, label='Intensities Curve')
plt.title('Wavelengths vs Intensities')
plt.xlabel('Wavelengths (NM)')
plt.ylabel('Intensities')
plt.legend()
plt.grid(True)

# Second plot: Wavelengths distribution
plt.subplot(1, 2, 2)
plt.hist(wavelengths, bins=10, color='skyblue', edgecolor='black')
plt.title('Wavelengths Distribution')
plt.xlabel('Wavelengths (NM)')
plt.ylabel('Frequency')
plt.grid(True)

plt.tight_layout()
plt.show()
