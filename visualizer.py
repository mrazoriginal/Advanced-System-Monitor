import matplotlib.pyplot as plt

# visualizes CPU and RAM usage over time
def plot(history):
    plt.figure()
    # CPU usage trend
    plt.plot(history["cpu"])
    plt.title("CPU Usage Over Time")
    plt.xlabel("Time")
    plt.ylabel("CPU %")
    plt.show()

    plt.figure()
    # RAM usage trend
    plt.plot(history["ram"])
    plt.title("RAM Usage Over Time")
    plt.xlabel("Time")
    plt.ylabel("RAM %")
    plt.show()