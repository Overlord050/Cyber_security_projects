import socket
import threading

def scan_port(target, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        if s.connect_ex((target, port)) == 0:
            print(f"[+] Port {port} is OPEN")

target = "politieenwetenschap.nl"
ports = range(1, 10000)  ## Scan10000 ports

## threading because otherwise it's slow as heck
threads = []
for port in ports:
    thread = threading.Thread(target=scan_port, args=(target, port))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
