import psutil

# warm-up to avoid first-call zero values
psutil.cpu_percent(interval=None)

# returns current CPU usage percentage
def get_cpu():
    return psutil.cpu_percent(interval=None)

# returns current RAM usage percentage
def get_ram():
    mem = psutil.virtual_memory()
    return mem.percent

# returns snapshot of running processes with CPU and memory stats
def get_processes():
    processes = []

    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            # initialize CPU measurement for process
            p.cpu_percent(None)
            processes.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return processes