Daily Expense Tracker & Automation Pipeline

A full-stack Python project that simplifies daily expense tracking and automates report generation.

📌 Project Overview

This project includes a Flask-based web application for entering expenses and a backend automation system that generates daily reports and backups. It demonstrates real-world backend development using database integration and scheduled automation.

🛠️ Tech Stack

Backend: Python, Flask

Database: MySQL

Automation: Python (os, shutil, csv)

Scheduling: Windows Task Scheduler

📂 Project Structure

app.py – Flask app for handling user input and storing data in MySQL

backup_job.py – Automation script for report generation and backups

requirements.txt – Project dependencies

/main – Stores daily generated CSV files

/backup – Stores archived reports and summaries

⚙️ How It Works

User Input: Expenses are entered through a Flask web form.

Database Storage: Data is stored in a MySQL database.

Daily CSV Export: The app generates a CSV file for the current day.

Automation Script: A scheduled Python script:

Reads the daily CSV

Calculates total items and total expense

Creates a summary report

Archives data into a date-wise backup folder

🚀 Key Features

Daily expense tracking with web UI

MySQL database integration

Automated CSV generation

Scheduled backup and summarization

Real-world automation workflow
