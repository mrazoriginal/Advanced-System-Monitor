import time

from collector import get_cpu, get_ram, get_processes
from history import history, add_snapshot
from analyzer import analyze
from visualizer import plot
from logger import save_csv
from config import INTERVAL

def main():
    start = time.time()
    processes = []

    try:
        while True:
            cpu = get_cpu()
            ram = get_ram()
            processes = get_processes()

            add_snapshot(
                time.time() - start,
                cpu,
                ram,
                len(processes)
            )

            print(f"CPU: {cpu}% | RAM: {ram}% | Processes: {len(processes)}")

            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print("\nStopping... generating report...\n")

        result = analyze(history, processes)

        print("\n=== FINAL REPORT ===")
        for k, v in result.items():
            print(k, ":", v)

        save_csv(history)
        plot(history)

if __name__ == "__main__":
    main()
