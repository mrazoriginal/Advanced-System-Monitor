import matplotlib.pyplot as plt

def plot(history):
    plt.figure()
    plt.plot(history["cpu"])
    plt.title("CPU Usage Over Time")
    plt.xlabel("Time")
    plt.ylabel("CPU %")
    plt.show()

    plt.figure()
    plt.plot(history["ram"])
    plt.title("RAM Usage Over Time")
    plt.xlabel("Time")
    plt.ylabel("RAM %")
    plt.show()
