On-Box-InterfaceHealth

This project script periodically checks the status and error count of Ethernet interfaces on your NX-OS/IOS-XE device. If it detects any issues (interfaces that are down or have errors), it prints an alert. 

## Files

- `OnBox-InterfaceHealth.py`: Contains the on-box python script.

## Installation

1. Clone the repository:

    git clone https://github.com/CobraTamer/On-box-App_InterfaceHealth.git


## Usage


	1.	Access Your NX-OS Device:
	•	Open your terminal or SSH client (like PuTTY, SecureCRT, or a terminal emulator on Linux/Mac).
	•	Connect to your NX-OS device using SSH. Example:

ssh admin@your-nxos-device-ip


	2.	Enable Bash Shell:
	•	On the NX-OS device, enable the Bash shell to use Linux-like commands. Enter configuration mode and enable Bash:

conf t
feature bash-shell
exit
run bash


	3.	Create the Script:
	•	Use a text editor like vim to create the script file. Example:

vim interface_health_check.py

	3.	
	•	In vim, press i to enter insert mode, then copy and paste the script above into the editor.
	•	Press Esc, then type :wq and press Enter to save and exit.
	4.	Make the Script Executable:
	•	Change the permissions to make the script executable:

chmod +x interface_health_check.py


	5.	Run the Script:
	•	Execute the script using Python, do this in NX-OS mode not bash:

python3 interface_health_check.py




## Example Output

When you run the app, you should see "started interface monitoring..."
When the script detects issue, you will see output similar to this in your terminal:
Issue detected: {interface: Ethernet1/4, Status: down, Errors:8}
Interface health check completed.
 