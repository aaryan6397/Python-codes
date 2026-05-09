import numpy as np
import matplotlib.pyplot as plt

# Generate random temperature data
temperature = np.random.normal(30, 5, 100)

# Plot histogram
plt.hist(temperature, bins=10)

# Labels and title
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")

# Display chart
plt.show()