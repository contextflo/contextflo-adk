"""ContextFlo ADK Agent with MCP tool integration."""
import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams


# Get MCP server configuration from environment
MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "http://localhost:3000/mcp")
MCP_API_KEY = os.getenv("MCP_API_KEY")

if not MCP_API_KEY:
    raise ValueError(
        "MCP_API_KEY environment variable is required. "
        "Please set it in your .env file."
    )

# Ensure URL ends with /mcp but don't duplicate it
if not MCP_SERVER_URL.endswith("/mcp"):
    mcp_url = f"{MCP_SERVER_URL}/mcp"
else:
    mcp_url = MCP_SERVER_URL

print(f"🔑 Using Bearer token authentication for {mcp_url}")

# Create MCPToolset with Streamable HTTP connection to ContextFlo MCP Server
contextflo_mcp_tools = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=mcp_url,
        headers={
            "Authorization": f"Bearer {MCP_API_KEY}",
            "Content-Type": "application/json"
        }
    ),
)

# Create the ADK Agent with MCP tools
root_agent = Agent(
    name="contextflo_agent",
    model="gemini-pro-latest",
    description="AI agent that helps users analyze and explore their database using ContextFlo MCP tools.",
    instruction="""You are a helpful AI assistant that helps users analyze their database and create insights using ContextFlo's powerful data tools.
    For new questions, call `getOrgInfo` tool and follow the workflow defined in the response. Remmeber users expect multi step workflows to answer their questions.
    Do one step at a time each time explaning users what you are doing. The key is to assist users in their data analysis and help them understand their data better.
""",
    tools=[contextflo_mcp_tools],
)

