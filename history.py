history = {
    "time": [],
    "cpu": [],
    "ram": [],
    "process_count": []
}

def add_snapshot(t, cpu, ram, process_count):
    history["time"].append(t)
    history["cpu"].append(cpu)
    history["ram"].append(ram)
    history["process_count"].append(process_count)
