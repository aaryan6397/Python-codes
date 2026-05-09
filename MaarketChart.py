import matplotlib.pyplot as plt

# Data
brands = ["Samsung", "Apple", "Xiaomi", "OnePlus", "Vivo"]
share = [35, 30, 15, 10, 10]

# Highlight maximum share
explode = [0.1, 0, 0, 0, 0]

# Pie chart
plt.pie(share,
        labels=brands,
        autopct='%1.1f%%',
        explode=explode,
        shadow=True)

# Title
plt.title("Smartphone Market Share")

# Display chart
plt.show()