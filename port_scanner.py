import socket
from datetime import datetime
import threading
from queue import Queue
import time
import os

def port_scanner_worker(target, port_queue, completed_ports, results):
    while not port_queue.empty():
        port = port_queue.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port, 'tcp')
                except:
                    service = "Unknown"

                # Attempt to grab the banner
                banner = grab_banner(target, port)
                result_line = f"Port {port}: Open (Service: {service}, Banner: {banner})"
                print(result_line)
                with results_lock:
                    results.append(result_line)
            s.close()
        except socket.error:
            pass
        finally:
            port_queue.task_done()
            with completed_ports_lock:
                completed_ports[0] += 1

def grab_banner(target, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except:
        return "No banner"

def print_progress(total_ports, completed_ports):
    while completed_ports[0] < total_ports:
        time.sleep(10)
        with completed_ports_lock:
            percentage = (completed_ports[0] / total_ports) * 100
        print(f"Scan Progress: {percentage:.2f}%")

def save_results(results):
    save_to_file = input("Do you want to save the scan details to a file? (yes/no): ").strip().lower()
    if save_to_file == 'yes':
        file_name = input("Enter the file name (without extension): ").strip() + ".txt"
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, file_name)
        try:
            with open(file_path, 'w') as file:
                for line in results:
                    file.write(line + '\n')
            print(f"Results saved to {file_path}")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")

if __name__ == "__main__":
    target = input("Enter the target host (IP or domain): ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    num_threads = 100  # You can adjust this number as needed

    total_ports = end_port - start_port + 1
    completed_ports = [0]  # Using a list to allow shared access between threads
    results = []  # List to hold scan results
    completed_ports_lock = threading.Lock()
    results_lock = threading.Lock()

    print(f"Scanning target: {target}")
    print(f"Time started: {str(datetime.now())}")

    port_queue = Queue()

    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    # Start the progress printing thread
    progress_thread = threading.Thread(target=print_progress, args=(total_ports, completed_ports))
    progress_thread.daemon = True
    progress_thread.start()

    # Start the port scanning threads
    for _ in range(num_threads):
        thread = threading.Thread(target=port_scanner_worker, args=(target, port_queue, completed_ports, results))
        thread.start()

    port_queue.join()

    print(f"Time finished: {str(datetime.now())}")

    # Ask user if they want to save results
    save_results(results)
