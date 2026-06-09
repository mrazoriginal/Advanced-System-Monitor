import csv

def save_csv(history, filename="log.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time", "cpu", "ram", "process_count"])

        for i in range(len(history["time"])):
            writer.writerow([
                history["time"][i],
                history["cpu"][i],
                history["ram"][i],
                history["process_count"][i]
            ])
