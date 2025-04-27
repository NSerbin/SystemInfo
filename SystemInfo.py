import socket
from requests import get
import platform
import psutil
import sys

def print_header(title):
    print("=" * 40)
    print(f"{title.center(40)}")
    print("=" * 40)

def menu():
    print_header("System Information Script 1.0")
    print("Please Choose an Option:")
    print("[1] Get System Information")
    print("[2] Get CPU Information")
    print("[3] Get Disk Information")
    print("[4] Get Memory Information")
    print("[5] Get Local and Public IP")
    print("[6] Exit")
    
    try:
        choice = int(input("\nEnter your choice: "))
        options = {
            1: get_system_info,
            2: get_cpu_info,
            3: get_disk_info,
            4: get_memory_info,
            5: get_ip_info,
            6: exit_program
        }
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid option, please choose between 1-6.")
    except ValueError:
        print("Please enter a valid number.")

def convert_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_system_info():
    print_header("System Information")
    uname = platform.uname()
    print(f"System Platform : {uname.system}")
    print(f"Hostname        : {uname.node}")
    print(f"O.S. Release    : {uname.release}")
    print(f"O.S. Version    : {uname.version}")
    print(f"Machine Type    : {uname.machine}")

def get_cpu_info():
    print_header("CPU Information")
    print(f"Physical cores  : {psutil.cpu_count(logical=False)}")
    print(f"Total cores     : {psutil.cpu_count(logical=True)}")
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency   : {cpufreq.max:.2f} MHz")
    print(f"Min Frequency   : {cpufreq.min:.2f} MHz")
    print(f"Current Frequency: {cpufreq.current:.2f} MHz")
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"  Core {i+1}: {percentage}%")
    print(f"Total CPU Usage : {psutil.cpu_percent()}%")

def get_disk_info():
    print_header("Disk Information")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint    : {partition.mountpoint}")
        print(f"  File System   : {partition.fstype}")
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"  Used          : {convert_size(usage.used)} ({usage.percent}%)")
            print(f"  Free          : {convert_size(usage.free)}")
            print(f"  Total Size    : {convert_size(usage.total)}\n")
        except PermissionError:
            continue

def get_memory_info():
    print_header("Memory Information")
    mem = psutil.virtual_memory()
    print(f"Used Memory     : {convert_size(mem.used)} ({mem.percent}%)")
    print(f"Available Memory: {convert_size(mem.available)}")
    print(f"Total Memory    : {convert_size(mem.total)}")

    print_header("Swap Memory")
    swap = psutil.swap_memory()
    print(f"Used Swap       : {convert_size(swap.used)} ({swap.percent}%)")
    print(f"Available Swap  : {convert_size(swap.free)}")
    print(f"Total Swap      : {convert_size(swap.total)}")

def get_ip_info():
    print_header("Local and Public IP")
    hostname = socket.gethostname()

    # Get local IP
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
    except Exception:
        local_ip = "Unable to get Local IP"
    
    # Get public IP from multiple services
    public_ip = None
    services = [
        "https://api.ipify.org",
        "https://ifconfig.me/ip",
        "https://ident.me",
        "https://ipecho.net/plain",
    ]
    
    for service in services:
        try:
            response = get(service, timeout=5)
            if response.status_code == 200:
                public_ip = response.text.strip()
                break
        except Exception:
            continue
    
    if not public_ip:
        public_ip = "Unable to fetch Public IP"

    print(f"HOSTNAME  : {hostname}")
    print(f"Local IP  : {local_ip}")
    print(f"Public IP : {public_ip}")


def exit_program():
    print("Exiting... Goodbye!")
    sys.exit()

if __name__ == "__main__":
    menu()
