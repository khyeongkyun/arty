# src/graphs/main_graph.py
from langgraph.graph import StateGraph, START, END
from langgraph.types import Send

from state.schema import State
from agents.director import director
from agents.worker import researcher
from agents.sender import sender

def assign_workers(state: State):
    return [Send("researcher", {"section": s}) for s in state["sections"]]

def build_graph():
    builder = StateGraph(State)

    builder.add_node("director", director)
    builder.add_node("researcher", researcher)
    builder.add_node("sender", sender)

    builder.add_edge(START, "director")
    builder.add_conditional_edges(
        "director", assign_workers, ["researcher"]
    )
    builder.add_edge("researcher", "sender")
    builder.add_edge("sender", END)

    return builder.compile()
