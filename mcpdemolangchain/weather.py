from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """Get the weather of a location
    
    Args:
        location (str): the location name
    
    Returns:
        str: weather description
    """
    # in real world you would call a weather API here
    return f"It is always sunny in {location}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")