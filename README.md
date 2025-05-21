# Cisco Packet Tracer Guide Agent

This is a simple command-line AI agent that provides help and guidance for Cisco Packet Tracer configurations and commands.

## How it Works

The agent uses a predefined knowledge base of common Packet Tracer tasks, commands, and troubleshooting steps. When you ask a question, it searches this knowledge base for relevant keywords and provides the corresponding information.

## How to Run

1.  Ensure you have Python 3 installed on your system.
2.  Clone this repository or download the `cisco_guide_agent.py` file.
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the agent using the command: `python cisco_guide_agent.py`
6.  The agent will then prompt you for input. Ask questions like:
    *   "How do I add a router?"
    *   "Tell me about VLAN configuration."
    *   "What is the ping command?"
7.  Type `exit` to close the agent.

## Current Knowledge Base Topics

The current knowledge base includes basic information on:
*   Adding routers
*   Connecting devices with cables
*   Using the `ping` command
*   Configuring IP addresses on PCs
*   Basic VLAN configuration on switches

## Limitations

*   The knowledge base is currently limited. More topics and detailed explanations can be added.
*   The agent uses simple keyword matching. It may not understand complex queries or natural language nuances perfectly.
*   It does not interact directly with Cisco Packet Tracer software. It's a standalone guide.
