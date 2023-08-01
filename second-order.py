import matplotlib.pyplot as plt
import random

number_of_points = 100
iteration = 100  # Change number of iterations here

def multiple_randomizer():
    n = 0
    x = 100
    while n < iteration:
        x = random.randint(0, x)  # Recursive randomizer function
        n = n + 1
    return x

def populator(number_of_points):
    n = 0
    coordinates = []
    while n < number_of_points:
        x = multiple_randomizer()
        coordinates.append(x)
        n = n + 1
    return coordinates

def zipper(list_x, list_y):
    coordinates = list(zip(list_x, list_y))
    return coordinates

def plotter(coordinates):
    # Create list of x and y values

    x_values = []
    y_values = []

    for coord in coordinates:
        x = coord[0]
        x_values.append(x)
        y = coord[1]
        y_values.append(y)

    plt.scatter(x_values, y_values)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    title = "Iteration = " + str(iteration)
    plt.title(title)
    plt.show()

# Step 1. Generate random data for x and y

coordinates_x = populator(number_of_points)
coordinates_y = populator(number_of_points)

# Step 2. Create data points (x,y)

coordinates = zipper(coordinates_x, coordinates_y)

# Step 3. Plot the graph

plotter(coordinates)
