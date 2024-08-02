# Port Scanner

Welcome to the Port Scanner project! This Python-based application scans ports on a specified host to check for open ports and services.

## Overview
The Port Scanner allows users to scan a range of ports on a target host to identify which ports are open. It’s a useful tool for network administrators and security professionals to assess the state of their network and services.

## Features
- Scan a specified range of ports on a target host.
- Identify open ports and display results.
- Simple command-line interface.

## Installation
To run the Port Scanner, follow these steps:
1. **Clone the repository:** ```bash git clone https://github.com/Danilo-Mugnaini/port_scan.git cd port_scan ```
2. **Create and activate a virtual environment (optional but recommended):** ```bash python -m venv venv source venv/bin/activate  # On Windows use `venv\Scripts\activate` ```
3. **Install the required packages:** You can create a `requirements.txt` file with the following content: ``` ```
   Install any additional packages if necessary.

## Usage
To start using the port scanner, run the following command: ```bash python port_scanner.py <target_host> <start_port> <end_port> ```
Replace `<target_host>` with the IP address or hostname of the target, `<start_port>` with the starting port number, and `<end_port>` with the ending port number.

### Example
```bash python port_scanner.py 192.168.1.1 1 1024 ```
This command will scan ports 1 to 1024 on the host `192.168.1.1`.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please contact [Danilo Mugnaini](https://github.com/Danilo-Mugnaini).
