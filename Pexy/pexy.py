import socket
from concurrent.futures import ThreadPoolExecutor
import datetime
import argparse

parser = argparse.ArgumentParser(description="Simple port scanner made by Exyth ;p")
parser.add_argument("-t", "--target", help="Set the target.", required=True)
parser.add_argument("-p1", "--startport", default=1, help="Set the port to start with.", type=int)
parser.add_argument("-p2", "--endport", default=65535, help="Set the last port to scan.", type=int)
parser.add_argument("-p", "--sports", help="Set specific ports to scan (comma separated)", type=str)
parser.add_argument("-tm", "--timeout", default=1, help="Set the timeout duration.", type=float)
parser.add_argument("-th", "--threads", help="Set max threads.", default=100, type=int)
parser.add_argument("-sp", "--showports", help="Show all ports being scanned (even closed).", action="store_true")
parser.add_argument("-os", "--osdetection", help="Turn on service name resolution.", action="store_true")

args = parser.parse_args()

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(args.timeout)
    try:
        result = s.connect_ex((args.target, port))
        if result == 0:
            service = "unknown"
            if args.osdetection:
                try:
                    service = socket.getservbyport(port)
                except OSError:
                    pass
            print(f'\n[OPEN] Port {port} (Service: {service}) is open!\n')
            with open('available_ports.txt', 'a') as avports:
                avports.write(f'Port {port} is open - Service: {service}\n')
        elif args.showports:
            print(f'[CLOSED] Port {port} is closed')
    finally:
        s.close()

if args.sports:
    try:
        portslist = [int(port.strip()) for port in args.sports.split(',')]
    except ValueError:
        print("Error: Ports must be integers.")
        exit(1)
else:
    portslist = list(range(args.startport, args.endport + 1))

start_time = datetime.datetime.now()

with ThreadPoolExecutor(max_workers=args.threads) as exec:
    exec.map(scan, portslist)

end_time = datetime.datetime.now()
duration = (end_time - start_time).total_seconds()

print("\nScan completed.")
print(f"Duration: {duration:.2f} seconds")
