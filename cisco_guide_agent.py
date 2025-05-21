KNOWLEDGE_BASE = [
    {
        "keywords": ["router", "add router", "insert router"],
        "response": "To add a router in Packet Tracer, go to 'Network Devices' > 'Routers' and drag your desired router model onto the workspace."
    },
    {
        "keywords": ["connect devices", "cable", "link"],
        "response": "To connect devices, select 'Connections' (the lightning bolt icon), choose the appropriate cable type (e.g., Copper Straight-Through for PC to Switch, Copper Cross-Over for PC to PC or Switch to Switch), and click on the devices you want to connect."
    },
    {
        "keywords": ["ping", "test connectivity"],
        "response": "To test connectivity using ping: Click on a PC, go to the 'Desktop' tab, open 'Command Prompt', and type 'ping <IP_ADDRESS_OF_OTHER_DEVICE>'. For example, 'ping 192.168.1.2'."
    },
    {
        "keywords": ["ip address", "configure ip", "set ip"],
        "response": "To configure an IP address on a PC: Click the PC > Desktop tab > IP Configuration. Select 'Static' and enter the IP address, Subnet Mask, and Default Gateway."
    },
    {
        "keywords": ["vlan", "virtual lan", "configure vlan"],
        "response": "To configure a VLAN on a switch: \n1. Enter global configuration mode: `enable` -> `configure terminal` \n2. Create VLAN: `vlan <VLAN_ID>` (e.g., `vlan 10`) \n3. Name VLAN (optional): `name <VLAN_NAME>` (e.g., `name Sales`) \n4. Assign ports to VLAN: `interface <INTERFACE_ID>` (e.g., `interface fa0/1`) -> `switchport mode access` -> `switchport access vlan <VLAN_ID>`"
    }
]

def find_answer(query):
    query_lower = query.lower()
    for entry in KNOWLEDGE_BASE:
        for keyword in entry["keywords"]:
            if keyword.lower() in query_lower:
                return entry["response"]
    return "Sorry, I don't have information on that topic. Try rephrasing your question or using different keywords."

if __name__ == "__main__":
    print("Welcome to the Cisco Packet Tracer Guide Agent!")
    print("Ask me about configurations or commands (e.g., 'how to add a router?', 'configure vlan', 'ping command'). Type 'exit' to quit.")
    
    while True:
        user_query = input("> ")
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break
        
        answer = find_answer(user_query)
        print(answer)
        print("-" * 20) # Separator for readability
