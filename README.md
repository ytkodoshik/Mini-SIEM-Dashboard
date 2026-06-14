## Mini SIEM & SOC Dashboard

##  Overview
A lightweight Security Information and Event Management (SIEM) system built with Python and FastAPI. This project simulates a Security Operations Center (SOC) environment by generating mock network traffic, storing logs in a local SQLite database, analyzing them in real-time for Brute-Force attacks, and visualizing the data on an interactive dashboard.

##  Features
- **Log Ingestion API:** RESTful API built with FastAPI to receive and normalize security events.
- **Traffic Simulator:** Python script that continuously generates realistic network logs (e.g., failed logins, malware detection, port scans).
- **Real-time Correlation Engine:** Background analyzer that detects Brute-Force attacks (e.g., 3+ failed logins from the same IP) and triggers critical alerts in the terminal.
- **Interactive Dashboard:** Frontend interface using Chart.js to visualize incident severity and display recent logs dynamically.

##  Tech Stack
- **Backend:** Python, FastAPI, Uvicorn, SQLAlchemy
- **Database:** SQLite
- **Frontend:** HTML, Vanilla JavaScript, Chart.js
- **Tools:** Git, REST APIs

##  How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/YourUsername/Mini-SIEM-Dashboard.git](https://github.com/YourUsername/Mini-SIEM-Dashboard.git)
cd Mini-SIEM-Dashboard
```

### 2. Set up Virtual Environment & Install Dependencies
```bash
python -m venv venv

# For Windows:
venv\Scripts\activate

# For Linux/Mac:
# source venv/bin/activate

pip install -r requirements.txt
```

### 3. Start the SOC Environment (Requires 3 Terminals)

**Terminal 1: Start the API Server**
```bash
uvicorn main:app --reload
```

**Terminal 2: Start the Log Generator**
```bash
python log_generator.py
```

**Terminal 3: Start the Correlation Engine**
```bash
python analyzer.py
```

### 4. View the Dashboard
Simply open the `dashboard.html` file in your web browser to see the live data populating the charts and tables!

## 📸 Screenshots

<img width="1191" height="1283" alt="Zrzut ekranu 2026-06-14 101530" src="https://github.com/user-attachments/assets/f349a6e8-dd76-4e9e-8ca2-3606b0ad03b4" />
