# Daily Expense Tracker & Automation Pipeline

A Full-Stack Python application designed to streamline daily expense logging and automate financial reporting. 

## 📌 Project Overview
This project consists of a **Flask-based web interface** for data entry and an **automated backend pipeline** that processes, summarizes, and archives data daily. It replaces manual bookkeeping with a structured, reliable digital system.

## 🛠️ Tech Stack
* **Backend:** Python 3.x, Flask
* **Database:** MySQL
* **Automation:** Python (OS, Shutil, CSV libraries)
* **OS Integration:** Windows Task Scheduler

## 📂 Project Structure
* `app.py` - The core Flask application handling web requests and MySQL database operations.
* `backup_job.py` - The automation script that performs ETL (Extract, Transform, Load) tasks.
* `requirements.txt` - File containing all external dependencies for easy environment setup.
* `/main` - Directory for active daily logs.
* `/backup` - Directory for date-wise archived summaries and CSVs.

## ⚙️ How It Works
1. **Data Entry:** The user enters the item name and amount via the Flask web UI.
2. **Persistence:** Data is saved into a MySQL database for real-time access.
3. **Daily Export:** The system generates a CSV file from the database.
4. **Automation Pipeline:** The `backup_job.py` script runs automatically (via Task Scheduler) to:
    - Read the day's CSV.
    - Calculate total items and total expenditure.
    - Generate a `summary.csv`.
    - Archive all files into a date-stamped folder and clear the active directory.

## 🚀 Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
