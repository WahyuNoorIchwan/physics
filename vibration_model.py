import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 10
w = 0.25
n = 50

# Model Matrix - t and y
model = np.zeros((n, 2))
model[:, 0] = range(50)

# Calculate y
for i in range(n):
    model[i, 1] = A*np.sin(w*model[i, 0])
    
# Plot Vibration Model
fig, ax = plt.subplots()
fig.set_size_inches(8, 4)

ax.scatter(model[:, 0], model[:, 1])
ax.set_title("Vibration Simulation")
ax.set_xlabel("Time")
ax.set_ylabel("Deviation")

plt.show()