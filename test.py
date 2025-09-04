import os
import csv

source = os.path.expanduser("~/Downloads")
destination = os.path.expanduser("~/Organized_Files_AI")
os.makedirs(destination, exist_ok=True)

# Get all filenames
filenames = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
print(filenames)

# Save to CSV
csv_file = os.path.join(destination, "filenames.csv")
with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Filename"])  # header
    for file in filenames:
        writer.writerow([file])

print(f"Saved {len(filenames)} filenames to {csv_file}")
