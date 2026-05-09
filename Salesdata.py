import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [5000, 7000, 6500, 8000, 9000, 8500]

# Create line chart
plt.plot(months, sales, marker='o', label="Sales")

# Title and labels
plt.title("Monthly Sales Data")
plt.xlabel("Months")
plt.ylabel("Sales Amount")

# Grid and legend
plt.grid(True)
plt.legend()

# Display chart
plt.show()