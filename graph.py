from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from agents import (manager_agent, research_agent, coding_agent, testing_agent, report_agent)
from tools import search_web

# Shared State
class NexusState(TypedDict):
    task: str
    category: str
    research: str
    code: str
    review: str
    final: str


# 1. Manager Node
def manager_node(state):
    print("Manager Agent is working...")
    category = manager_agent(state["task"])
    print("Selected Category:", category)
    return {"category": category}

# 2. Research Node
def research_node(state):
    print("Research Agent is working...")
    search_data = search_web(state["task"])
    result = research_agent(state["task"],search_data)
    return {"research": result}

# 3. Coding Node
def coding_node(state):
    print("Coding Agent is working...")
    code = coding_agent(state["task"])
    return {"code": code}

# 4. Testing Node
def testing_node(state):
    print("Testing Agent is reviewing code...")
    review = testing_agent(state["task"], state.get("code", ""))
    return {"review": review}

# 5. Report Node
def report_node(state):
    print("Report Agent is preparing final report...")
    results = {
        "Category": state.get("category", ""),
        "Research": state.get("research", ""),
        "Code": state.get("code", ""),
        "Testing": state.get("review", "")
    }
    final_report = report_agent(state["task"], results)
    return {"final": final_report}

# Route According to Task
def route_task(state):
    category = state.get("category", "GENERAL")
    if category == "CODE":
        return "coding"
    elif category == "RESEARCH":
        return "research"

    return "report"

# Build LangGraph
builder = StateGraph(NexusState)

builder.add_node("manager", manager_node)
builder.add_node("research", research_node)
builder.add_node("coding", coding_node)
builder.add_node("testing", testing_node)
builder.add_node("report", report_node)

builder.add_edge(START, "manager")
builder.add_conditional_edges("manager",
    route_task,
    {
        "coding": "coding",
        "research": "research",
        "report": "report"
    }
)

builder.add_edge("research", "report")
builder.add_edge("coding", "testing")
builder.add_edge("testing", "report")
builder.add_edge("report", END)

# Compile Graph
nexus_graph = builder.compile()
print("NexusAI: LangGraph Workflow Loaded Successfully!")
