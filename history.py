# in-memory time series storage for system metrics

history = {
    "time": [],  # timestamps
    "cpu": [],   # cpu usage samples
    "ram": [],   # ram usage samples
    "process_count": []  # number of running processes
}

# append a new snapshot into history buffers
def add_snapshot(t, cpu, ram, process_count):
    history["time"].append(t)
    history["cpu"].append(cpu)
    history["ram"].append(ram)
    history["process_count"].append(process_count)