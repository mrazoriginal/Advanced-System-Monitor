import psutil

def get_cpu():
    return psutil.cpu_percent(interval=None)

def get_ram():
    mem = psutil.virtual_memory()
    return mem.percent

def get_processes():
    processes = []

    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return processes
