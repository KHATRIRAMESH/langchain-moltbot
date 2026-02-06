import os
from dotenv import load_dotenv

# Load .env from the project root
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

# Use MemorySaver for simple in-memory checkpointing (async-compatible)
from langgraph.checkpoint.memory import MemorySaver

# ------------------- Tools -------------------
search = DuckDuckGoSearchRun()


@tool
def calculator(expression: str) -> str:
    """Useful for simple math. Example: '2*3+4'"""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


@tool
def read_file(filename: str) -> str:
    """Read a file from the workspace folder"""
    try:
        with open(f"workspace/{filename}", "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"


@tool
def write_file(filename: str, content: str) -> str:
    """Write content to workspace/filename (creates folder if needed)"""
    try:
        os.makedirs("workspace", exist_ok=True)
        with open(f"workspace/{filename}", "w", encoding="utf-8") as f:
            f.write(content)
        return f"✓ Wrote {filename}"
    except Exception as e:
        return f"Error: {e}"


tools = [search, calculator, read_file, write_file]

# ------------------- Agent -------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)  # change to gpt-4o if you want


memory = MemorySaver()

agent = create_react_agent(llm, tools, checkpointer=memory)
