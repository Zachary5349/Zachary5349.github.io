import socket
import time
import subprocess
import psutil
import os

# Threshold of the connections to your computer
connection_threshold = 292
# The program runs once per second
sleep_interval = 120
# Threshold of the CPU usage (Percentage)
cpu_threshold = 31.6
# Threshold of the memory usage (Percentage)
memory_threshold = 85.7
# Threshold of the disk usage (Percentage)
disk_threshold = 74.7

suspicious_processes = ['nc', 'netcat', 'telnet']

def get_connections():
    # Use the netstat command to get the number of connections
    netstat_output = subprocess.check_output(['netstat', '-an'])        

    connections = netstat_output.decode('utf-8').split('\n')

    return len(connections)

def get_cpu_usage():
    # Use the psutil library to get the current CPU usage
    return psutil.cpu_percent()

def get_memory_usage():
    # Use the psutil library to get the current memory usage
    return psutil.virtual_memory().percent

def get_disk_usage():
    # Use the psutil library to get the current disk usage
    return psutil.disk_usage('/').percent

def detect_suspicious_processes():
    # Use the psutil library to get a list of running processes
    processes = [p.info for p in psutil.process_iter(['pid', 'name'])]

    for process in processes:

        if process['name'] in suspicious_processes:

            print(f"Suspicious process detected: {process['name']}")
        

def detect_ddos():
    # Get the current number of connections
    current_connections = get_connections()

    # Check if the number of connections exceeds the threshold
    if current_connections > connection_threshold:

        print(f"Potential DDoS attack detected! Connections Threshold is at {current_connections}")
    else:

         print(f"Connections seem normal.")
     

    # Check if CPU usage exceeds the threshold
    cpu_usage = get_cpu_usage()

    if cpu_usage > cpu_threshold:

        print(f"High CPU usage detected! CPU usage percentage is at {cpu_usage}")

    else:

        print(f"Connections seem normal.")
    # Check if memory usage exceeds the threshold
    memory_usage = get_memory_usage()

    if memory_usage > memory_threshold:

        print(f"High memory usage detected! CPU usage percentage is at {memory_usage}")
    else:

        print(f"Memory usage seem normal.")
    # Check if disk usage exceeds the threshold
    disk_usage = get_disk_usage()

    if disk_usage > disk_threshold:

        print(f"High disk usage detected! CPU usage percentage is at {disk_usage}")

    else:

        print(f"Disk usage seem normal.")

    print("")
    print("waiting 20 seconds to gain more data!")
    # Check for suspicious processes
    detect_suspicious_processes()

while True:
    detect_ddos()
    time.sleep(sleep_interval)