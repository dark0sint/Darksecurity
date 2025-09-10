
---

### 2. `setup.py`

```python
#!/usr/bin/env python3
import os
import sys
import subprocess

def install_full():
    print("[*] Installing Full DarkSecurity Stack...")
    # Contoh instalasi paket
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "bro", "elasticsearch", "kibana", "logstash", "apache2", "python3-flask"])
    print("[*] Full installation complete.")

def install_sensor():
    print("[*] Installing Sensor Only...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "bro"])
    print("[*] Sensor installation complete.")

def install_webadmin():
    print("[*] Installing Web Admin Only...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "apache2", "python3-flask", "kibana"])
    print("[*] Web Admin installation complete.")

def main():
    print("Welcome to DarkSecurity Setup")
    print("Choose installation type:")
    print("1. Full Install")
    print("2. Sensor Install")
    print("3. Web Admin Install")
    choice = input("Enter choice (1-3): ")

    if choice == '1':
        install_full()
    elif choice == '2':
        install_sensor()
    elif choice == '3':
        install_webadmin()
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()
