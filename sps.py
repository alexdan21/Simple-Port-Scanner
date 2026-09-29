import pyfiglet
import sys
import socket

common_ports = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    587: "SMTP Submission",
    631: "IPP Printing",
    993: "IMAPS",
    995: "POP3S",
    1433: "Microsoft SQL Server",
    1521: "Oracle Database",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Alternate",
    8443: "HTTPS Alternate",
}

ascii_banner = pyfiglet.figlet_format("SIMPLE PORT SCANNER")
print(ascii_banner)

target = input("Target IP: ")
type_scan = int(input("Fast scan(0)/Full scan(1):")) 

print("-" * 50)
print("Scanning Target: " + target)
print("-" * 50)

if type_scan == 1:
    try:
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
        
            result = s.connect_ex((target,port))
            if result == 0:
                print("Port {} is open".format(port))

        s.close()
        
    except KeyboardInterrupt:
        print("\n Exiting Program!")
        sys.exit()
    except socket.gaierror:
        print("\n IP Could Not Be Resolved!")
        sys.exit()
    except socket.error:
        print("\n Server not responding!")
        sys.exit()

elif type_scan == 0:
    try:
        for port, service_name in common_ports.items():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
        
            result = s.connect_ex((target,port))
            if result == 0:
                print(f"Port {port} ({service_name}) is open")

        s.close()
        
    except KeyboardInterrupt:
        print("\n Exiting Program!")
        sys.exit()
    except socket.gaierror:
        print("\n IP Could Not Be Resolved!")
        sys.exit()
    except socket.error:
        print("\n Server not responding!")
        sys.exit()

else:
    print("Incorrect selection. Please try again.")