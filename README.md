# Lostboy Security Scanner

## 🔥 Overview
**Lostboy Security Scanner** is an interactive Python-based reconnaissance and enumeration tool designed for penetration testers and cybersecurity enthusiasts. It provides multiple scanning options, such as port scanning, directory brute-forcing, OSINT gathering, and automated recon, making it ideal for solving **CTFs, TryHackMe rooms, HackTheBox challenges, and real-world penetration tests**.

## 🎯 Features
- 🔹 **Interactive CLI Menu** – Choose from multiple scanning options
- 🔹 **Ping Scan** – Check if a target is alive
- 🔹 **Nmap Port Scan** – Scan for open ports and services
- 🔹 **Nmap Aggressive Scan (-A)** – Perform an in-depth scan
- 🔹 **Gobuster Directory Brute-Force** – Enumerate hidden directories and files
- 🔹 **WhatWeb Scan** – Detect web technologies
- 🔹 **TheHarvester OSINT** – Gather emails, domains, and other OSINT data
- 🔹 **WFuzz Fuzzing** – Perform web fuzzing attacks
- 🔹 **SearchSploit Integration** – Find exploits related to target services
- 🔹 **Automated Recon Mode** – Run all major scans with one command
- 🔹 **Colored Output & Logging** – Easy-to-read terminal output with saved reports

---

## 🛠 Installation & Setup
### **1️⃣ Install Dependencies**
Ensure you have **Python 3** and the required tools installed:
```bash
sudo apt update && sudo apt install nmap gobuster whatweb theharvester wfuzz exploitdb figlet
pip install termcolor pyfiglet
```

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/lostboy-scanner.git
cd lostboy-scanner
```

### **3️⃣ Run the Script**
```bash
python3 myscript.py
```

---

## 🚀 Usage
Upon running the script, you will be presented with an interactive menu:
```bash
[?] Enter target IP or domain: example.com
```
Then, choose an option:
```
1️⃣  Ping Scan
2️⃣  Nmap Port Scan
3️⃣  Nmap Aggressive Scan (-A)
4️⃣  Gobuster Directory Brute-Force
5️⃣  WhatWeb (Tech Detection)
6️⃣  TheHarvester (OSINT)
7️⃣  WFuzz (Fuzzing)
8️⃣  SearchSploit (Exploit DB)
9️⃣  Automated Recon Mode
🔟  Exit
```

### **Examples**
#### ➤ **Basic Ping Scan**
```bash
[?] Enter target IP or domain: 192.168.1.1
[+] Pinging 192.168.1.1...
```

#### ➤ **Nmap Port Scan with Custom Port Range**
```bash
[?] Enter port range (default: 1-65535): 80,443
[+] Running Nmap Port Scan on 192.168.1.1...
```

#### ➤ **Automated Recon Mode**
```bash
[+] Running all major scans on target: example.com
✔️ Ping Scan ✔️ Port Scan ✔️ OSINT ✔️ Directory Brute-Force
```


## 🤝 Contributing
Want to add new features or improve the tool? Feel free to contribute:
1. **Fork the repository**
2. **Create a new branch** (`feature/new-feature`)
3. **Commit your changes**
4. **Push the changes** and submit a **pull request**

---

## ⚠️ Disclaimer
This tool is intended for educational and ethical purposes only. Do not use it without explicit permission. The author is not responsible for any misuse.

---

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🔗 Connect with Me
💻 **GitHub:** [github.com/yourusername](https://github.com/div3107)   
📧 **Email:** geek.divyanshu@gmail.com  

🔒 **Stay secure and happy hacking!** 🚀

