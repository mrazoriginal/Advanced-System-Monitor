def analyze(history, processes):
    cpu_avg = sum(history["cpu"]) / len(history["cpu"])
    cpu_max = max(history["cpu"])

    ram_avg = sum(history["ram"]) / len(history["ram"])
    ram_max = max(history["ram"])

    top_cpu = sorted(processes, key=lambda x: x.get("cpu_percent", 0), reverse=True)[:5]
    top_mem = sorted(processes, key=lambda x: x.get("memory_percent", 0), reverse=True)[:5]

    return {
        "cpu_avg": cpu_avg,
        "cpu_max": cpu_max,
        "ram_avg": ram_avg,
        "ram_max": ram_max,
        "top_cpu": top_cpu,
        "top_mem": top_mem
    }
