import requests
import time
import random

API_URL = "http://127.0.0.1:8000/logs/"

ips = ["192.168.1.10", "192.168.1.15", "10.0.0.5", "172.16.0.50", "8.8.8.8"]
event_types = ["failed_login", "port_scan", "malware_detected", "successful_login", "firewall_block"]
severities = ["low", "medium", "high", "critical"]
messages = [
    "Zablokowano próbę skanowania portów na zaporze zewnętrznej.",
    "Błędne hasło dla użytkownika administrator (możliwy brute-force).",
    "Wykryto ruch sieciowy do znanego serwera Command & Control (C2).",
    "Pomyślne logowanie do sieci firmowej przez VPN.",
    "System antywirusowy zablokował pobieranie podejrzanego pliku .exe."
]

print("🛡️ Rozpoczynam symulację ruchu sieciowego SOC...")
print("Wciśnij Ctrl+C w tym terminalu, aby zatrzymać symulację.\n")

while True:
    log_data = {
        "source_ip": random.choice(ips),
        "severity": random.choice(severities),
        "event_type": random.choice(event_types),
        "message": random.choice(messages)
    }

    try:
        response = requests.post(API_URL, json=log_data)
        print(f"[+] Wysłano: {log_data['event_type']} (Priorytet: {log_data['severity']}) -> Status API: {response.status_code}")
        
    except requests.exceptions.ConnectionError:
        print("[-] Błąd połączenia z API. Czy uvicorn (serwer FastAPI) na pewno jest włączony?")

    time.sleep(random.randint(1, 4))