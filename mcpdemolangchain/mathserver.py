from mcp.server.fastmcp import FastMCP

mcp = FastMCP("math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers
    
    Args:
        a (int): first int
        b (int): second int
    
    Returns:
        int: output int
    """
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers
    
    Args:
        a (int): first int
        b (int): second int
    
    Returns:
        int: output int
    """
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")