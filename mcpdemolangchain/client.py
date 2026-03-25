import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )

    tools = await client.get_tools()
    model = ChatGroq(model="llama-3.1-8b-instant")
    agent = create_agent(model, tools)

    # test math
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is 3 + 5 * 2"}]}
    )
    print("Math:", math_response["messages"][-1].content)

    # test weather
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in California?"}]}
    )
    print("Weather:", weather_response["messages"][-1].content)

asyncio.run(main())