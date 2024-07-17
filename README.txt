Basic Network Information Retrieval Tool

This script retrieves network information from the local system.

Features:
- Display the IP address of the local machine.
- List available network interfaces along with their corresponding IP addresses and MAC addresses.
- Perform a ping test to a specified host or IP address to check for connectivity.

Usage:
Run the `network_info_tool.py` script and follow the prompts to retrieve network information and perform a ping test.

Challenges:
- Handling different outputs for network interfaces on Windows and Unix-based systems.
- Ensuring the script works across multiple platforms.

Special Considerations:
- The script uses standard system commands (`ipconfig`/`ifconfig`) and the `ping` command, so it needs appropriate permissions to execute these commands.

Version Control:
- The project is managed using Git for version control.
- Different versions are managed using branches and merges.

Author:
[Your Name]
