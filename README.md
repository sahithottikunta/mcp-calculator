# 🧮 Ultimate Python MCP Server

A Model Context Protocol (MCP) server built with Python using the `FastMCP` framework. This server exposes a set of core mathematical tools, instruction prompts, and read-only resources that an AI assistant (like Claude Desktop or VS Code Copilot) can interact with dynamically.

## 🚀 Features

- **Tools:** `add` and `multiply` operations that automatically infer schemas via Python type hints and docstrings.
- **Resources:** A read-only documentation resource located at `memo://docs/calculator-guide`.
- **Prompts:** A dynamic `math_tutor_prompt` template to configure an AI assistant into a patient math instructor.

---

## 🛠️ Local Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.10+** and **Node.js** (v20+) installed on your machine. 

### 2. Clone and Setup Environment
Clone this repository to your local machine, open the folder, and create a virtual environment:

```bash
# Create the virtual environment
python -m venv .venv

# Activate the virtual environment (Windows)
.venv\Scripts\activate

# Activate the virtual environment (Mac/Linux)
source .venv/bin/activate
3. Install Dependencies
Install the required Model Context Protocol SDK with developer CLI capabilities:

Bash
pip install "mcp[cli]"
🔬 Testing with MCP Inspector
Since MCP servers utilize standard input/output (stdio) channels to communicate with language models, you cannot test them by running a normal Python execution command. Use the official visual web inspector instead:

Bash
npx @modelcontextprotocol/inspector python calculator_server.py
Open the local link generated in your browser (typically http://localhost:5173).

Set Command to python.

Set Arguments to calculator_server.py.

Click Connect to begin interacting with the tools, resources, and prompts visually!