import socket
import threading

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        s.settimeout(2)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        s.close()
    
    except socket.error as e:
        print(f"Error: {str(e)}")

def main():
    try:
        host = input("Enter the host to scan: ")
        
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
        
        print(f"Scanning host {host} from port {start_port} to port {end_port}...")
        
        threads = []
        
        for port in range(start_port, end_port + 1):
            t = threading.Thread(target=scan_port, args=(host, port))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
    
    except KeyboardInterrupt:
        print("\nExiting the port scanner.")
    except ValueError:
        print("Invalid port number entered. Please enter a valid port number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
