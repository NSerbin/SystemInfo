# SystemInfo

## Inspiration
While exploring system information collection in Python, I came across an article by Abdou Rockikz that demonstrated how to gather system details using Python. I found it useful and decided to enhance and tailor the script for my own needs.

## Features
- Get System Information (OS, Hostname, Machine Type)
- Get CPU Information (Cores, Frequency, Usage)
- Get Disk Information (Disk Usage, Partitions)
- Get Memory Information (RAM and Swap Usage)
- Get Local and Public IP (Local network and public-facing IP)
- Clean and user-friendly menu for easy navigation.

## How to Use

1. Clone or download the repository.

2. Open a terminal/command prompt and navigate to the directory containing SystemInfo.py.

3. Run the script with Python:

```
python SystemInfo.py
```

4. Follow the interactive menu to get your desired information:

- Press 1 to get System Information.

- Press 2 to get CPU Information.

- Press 3 to get Disk Information.

- Press 4 to get Memory Information.

- Press 5 to get Local and Public IP.

- Press 6 to Exit the script.

### Example Output
When you choose Option 5 (Local and Public IP):
```
========================================
          Local and Public IP           
========================================
HOSTNAME  : MyPC
Local IP  : 192.168.0.105
Public IP : 203.0.113.45
```

## Requirements
- Python 3.x

- The following Python libraries:
    - psutil
    - requests

You can install the required libraries using pip:
```
pip install psutil requests
```

