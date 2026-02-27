# 💸 Daily Expense Tracker & Automation Pipeline

A full-stack Python project that simplifies daily expense tracking and automates report generation using Flask, MySQL, and Python automation.

---

## 📌 Project Overview
This project includes a Flask-based web application for entering expenses and a backend automation system that generates daily reports and backups. It demonstrates real-world backend development using database integration and scheduled automation workflows.

---

## 🛠️ Tech Stack
- Python
- Flask
- MySQL
- Python Automation (os, shutil, csv)
- Windows Task Scheduler
- Git & GitHub

---

## ✨ Key Features
- Simple web UI for daily expense entry  
- MySQL database integration  
- Automatic daily CSV generation  
- Scheduled backup and summarization  
- Folder-based archival system  

---

## 📂 Project Structure
- app.py # Flask web application
- backup_job.py # Automation script
- requirements.txt # Dependencies
- main/ # Daily CSV files
- backup/ # Archived reports

---

## ⚙️ How It Works
1. User enters expense through Flask UI  
2. Data stored in MySQL database  
3. Daily CSV generated automatically  
4. Scheduled script:
   - Reads CSV  
   - Calculates totals  
   - Creates summary  
   - Moves files to backup folder  

---

## 🚀 Run Locally

### Install dependencies
```bash
pip install -r requirements.txt

  
