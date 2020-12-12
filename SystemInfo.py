#Credits to "Abdou Rockikz" I only edit for what i want/need
import socket as s
from requests import get
import platform
import psutil

def menu():
    print("="*40)
    print("Welcome to System Information Script 1.0")
    print("="*40)
    print("Please Choose an Option:")
    print("="*40)
    print("[*] 1. Get System Information.")
    print("="*40)
    print("[*] 2. Get CPU Information.")
    print("="*40)
    print("[*] 3. Get Disk Information.")
    print("="*40)
    print("[*] 4. Get Memory Information.")
    print("="*40)
    print("[*] 5. Get Local and Public IP")
    print("="*40)
    print("[*] 6. Exit")
    print("="*40)
    option = int(input(""))
    if option == 1:
        sys_info()
    elif option == 2:
        cpu_info()
    elif option == 3:
        disk_info()
    elif option == 4:
        mem_info()       
    elif option == 5:
        ip_adress()
    elif option == 6:
        exit()
    else:
        raise ValueError("Please Choose option between 1-3.")

def size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def sys_info():
    print("="*17, "System Information", "="*17)
    uname = platform.uname()
    print(f"System Platform: {uname.system}")
    print(f"Hostname: {uname.node}")
    print(f"O.S. Release: {uname.release}")
    print(f"O.S. Version: {uname.version}")
    print(f"Machine Type: {uname.machine}")
    print("="*54)

def cpu_info():
    print("="*10, "CPU Info", "="*10)
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f} Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f} Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f} Mhz")
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i+1}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")
    print("="*30)

def disk_info():
    print("="*40, "Disk Information", "="*40)
    print("Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  Mount options: {partition.opts}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        print(f"  Used: {size(partition_usage.used)} | {partition_usage.percent}%")
        print(f"  Free: {size(partition_usage.free)}")
        print(f"  Total Size: {size(partition_usage.total)}")

def mem_info():
    # get the memory details
    print("="*3, "Memory Information", "="*3)
    svmem = psutil.virtual_memory()
    print(f"Used: {size(svmem.used)} = {svmem.percent}%")
    print(f"Available: {size(svmem.available)}")
    print(f"Total: {size(svmem.total)}")
    # get the swap memory details (if exists)
    print("="*10, "SWAP", "="*10)
    swap = psutil.swap_memory()
    print(f"Used: {size(swap.used)} = {swap.percent}%")
    print(f"Available: {size(swap.free)}")
    print(f"Total: {size(swap.total)}")

def ip_adress():
    print("="*40, "Local and Public IP", "="*40) 
    hostname = s.gethostname()
    local_ip = s.gethostbyname(hostname)
    public_ip = get('https://api.ipify.org').text
    print(f"HOSTNAME: {hostname} ")
    print(f"Local IP: {local_ip}")
    print(f"Public IP: {public_ip}")
    
if __name__ == "__main__":
    menu()
