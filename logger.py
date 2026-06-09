import csv

# export collected history into CSV file
def save_csv(history, filename="log.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)

        # header row
        writer.writerow(["time", "cpu", "ram", "process_count"])

        # write each snapshot row
        for i in range(len(history["time"])):
            writer.writerow([
                history["time"][i],
                history["cpu"][i],
                history["ram"][i],
                history["process_count"][i]
            ])