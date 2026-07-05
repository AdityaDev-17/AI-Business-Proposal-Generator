from langgraph.graph import StateGraph, START, END

from app.state import AgentState
from app.planner import planner
from app.executor import executor


# Create the graph
graph_builder = StateGraph(AgentState)

# Add nodes
graph_builder.add_node("planner", planner)
graph_builder.add_node("executor", executor)

# Define flow
graph_builder.add_edge(START, "planner")
graph_builder.add_edge("planner", "executor")
graph_builder.add_edge("executor", END)

# Compile graph
workflow = graph_builder.compile()