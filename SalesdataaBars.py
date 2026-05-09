import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("sales.csv")

# Plot bar chart
plt.bar(df["Product"], df["Sales"])

# Labels and title
plt.title("Product-wise Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

# Display chart
plt.show()