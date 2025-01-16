# CODTECH-ADV-TASK3
# Penetration Testing Toolkit
# Personal information

* Name : Patel Mihir

* Company : CODTECH IT SOLUTIONS PVT.LTD

* ID : CT08DAB

* Domain : Cyber Security & Ethical Hacking

* Duration: 20th Dec 2024 To 20th Jan 2025

* Mentor : Neela Santhosh kumar

# Overview
This repository contains a Penetration Testing Toolkit that includes essential modules for network security testing, such as port scanning, SSH brute-forcing, and DNS lookups. The toolkit is designed for educational purposes and to assist security professionals and researchers in understanding the basics of penetration testing techniques.


# Features
- Port Scanner:
        Scans well-known ports (e.g., SSH, HTTP, HTTPS, FTP) on a given target (IP or URL) to identify open ports.

- SSH Brute-Forcer:
        Attempts to brute-force an SSH login using either a single password or a password wordlist. This module leverages the powerful Paramiko library to perform SSH authentication attempts.

- DNS Lookup:
        Resolves a given IP address to a domain name (PTR record) by performing a reverse DNS lookup.

- Multithreading Support:
        The toolkit leverages Python’s threading to ensure that the operations (port scanning, SSH brute-forcing, and DNS lookup) are performed concurrently, improving the user experience.

- Color-Coded Output:
        The toolkit uses the colorama library to provide color-coded outputs for various messages (success, failure, informational, etc.), making it easy to identify the results.

- ASCII Art:
        The toolkit displays the title of the tool using ASCII art for a more engaging user interface.


 # Requirements

To run this toolkit, ensure that you have the following Python libraries installed:

- socket: This library is built into Python and is used for network connections.
- paramiko: For SSH brute-forcing via the SSH protocol.
- pyfiglet: Used for displaying ASCII art text.
- colorama: For colored output in the terminal.


# Installation

To install the required dependencies, you can use pip to install them:

    pip install paramiko pyfiglet colorama


# Steps to Run
- Clone the Repository

First, clone the repository to your local machine:

    git clone https://github.com/mdpatel1335/CODTECH-ADV-TASK3.git
    cd CODTECH-ADV-TASK3

- Run the Toolkit

After ensuring that the required libraries are installed, you can run the toolkit by executing the following command:

    python task3.py

This will launch the penetration testing toolkit, displaying the main menu with the following options:

- Port Scanner: You can input an IP address or domain, and the script will check well-known ports for availability.
- SSH Brute-Forcer: You can attempt to brute-force an SSH login using a username and either a single password or a wordlist of passwords.
- DNS Lookup: Input an IP address, and the script will attempt a reverse DNS lookup to find the associated domain name.
- Exit: Exit the program.

# Example:

- Port Scanner:
    - Enter the IP/URL you want to scan.
    - The script will display which well-known ports are open on the target.

- SSH Brute-Forcer:
    - Enter the target IP/URL and the SSH username.
    - Provide either a single password or the path to a wordlist.
    - The script will attempt SSH logins using the provided credentials.

- DNS Lookup:
    - Enter the IP address, and the script will attempt to resolve it to a domain name.

  # Notes

   - Ethical Usage: This toolkit should only be used on systems that you own or have explicit permission to test. Unauthorized access to systems is illegal and unethical.
   - Performance Considerations: The SSH brute-forcing module may take some time, especially if using a large wordlist.
   - Compatibility: This script should work on any system with Python 3.x installed.
 
# Screenshots:
![Screenshot From 2025-01-16 16-25-54](https://github.com/user-attachments/assets/3fb56f14-c626-4a8a-b704-1cd165afae46)

![Screenshot From 2025-01-16 16-26-36](https://github.com/user-attachments/assets/aaaa10d9-9b93-43b1-8ae3-2949683774b9)

![Screenshot From 2025-01-16 16-26-55](https://github.com/user-attachments/assets/8b121f11-0410-4fd4-a8f8-c75a0494f89f)

![Screenshot From 2025-01-16 16-27-25](https://github.com/user-attachments/assets/356c92ee-a8d9-448e-b436-a1082db38abd)


# Author 

MIHIR PATEL
