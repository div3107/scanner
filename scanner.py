import subprocess
import os
import pyfiglet
from termcolor import colored

# Function to display the banner
def display_banner():
    banner = pyfiglet.figlet_format("Lostboy Scanner")
    print(colored(banner, "cyan"))
    print(colored("Created by Lostboy", "yellow"))
    print(colored("=" * 50, "red"))

# Function to run system commands safely
def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(colored("[!] Error executing command", "red"))

# Scanning Functions
def run_ping_scan(target):
    print(colored(f"\n[+] Pinging {target}...", "green"))
    command = f"ping -c 4 {target}" if os.name != "nt" else f"ping -n 4 {target}"
    run_command(command)

def run_nmap_port_scan(target, ports="1-65535"):
    print(colored(f"\n[+] Running Nmap Port Scan on {target}...", "green"))
    command = f"nmap -p {ports} -sV {target} -oN nmap_scan.txt"
    run_command(command)

def run_nmap_aggressive_scan(target):
    print(colored(f"\n[+] Running Nmap Aggressive Scan (-A) on {target}...", "green"))
    command = f"nmap -A {target} -oN nmap_aggressive.txt"
    run_command(command)

def run_gobuster_scan(target, wordlist="/usr/share/wordlists/dirb/common.txt"):
    print(colored(f"\n[+] Running Gobuster on {target}...", "green"))
    command = f"gobuster dir -u {target} -w {wordlist} -o gobuster_results.txt"
    run_command(command)

def run_whatweb_scan(target):
    print(colored(f"\n[+] Running WhatWeb for Web Tech Detection on {target}...", "green"))
    command = f"whatweb {target} --color=always -v -o whatweb_results.txt"
    run_command(command)

def run_theharvester(target):
    print(colored(f"\n[+] Running theHarvester for OSINT on {target}...", "green"))
    command = f"theHarvester -d {target} -l 500 -b google -f theharvester_results.txt"
    run_command(command)

def run_wfuzz(target):
    print(colored(f"\n[+] Running WFuzz for Fuzzing on {target}...", "green"))
    command = f"wfuzz -c -z file,/usr/share/wordlists/dirb/common.txt --hc 404 {target}/FUZZ"
    run_command(command)

def run_searchsploit(target):
    print(colored(f"\n[+] Searching Exploit DB for {target}...", "green"))
    command = f"searchsploit {target}"
    run_command(command)

def run_auto_recon(target):
    print(colored("\n[+] Running Automated Recon on target...", "green"))
    run_ping_scan(target)
    run_nmap_port_scan(target)
    run_nmap_aggressive_scan(target)
    run_whatweb_scan(target)
    run_theharvester(target)
    run_gobuster_scan(target)
    print(colored("\n[✔] Automated Recon Completed! Check output files.", "yellow"))

# Main interactive menu
def main():
    display_banner()
    target = input(colored("[?] Enter target IP or domain: ", "cyan")).strip()

    while True:
        print(colored("\nChoose a scanning option:", "magenta"))
        print(colored("1️⃣  Ping Scan", "yellow"))
        print(colored("2️⃣  Nmap Port Scan", "yellow"))
        print(colored("3️⃣  Nmap Aggressive Scan (-A)", "yellow"))
        print(colored("4️⃣  Gobuster Directory Brute-Force", "yellow"))
        print(colored("5️⃣  WhatWeb (Tech Detection)", "yellow"))
        print(colored("6️⃣  TheHarvester (OSINT)", "yellow"))
        print(colored("7️⃣  WFuzz (Fuzzing)", "yellow"))
        print(colored("8️⃣  SearchSploit (Exploit DB)", "yellow"))
        print(colored("9️⃣  Automated Recon Mode", "yellow"))
        print(colored("🔟  Exit", "red"))

        choice = input(colored("\n[?] Enter your choice (1-10): ", "cyan")).strip()

        if choice == "1":
            run_ping_scan(target)
        elif choice == "2":
            ports = input(colored("[?] Enter port range (default: 1-65535): ", "cyan")).strip() or "1-65535"
            run_nmap_port_scan(target, ports)
        elif choice == "3":
            run_nmap_aggressive_scan(target)
        elif choice == "4":
            wordlist = input(colored("[?] Enter wordlist path (default: /usr/share/wordlists/dirb/common.txt): ", "cyan")).strip() or "/usr/share/wordlists/dirb/common.txt"
            run_gobuster_scan(target, wordlist)
        elif choice == "5":
            run_whatweb_scan(target)
        elif choice == "6":
            run_theharvester(target)
        elif choice == "7":
            run_wfuzz(target)
        elif choice == "8":
            run_searchsploit(target)
        elif choice == "9":
            run_auto_recon(target)
        elif choice == "10":
            print(colored("\n👋 Exiting... Stay Secure! 🔒", "red"))
            break
        else:
            print(colored("\n⚠️ Invalid choice! Please select a valid option.", "red"))

if __name__ == "__main__":
    main()

