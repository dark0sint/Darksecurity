import subprocess
import time
import sys

def start_bro():
    print("[*] Starting Bro (Zeek) IDS...")
    try:
        subprocess.run(["sudo", "broctl", "start"], check=True)
        print("[*] Bro started successfully.")
    except subprocess.CalledProcessError:
        print("[!] Failed to start Bro.")
        sys.exit(1)

def start_logstash():
    print("[*] Starting Logstash...")
    try:
        subprocess.run(["sudo", "systemctl", "start", "logstash"], check=True)
        print("[*] Logstash started successfully.")
    except subprocess.CalledProcessError:
        print("[!] Failed to start Logstash.")
        sys.exit(1)

def start_elasticsearch():
    print("[*] Starting Elasticsearch...")
    try:
        subprocess.run(["sudo", "systemctl", "start", "elasticsearch"], check=True)
        print("[*] Elasticsearch started successfully.")
    except subprocess.CalledProcessError:
        print("[!] Failed to start Elasticsearch.")
        sys.exit(1)

def start_kibana():
    print("[*] Starting Kibana...")
    try:
        subprocess.run(["sudo", "systemctl", "start", "kibana"], check=True)
        print("[*] Kibana started successfully.")
    except subprocess.CalledProcessError:
        print("[!] Failed to start Kibana.")
        sys.exit(1)

def main():
    print("Starting DarkSecurity Monitoring Stack...")
    start_elasticsearch()
    time.sleep(5)  # Tunggu elasticsearch siap
    start_logstash()
    start_bro()
    start_kibana()
    print("[*] DarkSecurity stack is up and running.")

if __name__ == "__main__":
    main()
