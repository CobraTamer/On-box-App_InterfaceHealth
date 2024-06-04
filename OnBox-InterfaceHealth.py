import cli
import time

def check_interface_health():
    try:
        output = cli.cli("show interface")
        interfaces = parse_interface_output(output)
        for interface in interfaces:
            if interface['errors']  0 or interface['status'] != 'up':
                log_issue(interface)
        print("Interface health check completed.")
    except cli.CliError as e:
        print(f"Error during interface health check: {e}")

def parse_interface_output(output):
    # This function parses the output of "show interface" and returns a list of dictionaries
    # Each dictionary contains details about an interface
    interfaces = []
    # Parsing logic goes here...
    return interfaces

def log_issue(interface):
    print(f"Issue detected: {interface}")

while True:
    check_interface_health()
    print("started interface monitoring...")
    time.sleep(3600)  # Check every hour