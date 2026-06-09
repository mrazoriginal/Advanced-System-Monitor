import time

from collector import get_cpu, get_ram, get_processes
from history import history, add_snapshot
from analyzer import analyze
from visualizer import plot
from logger import save_csv
from config import INTERVAL

# Main monitoring loop entry point

def main():
    start = time.time()  # track runtime start
    processes = []

    try:
        while True:
            # collect system metrics
            cpu = get_cpu()
            ram = get_ram()
            processes = get_processes()

            # store snapshot in history
            add_snapshot(
                time.time() - start,
                cpu,
                ram,
                len(processes)
            )

            # live console output
            print(f"CPU: {cpu}% | RAM: {ram}% | Processes: {len(processes)}")

            # wait before next sample
            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        # graceful shutdown + reporting
        print("\nStopping... generating report...\n")

        result = analyze(history, processes)

        print("\n=== FINAL REPORT ===")
        for k, v in result.items():
            print(k, ":", v)

        # export data
        save_csv(history)
        plot(history)

if __name__ == "__main__":
    main()