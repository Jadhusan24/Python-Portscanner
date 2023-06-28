import nmap

def scan_ports(target, ports):
    nm = nmap.PortScanner()
    nm.scan(target, ','.join(str(port) for port in ports))
    
    for host in nm.all_hosts():
        print(f"Scanning ports for {host}:")
        
        for port in ports:
            state = nm[host]['tcp'][port]['state']
            print(f"Port {port} is {state}")
            
# Example usage
target_ip = "127.0.0.1"  
ports_to_scan = [80, 443, 22, 8080]
scan_ports(target_ip, ports_to_scan)

