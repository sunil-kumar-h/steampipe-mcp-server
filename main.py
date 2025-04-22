# server.py
from mcp.server.fastmcp import FastMCP
import subprocess

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


@mcp.tool()
def steampipe_query(sql: str) -> str:
    """
   Executes a Steampipe SQL query just like in the terminal and returns the output.

   Args:
       sql (str): The SQL query to run. Example: "select count(*) from aws_ec2_instance"

   Returns:
       str: Raw terminal output from the Steampipe query.
   """
    try:
        result = subprocess.run(
            ["steampipe", "query", sql],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"
