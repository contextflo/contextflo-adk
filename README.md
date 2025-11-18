# ContextFlo ADK Agent

AI agent powered by Google ADK (Agent Development Kit) and Gemini that integrates natively with ContextFlo MCP tools for database analysis and insights.

## Features

- **Natural Language Database Queries**: Ask questions about your data in plain English
- **Step-by-Step Execution**: Interactive web UI shows tool calls and results in real-time (like Claude web app)
- **Native MCP Integration**: Uses ADK's built-in `MCPToolset` with Streamable HTTP connection
- **Full ContextFlo Tool Access**: All MCP tools automatically available:
  - Get organization info and data structure
  - List and explore database tables
  - Execute SQL queries with safety checks
  - Find related saved queries and patterns
  - Create and manage dashboards
  - Access business metrics and concepts

## Prerequisites

1. **Python 3.10+** installed
2. **MCP Server** running (the ContextFlo MCP server at `apps/mcp-server`)
3. **Google API Key** from [Google AI Studio](https://aistudio.google.com/apikey)
4. **MCP API Key** for authentication with your MCP server

## Setup

### 1. Install uv (if not already installed)

```bash
# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with pip:
pip install uv
```

### 2. Install Dependencies

```bash
cd apps/contextflo_agent
uv sync
```

This creates a virtual environment and installs all dependencies automatically.

### 3. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and add your credentials:
```env
GOOGLE_API_KEY=your_actual_google_api_key
MCP_API_KEY=your_actual_mcp_api_key
MCP_SERVER_URL=https://mcp.contextflo.com/mcp
```
## Running the Agent

### ADK Web UI (Recommended)

Launch Google ADK's interactive chat interface:

```bash
# From the apps directory (not apps/web - that's your Next.js app!)
cd apps
uv run adk web
```

Then:
1. Open your browser to `http://localhost:8000`
2. Select **"contextflo_agent"** from the dropdown
3. Start chatting!

**Note:** This launches ADK's built-in web interface, which is separate from your Next.js app in `apps/web`.
