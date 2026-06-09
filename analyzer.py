# analyzes system history and process stats

def analyze(history, processes):
    # handle empty dataset case
    if not history["cpu"]:
        return {
            "cpu_avg": 0,
            "cpu_max": 0,
            "ram_avg": 0,
            "ram_max": 0,
            "top_cpu": [],
            "top_mem": []
        }

    # CPU statistics
    cpu_avg = sum(history["cpu"]) / len(history["cpu"])
    cpu_max = max(history["cpu"])

    # RAM statistics
    ram_avg = sum(history["ram"]) / len(history["ram"])
    ram_max = max(history["ram"])

    # top processes by CPU usage
    top_cpu = sorted(processes, key=lambda x: x.get("cpu_percent", 0), reverse=True)[:5]

    # top processes by memory usage
    top_mem = sorted(processes, key=lambda x: x.get("memory_percent", 0), reverse=True)[:5]

    return {
        "cpu_avg": cpu_avg,
        "cpu_max": cpu_max,
        "ram_avg": ram_avg,
        "ram_max": ram_max,
        "top_cpu": top_cpu,
        "top_mem": top_mem
    }