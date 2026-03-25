# langgraph-mcp-agents
A hands-on learning repository covering LangGraph fundamentals — from basic chatbots and human-in-the-loop workflows to multimodal RAG, multi-agent systems, and MCP server integration with LangChain.

📁 Project Structure
2-LANGGRPAH-MCP/
├── 1-BasicChatbot/
│   └── 1-basicchatbot.ipynb          # Simple LangGraph chatbot with message state
├── 2-HumanAssistance/
│   └── humaninloop.ipynb             # Human-in-the-loop with interrupt and approval flows
├── 3-Debugging/
│   ├── agent.py                      # Agent definition for debugging demos
│   ├── debugging.ipynb               # LangGraph Studio & LangSmith tracing walkthrough
│   ├── LangGraph_Debug_Monitoring_Notes.docx
│   └── langgraph.json                # LangGraph Studio config
├── 4-Multimodal/
│   ├── multimodal_rag_notes.docx
│   ├── multimodal_sample.pdf
│   └── multimodalopenai.ipynb        # Multimodal RAG with vision + OpenAI
├── Agents/
│   ├── multi_agent_langgraph_notes.docx
│   └── multiaiagent.ipynb            # Multi-agent orchestration with LangGraph
├── mcpdemolangchain/
│   ├── client.py                     # MCP client connecting to tool servers
│   ├── mathserver.py                 # MCP math tool server
│   └── weather.py                    # MCP weather tool server
├── main.py                           # Entry point
├── pyproject.toml
├── requirements.txt
└── .env                              # API keys (not committed)


🧩 Modules Overview
1 — Basic Chatbot
Build a minimal stateful chatbot using StateGraph with MessagesState. Covers nodes, edges, and how LangGraph manages conversation history.
2 — Human Assistance (Human-in-the-Loop)
Implement interrupt() to pause graph execution for human review or approval. Demonstrates how to resume the graph after human input using Command.
3 — Debugging & Monitoring
Use LangGraph Studio for visual graph inspection and LangSmith for tracing. Covers how to structure a langgraph.json config, set checkpointers, and monitor state transitions.
4 — Multimodal RAG
Build a Retrieval-Augmented Generation pipeline that handles both text and images using OpenAI's vision models. Includes a sample PDF and notes.
5 — Multi-Agent Systems
Orchestrate multiple AI agents using LangGraph's supervisor and handoff patterns. Each agent has a specialized role; the graph routes tasks between them.
6 — MCP Demo (LangChain + MCP)
Connect LangChain agents to external tools via the Model Context Protocol (MCP). Includes a local math server and weather server, and a client that wires them together.


🛠️ Tech Stack
ToolPurposeLangGraphStateful agent graph frameworkLangChainLLM chains and tool integrationsOpenAILLM + vision model providerLangSmithTracing and observabilityMCPModel Context Protocol for tool servers

📚 Learning Path
Follow the modules in order for the best experience:
1-BasicChatbot → 2-HumanAssistance → 3-Debugging → 4-Multimodal → Agents → MCP
