# calculator_server.py
from mcp.server.fastmcp import FastMCP

# Initialize our FastMCP server app
mcp = FastMCP("calculator")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b

if __name__ == "__main__":
    # This runs the server over standard input/output (stdio)
    mcp.run()