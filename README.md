Key-Loger

Key-Loger is a Python-based cybersecurity learning project that demonstrates how keystroke logging works at a technical level.
⚠️ Important: This project is intended only for educational and research purposes. Keyloggers can be misused for malicious activity — please use responsibly in controlled environments.

Features

- Keystroke Capture: Logs user input from the keyboard.
- 
- File Storage: Saves captured keystrokes to a local file.
- 
- Lightweight Implementation: Simple Python script using standard libraries.
- 
- Cybersecurity Focus: Helps students understand how attackers might exploit input logging, and how defenders can detect/prevent it.

Tech Stack

Language:Python 3

Libraries:pynput (keyboard listener)

Output:Text file logs

Getting Started

Prerequisites

- Python 3.8+
  
- Install required library:

    pip install pynput


Installation

- Clone the repository
  
git clone https://github.com/GodANDDevil/Key-Loger.git

cd Key-Loger

- Run the script
  
python keylogger.py

- Check the log file
  
- Keystrokes will be saved in a .txt file (e.g., log.txt).
  

📂 Project Structure

Key-Loger/

│── keylogger.py     # Main script

│── log.txt          # Output file (generated after running)



🔒 Ethical Use
This project is for:
- Cybersecurity students learning about malware techniques.
  
- Researchers studying detection and prevention methods.
  
- Educators demonstrating risks of insecure systems.
  
Do not use this project for unauthorized monitoring. Misuse may be illegal and unethical.

💡 Future Improvements

- Add encryption for log files.
  
- Implement real-time alerts for suspicious activity.
  
- Explore defensive countermeasures (e.g., detecting keyloggers).
  
- Build a GUI dashboard for monitoring.

