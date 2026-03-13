from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition
from src.MCP_Client.models.state_mode import State
from src.MCP_Client.nodes.chat_llm_node import chat_llm
from src.MCP_Client.nodes.tool_call_node import tool_call

agent_builder = StateGraph(State)

agent_builder.add_node("chat_llm", chat_llm)
agent_builder.add_node("tools", tool_call)

agent_builder.add_edge(START, "chat_llm")

agent_builder.add_conditional_edges(
    "chat_llm",
    tools_condition,
)

agent_builder.add_edge("tools", "chat_llm")

agent = agent_builder.compile()

try:
    with open ("agent_mcp.png", "wb") as f:
        f.write(agent.get_graph().draw_mermaid_png())
except Exception as e:
    print(f"Could not draw graph: {e}")
