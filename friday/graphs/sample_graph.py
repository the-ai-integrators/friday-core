from typing import TypedDict, Dict, Optional
from langgraph.graph import StateGraph, END
from friday.agents.search_agent import SearchAgent
from friday.agents.math_agent import MathAgent


class SimpleState(TypedDict, total=False):
    input: str
    search_result: Dict
    math_result: str


def create_simple_graph():
    graph = StateGraph(SimpleState)

    search_agent = SearchAgent()
    math_agent = MathAgent()

    # --- Node 1: Search ---
    def node_search(state: SimpleState):
        query = state.get("input", "")
        result = search_agent.run(query)
        return {"search_result": result}   # THIS WILL BE RETURNED

    # --- Node 2: Math ---
    def node_math(state: SimpleState):
        expression = state.get("input", "")
        result = math_agent.run(expression)
        return {"math_result": result}     # THIS WILL BE RETURNED

    graph.add_node("search", node_search)
    graph.add_node("math", node_math)

    graph.set_entry_point("search")
    graph.add_edge("search", "math")
    graph.add_edge("math", END)

    return graph.compile()
