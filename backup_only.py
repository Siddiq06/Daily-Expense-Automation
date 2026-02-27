import os
import shutil
from datetime import datetime

def backup_job():
    today = datetime.now().strftime("%Y-%m-%d")
    source = f"main/{today}.csv"

    if not os.path.exists(source):
        print("No file today")
        return

    total_items = 0
    total_amount = 0

    with open(source, "r") as f:
        lines = f.readlines()
    lines=lines[1:]

    for line in lines:
        try:
            parts = line.strip().split(",")
            amount = int(parts[1].strip())
            total_amount += amount
            total_items+=1
        except:
            continue

    backup_folder = f"backup/{today}"
    os.makedirs(backup_folder, exist_ok=True)

    destination = f"{backup_folder}/{today}.csv"
    shutil.copy2(source, destination)
    os.remove(source)

    with open(f"{backup_folder}/summary.csv", "w") as f:
        f.write("metric,value\n")
        f.write(f"total_items,{total_items}\n")
        f.write(f"total_amount,{total_amount}\n")

    print("Backup completed")

backup_job()
